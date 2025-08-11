import requests
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS

# scrape from remote ok api

url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}

print("Fetching jobs from RemoteOK...")
resp = requests.get(url, headers=headers)
jobs = resp.json()

all_jobs = []
for job in jobs[1:]:  # index 0 = metadata
    title = job.get('position', '')
    description = job.get('description', '')
    all_jobs.append({'title': title, 'description': description})

df = pd.DataFrame(all_jobs)
df.to_csv('jobs.csv', index=False)
print(f"✅ Scraped {len(df)} jobs.")

if df.empty:
    print("No jobs found. Exiting.")
    exit()

# frequency analysis

skills = ["python", "java", "javascript", "c++", "sql", "aws", "docker", "react", "node", "tensorflow","pytorch","azure"]
freq = {skill: 0 for skill in skills}

for desc in df['description']:
    text = desc.lower()
    for skill in skills:
        if re.search(rf"\b{skill}\b", text):
            freq[skill] += 1

skill_df = pd.DataFrame(list(freq.items()), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)
skill_df.to_csv('skill_counts.csv', index=False)
print("\nTop Skills Found:\n", skill_df)

# Visualization with bar charts
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(data=skill_df, x='Count', y='Skill', palette='viridis')
plt.title("Top Tech Skills in RemoteOK Job Postings")
plt.tight_layout()
plt.savefig('skills_bar.png')
print("Saved bar chart: skills_bar.png")

# Visualization using word cloud
def clean_html_text(raw_html: str) -> str:
    """Strip HTML, urls, and common html/css artifacts; return normalized plain text."""
    soup = BeautifulSoup(raw_html or "", 'html.parser')
    text = soup.get_text(" ")                    # remove tags
    text = re.sub(r'http\S+|www\.\S+', ' ', text)   # remove urls

    text = re.sub(r'\b(li|nbsp|span|style|font|px|br|strong|amp|div|class)\b', ' ', text, flags=re.I)
    # keep letters, numbers and a few useful symbols (+, #, ., -)
    text = re.sub(r'[^A-Za-z0-9\s\+\#\.\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Clean every description and join
cleaned_descriptions = [clean_html_text(d) for d in df['description'].astype(str)]
text_data = " ".join(cleaned_descriptions)

# Build stopwords (include default + a few custom tokens common in job posts)
stopwords = set(STOPWORDS)
stopwords.update([
    'li','nbsp','span','style','font','px','br','strong','amp','div','class',
    'please','applicants','job','position','apply','applying','experience','team'
])

wc = WordCloud(
    width=800, height=400,
    background_color='white',
    stopwords=stopwords,
    max_words=200,
    collocations=False,   # avoid joining words like "machine learning" into a single token
    prefer_horizontal=0.9
).generate(text_data)

wc.to_file('wordcloud.png')
print("Saved cleaned word cloud: wordcloud.png")

