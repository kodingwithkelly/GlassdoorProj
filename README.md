# Glassdoor Data Analyst Essential Knowledge Guide: Project Overview 
* Web scraped 20 pages of Glassdoor using BeautifulSoup and Selenium to obtain 200 interview questions from 146 companies to create a study guide and scraped 1000 data analyst job postings to visualize trends.
* Cleaned and preprocessed data using Pandas and NumPy 
* Analyzed essential data analytics job skills with NLP techniques: Word2Vec, Topic Modeling with LDA, and Rule-Based Matching
* Explored the data and created visualizations using Seaborn and Matplotlib.
* Developed a model using sklearn to estimate data analyst salaries. **(In progress)**

## Conclusion


## Code and Resources Used 
**Packages:** selenium, beautifulSoup, time, pandas, numpy, pyLDAvis, gensim, nltk, re, pprint, spacy, collection, matplotlib, seaborn

**Project Inspiration:** 

https://github.com/PlayingNumbers/ds_salary_proj (Ken Jee)

**Web Scraping and Login Code:** 

https://github.com/arapfaik/scraping-glassdoor-selenium

https://github.com/williamxie11/glassdoor-interview-scraper/blob/master/scraper_v1.2.py

**Useful guides:**

https://www.machinelearningplus.com/spacy-tutorial-nlp/#phrasematcher (Shrivarsheni, spaCy tutorial)

https://www.youtube.com/watch?v=Otde6VGvhWM (Krish Naik, word2vec tutorial)


## Web Scraping
Web scraped 1,000 Data Analyst job listings on Glassdoor for the following features: 

* Job title
* Salary Estimate
* Job Description
* Company Name
* Company Rating
* Location
* Size
* Industry 

As well as 200 most popular Data Analyst interview questions on Glassdoor.

## Data Cleaning
After web scraping and discovering the data I had, I made the following changes:
* Job Listing
  * Removed null salary rows
    * Created new columns for min, max, and average salary
  * Separated the company name from rating 
  * Reformatted size and industry such that "Size: " and "Industry: " was removed from each value
    * Replaced N/A with NaN
  * Separated location into city and state
    * If location = "United States" then NaN for both
    * If location = "Remote" then "Remote" for both
    * If location = a state then NaN for city and state = state
  * Reordered columns for clarity
  * Merged 7 csv files together 
* Interview Questions
  * Reordered the list by company name alphabetically descending
  * Added categories for the type of questions. **(In progress)**
  
## EDA
Below are a few graphs from my EDA. 

![alt text](https://github.com/kodingwithkelly/GlassdoorProj/blob/main/Readme_pngs/LDA.png "LDA")
![alt text](https://github.com/kodingwithkelly/GlassdoorProj/blob/main/Readme_pngs/distribution_salary.png "Distribution Salary")
![alt text](https://github.com/kodingwithkelly/GlassdoorProj/blob/main/Readme_pngs/listing_map.png "Map of Listings")
![alt text](https://github.com/kodingwithkelly/GlassdoorProj/blob/main/Readme_pngs/size_count.png "Size Count")

## Future Work

