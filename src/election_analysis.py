
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (using the correct CSV filename)
df = pd.read_csv('../kodaqs-test/data/2017_german_election_overall.csv')

# Calculate voter turnout
df['vote_on_voter'] = df['total_votes'] / df['registered.voters']

# Voter turnout boxplot by state
plt.figure(figsize=(10, 16))
sns.boxenplot(y='state', x='vote_on_voter', data=df, palette='Set1')
median_turnout = df['vote_on_voter'].median()
plt.axvline(x=median_turnout, linewidth=2.5, linestyle='--', color='grey')
plt.text(median_turnout + 0.01, 1, f'Median rate: {median_turnout:.2f}', fontsize=14)
plt.title('Voter Turnout by State')
plt.savefig('figures/voter_turnout_by_state.png', bbox_inches='tight')

# Valid first and second votes by state
state_votes = df.groupby('state')[['valid_first_votes', 'valid_second_votes']].sum().sort_values(by='valid_second_votes', ascending=False)
state_votes.plot(kind='bar', figsize=(12, 8))
plt.title('Valid First and Second Votes by State')
plt.ylabel('Number of Votes')
plt.xlabel('State')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/valid_votes_by_state.png', bbox_inches='tight')

# Distribution of invalid votes
df['total_invalid_votes'] = df['invalid_first_votes'] + df['invalid_second_votes']
plt.figure(figsize=(10, 6))
sns.histplot(df['total_invalid_votes'], kde=True, color='red')
plt.title('Distribution of Invalid Votes')
plt.xlabel('Total Invalid Votes')
plt.ylabel('Frequency')
plt.savefig('figures/invalid_votes_distribution.png', bbox_inches='tight')
