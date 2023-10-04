import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initial Configs
st.set_page_config(layout='wide')
st.title('Overall Analysis') 
st.markdown('<p align="justify"> Amount of users predicted to book their next destination to each country for their third, fourth and fifth most likely next destinations.</p>', unsafe_allow_html=True)

def load_data(file):
    data = pd.read_csv(file)

    return data

def overall_analysis(data):
      fig, axes = plt.subplots(3, 1, figsize=(19, 15))
            
      aux1 = data[['User ID', 'Predicted Third Country Destination']].groupby('Predicted Third Country Destination').count().reset_index().rename(columns={'User ID': 'Amount of Users'})
      axes[0] = sns.barplot(ax=axes[0] , x='Predicted Third Country Destination', y='Amount of Users', data=aux1, palette='deep')
      for i in axes[0].containers:
        axes[0].bar_label(i,)

      aux2 = data[['User ID', 'Predicted Fourth Country Destination']].groupby('Predicted Fourth Country Destination').count().reset_index().rename(columns={'User ID': 'Amount of Users'})
      axes[1] = sns.barplot(ax=axes[1], x='Predicted Fourth Country Destination', y='Amount of Users', data=aux2, palette='deep')
      for i in axes[1].containers:
        axes[1].bar_label(i,)

      aux3 = data[['User ID', 'Predicted Fifth Country Destination']].groupby('Predicted Fifth Country Destination').count().reset_index().rename(columns={'User ID': 'Amount of Users'})
      axes[2] = sns.barplot(ax=axes[2], x='Predicted Fifth Country Destination', y='Amount of Users', data=aux3, palette='deep')
      for i in axes[2].containers:
        axes[2].bar_label(i,)

      fig.tight_layout(pad = 7)
      plt.show()

      return fig

if __name__ == "__main__":
    # Load Data
    data = load_data('new_data/final_data_pred.csv')

    # Plots
    st.pyplot(overall_analysis(data))
