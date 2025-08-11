# RemoteOK Job Skills Scraper and Analysis

This Python project scrapes job listings from the [RemoteOK API](https://remoteok.com/api), analyzes the frequency of key tech skills mentioned in job descriptions, and generates visualizations to highlight trending skills in the remote job market.

---

## Features

- **Job Data Scraping**: Fetches remote job postings including position titles and detailed descriptions.
- **Skill Frequency Analysis**: Counts occurrences of a predefined list of popular tech skills in job descriptions using regex.
- **Data Storage**: Saves scraped job data and skill frequency counts as CSV files for further analysis.
- **Visualizations**:
  - Bar chart displaying the most in-demand skills.
  - Word cloud highlighting frequent terms from job descriptions (with cleaning and custom stopwords).

---

## Technologies Used

- Python 3.13
- `requests` — for making HTTP requests to the RemoteOK API
- `pandas` — for data manipulation and CSV handling
- `re` (regex) — for skill pattern matching in text
- `BeautifulSoup` (bs4) — for cleaning HTML tags from job descriptions
- `matplotlib` and `seaborn` — for data visualization (bar charts)
- `wordcloud` — to generate word cloud images from job descriptions

---

## Setup and Usage

1. **Clone the repository**

```bash
git clone https://github.com/nikhil_sethu/trending-skills.git
cd trending-skills 
```

2. **Install dependencies**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scraper and analysis**
   ```bash
   python3.13 scraper.py
   ```

  # Customization

- Modify the **skills** list in the script to analyze different or additional skills.  
- Update **stopwords** in the word cloud section to exclude irrelevant words.

---

# Learning Goals

This project is designed to practice and demonstrate:

- Working with REST APIs and JSON data  
- Text cleaning and processing with regex and BeautifulSoup  
- Data analysis and visualization using pandas, matplotlib, seaborn, and wordcloud  
- Combining multiple Python libraries for end-to-end data science workflows

---

# License

This project is open source and available under the MIT License.

---

# Contact

Created by Nikhil — feel free to reach out for collaboration or questions!

5.	**Outputs**
- `jobs.csv`: Contains all scraped job titles and descriptions.
- `skill_counts.csv`: Skill frequency counts sorted by demand.
- `skills_bar.png`: Bar chart visualization of top skills.
- `wordcloud.png`: Word cloud image from job descriptions.(Still a work in progress, trying to get rid of url tags)
