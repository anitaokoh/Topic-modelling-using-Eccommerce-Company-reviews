# Topic modelling using Eccommerce Company reviews

![](https://github.com/anitaokoh/reviews_topics/blob/main/visuals/app.png)

### PROJECT OVERVIEW
**Goal:** Create a review topic app that allows users (customers or Company affiliate) to drill down reviews based on the review sentiments or priority score

**Companies reviews Used:** The three ecommerce company reviews used are **Amazon,Zalando and Outfittery**

**Data Source:** Reviews were scrapped from TrustPilot
### KEY MILESTONE
- Scraped reviews from Trustpilot using Beautifulsoup
- Stored clean data in AWS s3 , read it into AWS comprehend for topic modeling and sentiment analysis and stored it back to S3
- Discovered other python library for obvious spelling correction and expansion of English contractions e.g don’t == do not etc
### ARCHITECTURE
![](https://github.com/anitaokoh/reviews_topics/blob/main/visuals/architecture.png)
### DATA: BEFORE & AFTER Screenshot
![](https://github.com/anitaokoh/reviews_topics/blob/main/visuals/before_after.png)
### DEMO VIDEO
![](https://github.com/anitaokoh/reviews_topics/blob/main/visuals/demo-video.gif)
### TOOLS USED
- Key Python Libraries ( Pandas, Numpy, Matplotlib, re, Streamlit)
- Other Python Libraries (Contractions, SpellCheckers)
- AWS services (AWS S3, AWS Comprehend)
- VS Code
- Jupyter Notebook
- UI APP powered by Streamlit
