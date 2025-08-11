import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# software engineering interns in NYC (target)
BASE_URL = "https://www.indeed.com/jobs?q=software+engineer+intern&l=New+York&start={}"

all_jobs = []

for page in range(0, 30, 10):  # scrape relevant (first 3 pages)
    url = BASE_URL.format(page)
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'html.parser')

    for card in soup.select('div.job_seen_beacon'):
        title = card.find('h2').get_text(strip=True)
        snippet = card.find('div', class_='job-snippet')
        desc = snippet.get_text(" ", strip=True) if snippet else ''
        all_jobs.append({'title': title, 'description': desc})

df = pd.DataFrame(all_jobs)
df.to_csv('jobs.csv', index=False)
print(f"Scraped {len(df)} jobs.")

skills = ["python", "java", "javascript", "c++", "sql", "aws", "docker", "react", "node", "tensorflow"]

freq = {skill: 0 for skill in skills}

for desc in df['description']:
    text = desc.lower()
    for skill in skills:
        if re.search(rf"\b{skill}\b", text):
            freq[skill] += 1

skill_df = pd.DataFrame(list(freq.items()), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)
skill_df.to_csv('skill_counts.csv', index=False)
print(skill_df)