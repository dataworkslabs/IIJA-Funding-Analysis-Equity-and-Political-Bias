#  IIJA Funding Analysis: Equity and Political Bias

##  Project Overview
This project looks at how the Infrastructure Investment and Jobs Act (IIJA) money was actually handed out as of March 2023. Instead of just looking at the big "billions" numbers—which can be misleading—I focused on funding per person. This makes it much easier to see the real story behind where the money is going and whether it’s being shared fairly across different states.

##  Core Research Questions
I combined the official government funding list with 2023 Census data and the 2020 election results to answer two main things:
Is it political? Did the states that voted for Joe Biden get more money, or did the funding follow a different set of rules?
1. Is the funding equitable based on state population?
2. Does the allocation favor the political interests of the Biden administration?

##  Key Insights
* **The "Small State" Advantage:** Funding is significantly skewed toward low-population, rural states. States like Alaska and Wyoming receive over $3,000 per person, while populous states like Texas and Florida receive less than $400.
* **Lack of Partisan Bias:** Despite being a signature Biden administration bill, states that voted for Donald Trump in 2020 receive, on average, **higher funding per capita** ($1,137) than states that voted for Joe Biden ($671).
* **Formula-Driven Allocation:** The data suggests that funding is driven by geographic infrastructure needs (road mileage, rural bridges) rather than political favoritism or pure population density.

##  Visualizations

### 1. Per Capita Funding by State
This chart highlights the disparity in per-capita funding across the country, showing a clear preference for rural/small-population areas.
![Equity Analysis](./visuals/1_equity_analysis.png)

### 2. Political Comparison (Biden vs. Trump States)
A direct comparison showing that "Red" states are the primary beneficiaries of IIJA funds on a per-person basis.
![Political Bias Analysis](./visuals/2_political_bias.png)

##  Technologies Used
* **Python 3.14**
* **Pandas:** Data cleaning and merging.
* **Matplotlib & Seaborn:** Data visualization.

##  Project Structure
* `data/`: Contains the raw and processed CSV files.
* `scripts/`: Python scripts for analysis and visualization.
* `visuals/`: Generated charts used in the report.
* `IIJA_Analysis_Report.pdf`: The final summary document.

## How to Reproduce
1. Clone this repository.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
