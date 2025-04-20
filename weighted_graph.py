import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


META_CSV = "state_meta.csv"          # columns: state,pop,area
STATES   = pd.read_csv(META_CSV)["state"].tolist()

# minimal contiguous‑border map (add AK–HI self‑loops later)
BORDERS = {
    "Alabama": ["Florida","Georgia","Mississippi","Tennessee"],
    "Alaska":  [],
    # … (fill out all 51) …
    "Wyoming": ["Colorado","Idaho","Montana","Nebraska","South Dakota","Utah"]
}


def build_weight_matrix(meta, γ1=1.0, γ2=1.0, ε=1e-4):
    """
    meta : DataFrame with index=state, columns=['pop','area']
    returns: W (N×N) row‑stochastic, C (binary contiguity)
    """
    states = meta.index.tolist()
    N      = len(states)
    pop    = np.log(meta["pop"].values)     
    area   = meta["area"].values

    σ_pop  = pop.std()
    σ_area = area.std()

    C = np.zeros((N, N))
    for i,s in enumerate(states):
        for t in BORDERS.get(s, []):
            j = states.index(t)
            C[i,j] = C[j,i] = 1
    np.fill_diagonal(C, 0)

    W = np.zeros_like(C, dtype=float)
    for i in range(N):
        for j in range(i+1, N):
            if C[i,j]:
                diff_pop  = abs(pop[i]-pop[j]) / σ_pop
                diff_area = abs(area[i]-area[j]) / σ_area
                w = np.exp(-γ1*diff_pop**2 - γ2*diff_area**2)
                W[i,j] = W[j,i] = w

    W += ε
    row_sum = W.sum(axis=1, keepdims=True)
    W      /= row_sum
    return W, C

def to_networkx(W, states):
    G = nx.DiGraph()                    
    for i,s in enumerate(states):
        G.add_node(s)
    for i in range(len(states)):
        for j in range(len(states)):
            if i != j:
                G.add_edge(states[i], states[j], weight=float(W[i,j]))
    return G


def laplacian_regression(X, y, W, lamb=1.0):
    """
    Solve  (XᵀX + λ Xᵀ L X) β = Xᵀ y   where L=D-W.
    """
    D    = np.diag(W.sum(1))
    L    = D - W
    XtX  = X.T @ X
    A    = XtX + lamb * (X.T @ L @ X)
    b    = X.T @ y
    β    = np.linalg.solve(A, b)
    return β


def synth_emissions(states, years=10, seed=0):
    rng   = np.random.default_rng(seed)
    base  = rng.uniform(2.5, 5.0, len(states))          # baseline log‑CO₂
    trend = rng.normal(0, 0.01, len(states))            # small drift
    Y     = {}
    for t in range(years):
        noise = rng.normal(0, 0.05, len(states))
        Y[1970+t] = np.exp(base + trend*t + noise)      # convert back
    return pd.DataFrame(Y, index=states).T

def main():
    meta = pd.read_csv(META_CSV, index_col="state")
    W,_  = build_weight_matrix(meta)
    G    = to_networkx(W, meta.index.tolist())

    X = np.column_stack([
        np.ones(len(meta)),
        np.log(meta["pop"].values),
        meta["area"].values
    ])
    emissions = synth_emissions(STATES).iloc[-1].values  
    β = laplacian_regression(X, emissions, W, lamb=1.0)
    print("β̂ (Laplacian‑regularised):", β.round(4))

    #quick visual
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_size=300, alpha=0.7,
            edge_color=[G[u][v]['weight'] for u,v in G.edges()],
            edge_cmap=plt.cm.Blues, with_labels=True)
    plt.title("Row‑stochastic weight graph")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
