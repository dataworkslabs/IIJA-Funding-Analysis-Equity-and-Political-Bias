import pandas as pd

# 1. Load the data
df = pd.read_csv('processed_iija_data_phase1.csv')

# 2. Calculate Funding Per Capita
# We multiply by 1 billion because the 'Total' column is in billions
df['Funding_Per_Capita'] = (df['Total (Billions)'] * 1_000_000_000) / df['Population']

# 3. Clean the data (removing rows with missing population like Tribal Nations)
df_clean = df.dropna(subset=['Funding_Per_Capita']).copy()

# 4. Group by Political Winner
# This calculates the average per-person funding for Biden states vs. Trump states
political_summary = df_clean[df_clean['2020_Election_Winner'].isin(['Biden', 'Trump'])].groupby('2020_Election_Winner')['Funding_Per_Capita'].mean()

# 5. Find the extremes (Equity Check)
top_5 = df_clean.sort_values('Funding_Per_Capita', ascending=False).head(5)
bottom_5 = df_clean.sort_values('Funding_Per_Capita', ascending=True).head(5)

# 6. Print the findings to your screen
print("--- POLITICAL BIAS ANALYSIS ---")
print(political_summary)
print("\n--- TOP 5 HIGHEST FUNDED (PER CAPITA) ---")
print(top_5[['State, Teritory or Tribal Nation', 'Funding_Per_Capita']])
print("\n--- BOTTOM 5 LOWEST FUNDED (PER CAPITA) ---")
print(bottom_5[['State, Teritory or Tribal Nation', 'Funding_Per_Capita']])

# 7. Save this new calculated data to a new CSV for the next phase
df_clean.to_csv('iija_analysis_phase2_results.csv', index=False)