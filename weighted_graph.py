import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
def gen_data(states, months):
    d = {}
    for s in states:
        b = random.uniform(40,80)
        svals = [np.sin(2*np.pi*m/12)*random.uniform(5,15) for m in range(months)]
        nvals = np.random.normal(0,2,months)
        d[s] = [b + svals[m] + nvals[m] for m in range(months)]
    return pd.DataFrame(d, index=[f"Month_{i+1}" for i in range(months)])
def sim_matrix(df):
    return df.T.corr()
def build_graph(corr, thr):
    G = nx.Graph()
    for s in corr.columns:
        G.add_node(s)
    for i in range(len(corr.columns)):
        for j in range(i+1, len(corr.columns)):
            s1 = corr.columns[i]
            s2 = corr.columns[j]
            w = corr.iloc[i, j]
            if abs(w) >= thr:
                G.add_edge(s1, s2, weight=w)
    return G
def norm_graph(G):
    ws = [abs(G[u][v]["weight"]) for u, v in G.edges()]
    if ws:
        mi, ma = min(ws), max(ws)
        for u, v in G.edges():
            w = abs(G[u][v]["weight"])
            norm = (w - mi)/(ma - mi) if ma != mi else 1
            G[u][v]["norm"] = norm
    return G
def cluster(G):
    try:
        import community as community_louvain
        return community_louvain.best_partition(G)
    except:
        return {n:0 for n in G.nodes()}
def plot_graph(G, part):
    pos = nx.spring_layout(G, seed=42)
    clust = set(part.values())
    colors = {c: plt.cm.get_cmap("tab20")(i/len(clust)) for i, c in enumerate(clust)}
    ncol = [colors[part[n]] for n in G.nodes()]
    plt.figure(figsize=(10,8))
    nx.draw(G, pos, node_color=ncol, with_labels=True, node_size=600)
    elabels = {(u, v): f"{G[u][v]['weight']:.2f}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)
    plt.title("US States Climate Dependency")
    plt.axis("off")
    plt.show()
def plot_hist(G):
    ws = [abs(G[u][v]["weight"]) for u, v in G.edges()]
    plt.figure(figsize=(6,4))
    plt.hist(ws, bins=10, color="gray", edgecolor="black")
    plt.title("Edge Weight Distribution")
    plt.xlabel("Correlation")
    plt.ylabel("Frequency")
    plt.show()
def plot_clusters(part):
    inv = {}
    for n, c in part.items():
        inv.setdefault(c, []).append(n)
    clusters = list(inv.values())
    sizes = [len(c) for c in clusters]
    plt.figure(figsize=(8,6))
    plt.bar(range(len(sizes)), sizes, color="skyblue")
    plt.title("Cluster Sizes")
    plt.xlabel("Cluster")
    plt.ylabel("Count")
    plt.show()
def main():
    states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
    months = 12
    df = gen_data(states, months)
    corr = sim_matrix(df)
    G = build_graph(corr, 0.8)
    G = norm_graph(G)
    part = cluster(G)
    plot_graph(G, part)
    plot_hist(G)
    plot_clusters(part)
    summary = corr.describe()
    summary.to_csv("climate_summary.csv")
    df.to_csv("synthetic_climate_data.csv")
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    sample_col = df.columns[random.randint(0, len(df.columns)-1)]
    ax.plot(df.index, df[sample_col].values, marker="o", linestyle="-")
    ax.set_title("Sample Trend " + sample_col)
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature")
    plt.show()
if __name__ == "__main__":
    main()
print("Graph analysis complete.")
print("Data saved as CSV.")
