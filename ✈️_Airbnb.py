# Imports
import os
import pandas as pd
import streamlit as st

# Initial Configs
st.set_page_config(
    page_title='Airbnb App',
    page_icon=':airplane:', 
    layout='wide')

st.markdown('<h1 align="center">Airbnb Destinations Predictions</h1>', unsafe_allow_html=True) 

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('pic/logo.png', width=500)

with col3:
    st.write(' ')

st.markdown('- #### Welcome, here you will find the five most likely countries predictions for an Airbnb user to book their next destination.')
st.markdown('#')

st.markdown('- ##### The Predictions Display page shows the new users data alongside their predictions, from the most likely country of their next booking to the least likely.')
st.markdown('#')

st.markdown('- ##### In the third, fourth and fifth pages you will find a general, age and gender analysis, respectively.')
st.markdown('##')

st.markdown('<i> General, age and gender analysis are done using only the third, fourth and fifth most likely country destinations, since the first and second most likely countries predictions are mostly USA and NDF (no destination found). </i>', unsafe_allow_html=True)
st.markdown('<i> It should take around a couple of minutes for the app to load completely. </i>', unsafe_allow_html=True)

st.cache(allow_output_mutation=True, hash_funcs={sqlalchemy.engine.base.Engine: id})
def get_data(conn_url):
    # conn
    conn_url = conn_url
    engine = sqlalchemy.create_engine(conn_url)

    query = """
    SELECT * FROM data_pred;
    """
    final_data_pred = pd.read_sql(query, con=engine)

    return final_data_pred

def final_adjustments(data):
    # Renaming columns
    data.columns = ['User ID',
                    'Date Account Created',
                    'Date First Active',
                    'Gender',
                    'Age', 
                    'Signup Method',
                    'Signup Flow',
                    'Language',
                    'Affiliate Channel',
                    'Affiliate Provider',
                    'First Affiliate Tracked', 
                    'Signup App',
                    'First Device Type',
                    'First Browser',
                    'Predicted First Country Destination',
                    'Predicted Second Country Destination',
                    'Predicted Third Country Destination', 
                    'Predicted Fourth Country Destination', 
                    'Predicted Fifth Country Destination']

    # Rearranging columns
    data = data[['User ID',
                 'Predicted First Country Destination',
                 'Predicted Second Country Destination',
                 'Predicted Third Country Destination', 
                 'Predicted Fourth Country Destination', 
                 'Predicted Fifth Country Destination',
                 'Date Account Created',
                 'Date First Active',
                 'Gender',
                 'Age', 
                 'Signup Method',
                 'Signup Flow',
                 'Language',
                 'Affiliate Channel',
                 'Affiliate Provider',
                 'First Affiliate Tracked', 
                 'Signup App',
                 'First Device Type',
                 'First Browser']]
    return data

if __name__ == "__main__":
    # Loading Credentials
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DATABASE = os.getenv('DATABASE')

    conn_url = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    # Get Data
    final_data_pred = get_data(conn_url)

    # Final Adjustments
    final_data_pred = final_adjustments(final_data_pred)

    # Saving
    final_data_pred.to_csv('new_data/final_data_pred.csv', index=False) # saving to csv so it can be used for pages 2, 3, 4 and 5.



# from gensim.models import KeyedVectors
# kv2 = KeyedVectors.load("models/word_embedding.kvmodel")