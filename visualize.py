import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the results from Phase 2
df = pd.read_csv('iija_analysis_phase2_results.csv')

# Set the visual style
sns.set_theme(style="whitegrid")

# Define our political colors
color_map = {'Biden': '#1f77b4', 'Trump': '#d62728', 'Territory': '#7f7f7f'}

# --- Chart 1: The Equity Story (Per Capita) ---
plt.figure(figsize=(10, 12))
df_sorted = df.sort_values('Funding_Per_Capita', ascending=False)
colors = [color_map.get(x, '#7f7f7f') for x in df_sorted['2020_Election_Winner']]

plt.barh(df_sorted['State, Teritory or Tribal Nation'], df_sorted['Funding_Per_Capita'], color=colors)
plt.xlabel('Funding Per Person (USD)')
plt.title('Is it Equitable? IIJA Funding Per Resident')
plt.tight_layout()
plt.savefig('1_equity_analysis.png')
plt.close()

# --- Chart 2: The Bias Story (Political Average) ---
political_df = df[df['2020_Election_Winner'].isin(['Biden', 'Trump'])]
avg_funding = political_df.groupby('2020_Election_Winner')['Funding_Per_Capita'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=avg_funding, x='2020_Election_Winner', y='Funding_Per_Capita', palette=color_map)
plt.ylabel('Average Funding Per Person (USD)')
plt.title('Is there Political Bias? Average Funding: Biden vs. Trump States')

# Add the dollar amounts on top of the bars
for i, v in enumerate(avg_funding['Funding_Per_Capita']):
    plt.text(i, v + 20, f"${v:,.2f}", ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('2_political_bias.png')
plt.close()

# --- Chart 3: Funding vs Population ---
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df, x='Population', y='Total (Billions)', hue='2020_Election_Winner', palette=color_map, s=100)
plt.title('Total Funding vs. Population Size')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('3_funding_trend.png')
plt.close()

print("Success! Check your folder for 1_equity_analysis.png, 2_political_bias.png, and 3_funding_trend.png")