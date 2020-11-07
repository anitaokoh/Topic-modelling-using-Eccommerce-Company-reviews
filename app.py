# import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)

# read image and data to variable and dataframe respectively
img = Image.open("Data/app.png")
data = pd.read_csv('Data/final_data.csv')
data = data[data['Sentiment'].isin(['NEGATIVE','POSITIVE'])]



def get_review_sentiments(topic,status,column):
    """Filter data by topic and status and return the review title, body and review sentiments"""

    topic_filter= data[data['topic']==topic]
    reviewtype_filter = topic_filter[topic_filter[column]==status]
    reviewtype_filter = reviewtype_filter.iloc[:5,:]
    # reviewtype_filter = reviewtype_filter.sample(5)
    body = list(reviewtype_filter['review_body'])
    title = list(reviewtype_filter['review_title'])
    sentiment = list(reviewtype_filter['Sentiment'])
    return title,body,sentiment

def summary_statistics():
    """Calculate the percentage sum of the topics by sentiment category and priority and return an highlighted dataframe"""

    topic = data.groupby('topic')[['topic']].count().rename(columns={'topic':'count'})
    sentiments = data.groupby(['topic','Sentiment'])[['Sentiment']].count().unstack()
    sentiments.columns = sentiments.columns.droplevel()
    priority = data.groupby(['topic','priority'])[['priority']].count().unstack()
    priority.columns = priority.columns.droplevel()
    results = pd.concat([sentiments,priority],axis=1)
    results = results.iloc[:,:].div(topic["count"], axis=0).round(2)
    results = pd.concat([results,topic],axis=1)
    results_design = results.style.highlight_max(axis=0,subset =['NEGATIVE','POSITIVE','High-priority','Low-priority','Moderate-priority'],)
    return results_design



# the controller
def main():
    """Have Customer and company affiliate sections. Partition by sentiments and priority respectively and return review outputs based on choice"""
    
    st.title('Ecommerce Reviews based on Topics')
    st.subheader("Over 600 reviews from three popular ecommerce in Berlin,Germany (Amazon, Zalando and Outfittery) were scraped from TrustPilot,cleaned and underwent into topic themes as well as a sentiment evaluation using AWS services")
    st.image(img,width=600,caption="Visuals")
    if st.checkbox("Start by Clicking"):
        status = st.radio(" Are you using the app as a Customer or a Company Affiliate",("Customer","Company Affiliate"))
        if status == 'Customer':
            st.write('**Welcome Customer**')
            topics = st.selectbox("Which of the topics would you be interested in?",["About Product/Services","Experience/Expectation","Transaction Journey"])
            if st.checkbox('Next'):
               
                status = st.radio("What type of reviews would you like to view?",("POSITIVE", "NEGATIVE"))
               
                st.text('See '+status+ ' Reviews')
                title,body,sentiment = get_review_sentiments(topics,status,'Sentiment')
                for i,j in zip(title,body):
                    st.write('**Review Title:** '+i)
                    st.warning(j)
                    st.write('\n')
                
        if status == 'Company Affiliate':
            st.write('**Welcome Company Afiliate.**')
            st.write('Check out the summary stats of reviews based on their department topics')
            df = summary_statistics()
            st.table(df)
            topics = st.selectbox("Which of the Department would you be interested in?",["About Product/Services","Experience/Expectation","Transactional Journey"])
            if st.checkbox('Check sentiment analytics chart'):
                
                st.text('See the analytics')
                new_data = data[data['topic']==topics]
                data_new = new_data.iloc[:,-2].value_counts()
                st.write(data_new.plot.bar())
                st.pyplot()
			        
                status = st.radio("What type of reviews would you like to view?",("High-priority","Moderate-priority", "Low-priority"))
                    
                st.text('See '+ status)
                    
                title,body,sentiment = get_review_sentiments(topics,status,'priority')
                for i,j,k in zip(title,body,sentiment):
                    st.write('**Review Title:** '+i)
                    st.warning(j)
                    st.text('Sentiment: '+ k)
                    st.write('\n')
                





if __name__ == "__main__":
    main()