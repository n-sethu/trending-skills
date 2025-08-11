import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load CSVs saved from scraper.py
df = pd.read_csv('jobs.csv')
skill_df = pd.read_csv('skill_counts.csv')

sns.barplot(data=skill_df, x='Count', y='Skill')
plt.title("Top Tech Skills in Job Postings")
plt.tight_layout()
plt.savefig('skills_bar.png')
plt.show()

# Word Cloud (gets relevant skills)
text_data = " ".join(df['description'].tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
wordcloud.to_file('wordcloud.png')