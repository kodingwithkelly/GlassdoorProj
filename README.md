# Glassdoor Data Analyst Essential Knowledge Guide: Project Overview 
* Web scraped 20 pages of Glassdoor using BeautifulSoup and Selenium to obtain 200 interview questions from 146 companies to create a study guide and scraped 1000 data analyst job postings to visualize trends.
* Cleaned and preprocessed data using Pandas and NumPy 
* Analyzed essential data analytics job skills with NLP techniques: Word2Vec, Topic Modeling with LDA, and Rule-Based Matching
* Explored the data and created visualizations using Seaborn and Matplotlib.
* Developed a Support Vector Regression model to estimate data analyst salaries with a mean absolute error of $12,700.

## Conclusion
Streamlit app: kodingwithkelly/streamlit_glassdoor


Currently California and New York have the highest number of listings for a mid-level data analyst with New York City having the most listings. Through a generated map, many of the listings are dispersed in the greater north east area of the United States. On the other hand, the top 2 companies offering data analyst jobs at the moment are Uline and Intuit which are big companies. Though smaller/mid-sized companies with a size of 1001-5000 are looking to grow their company with analysts. 

Lastly, the most covetted technical skills in this career are SQL, Excel, Tabelau, Python, R, and Power BI. While the most sought over soft skills are written and oral communication skills. 


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

## Model Building
The model included the following columns: Rating, State, Size, Industry, and Seniority. 
There were quite a few NaN values which then had to be imputed with means for numerical types and mode for categorical types.
After transforming the categorical variables into dummy variables, I split the data into a 80% training set and 20% testing set.

I then used 3 different models (Support Vector Regression, Random Forest, Decision Tree) and interpreted the results using mean absolute error to see how far off the salaries would be from the actual salary.
## Model Performace
* **Support Vector Regression:** MAE of 12.07
* **Random Forest:** MAE of 15.86
* **Decision Tree:** MAE of 13.80 

With a mean of $12,670.

## Future Work
In my NLP Jupyter Notebook I also noted that I could have improved the LDA Topic Modeling by making it more refined. I could also have benefitted with lemminizing or stemming though I am not sure if it would have made a big difference. 

I had also planned to categorgize the interview questions, but will have to look further into how to do so efficiently. 
