# Climate Data Review: Entry 1

## Step 1: Reviewing the GitHub Repository

For our first step, we reviewed this GitHub repository as recommended by the class syllabus: **Datasets, APIs, and Open Source Projects Related to Climate Change**.  

As we parsed through the repository, we—like the repo itself—categorized resources into **APIs** and **Databases**. Our initial conclusions were as follows:

### Key Observations

1. **APIs require detailed documentation and are not always free.** Databases will be our preferred choice for accessing geo-longitudinal air quality data due to their reliability and accessibility.  
2. **We prioritized air quality data** but also included CO₂ and methane emissions as complementary datasets.  
3. **There is more than enough data for our needs** (at least at first glance). Our approach will be **top-down**, meaning we will start with the most robust datasets and, as time allows, explore additional sources to strengthen our analysis. Not all APIs or datasets will be used, but we aim to incorporate as many relevant ones as possible.  
4. **Many datasets include overlapping information** from other sources, making them non-unique. We will keep this in mind and consolidate data where necessary as we progress.  

---

## APIs

- **Air Quality Programmatic APIs** – Free but has unclear documentation.  
- **AirVisual Platform** – Robust, easy to understand, and free.  
- **BreezoMeter** – Pricing unclear, sparse documentation.  
- **OpenAQ API Docs** – Limited and complex platform.  
- **Carbon Intensity API** – Reliable and robust; useful as a secondary source for indirect air pollution insights.  

---

## Databases

- **CO₂ Emissions from Fossil Fuels since 1751 (by Nation)** – Reliable; minimal documentation concerns.  
- **CO₂ PPM - Trends in Atmospheric Carbon Dioxide** – Same as above.  
- **Greenhouse Gas Emissions per 1,000 Kilocalories** – Same as above.  
- **Hockeystick (R Package)** – Same as above.  
- **How Many Gigatons of Carbon Dioxide...?** – Same as above.  
- **CO₂ and Greenhouse Gas Emissions** – Same as above.

# Climate Data Review: Entry 2
## Potential Questions to Answer:
- US vs. rest of the world (and based on election)
- US across presidencies
- State by state across elections
- County by county across elections
- Assuming endogenous values, the state of the US in 20 years...

# Climate Data Review: Entry 3
- Met with Judah to discuss the project.
- Going to submit a draft to him
- From what it seems, our project has pivoted such that it now:
  - Investigates airpollution across countries across time
  - Find countries that have a steady politics, where party changes are rare, juxtapose those with countries where parties change off. See if there's a fluctuation in the increase in airpllution in those regions and use an unsupervised method to narrow it down to political affiliation.
 
# Climate Data Review: Entry 4 
- finished collecting data
- Found alot of state and county US election data
- Found alot of air pollution data on a state level
- Now I'm going to scope the project to the national instead of international level because of the wealth of data I was able to find

# Climate Data Review: Entry 5
- Found historical election data of the house, senate, and presidency
- Going to combine these three into an index based on party
- Then I'm going to track the index score overtime and find the most extreme - flip-flop states, and the most extremely steady states, and the average
- Then I'm going to layer with climate data and see if a higher score indicates higher pollution. How much can we expect on average?
- Assuming the same trends in these states, how much pollution can we expect in the fututure?
- Can we then create a graph and see if neighboring states' ploitcal association has an effect on it's surroundings? This will have to include proximity and size of these states as variables

# Climate Data Review: Entry 6
- graphed the top ten and bottom ten carbon emitting states
- noticing that (obviously) population and state size play a large role
- to respind to this, I downloaded population and state size data (took a suprisingly long time to find)
- merged all this data into one dataframe that I'll run multivariate regression from
- I'm also trying to upload all my data to github but it's 15G so I'm trying to actually upload it to GoogleDrive and supply the link to github. This I've run through the terminal with notes and has so far taken 2 days for 2G. Assuming 1G a day, I think this will take me two weeks...
- Added a .gitignore file so it wont upload the data folder

- # Climate Data Review: Entry 7
- data almost done upload
- busy last week. will have a lot of time this coming week

- # Climate Data Review: Entry 8
- data ALMOST DONE: 12GB / 14 GB uploaded
- began working on creating a metric for score legilsation. this includes the percent vote a bill recived and wehther it was climate related.

- # Climate Data Review: Entry 9
- Data all uploaded
- all steps completed (badly - need to improve them) except adjacency graph
- making meetings with the TAs discuss further steps and:
  - Impute data? Using KNN?
  - Normalize data?
  - 
-  # Climate Data Review: Entry 10
- Met with Judah today to discuss project
- Making corrections regarding time series analysis

-  # Climate Data Review: Entry 11
- group meeting to discuss progress
- fixed minor bugs and discussed imputation process
- will need to fix some graphs and some data deletion that has been noticed

-  # Climate Data Review: Entry 12
- fixed minor bugs
- fixed a bug that wouldn't show correct party affiliation score on line graph

-  # Climate Data Review: Entry 13
- cleaned up code and organized a bit more in preparation for writing the full research paper