import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid
import pandas as pd

# Initial Configs
st.set_page_config(layout='wide')
st.title('Predictions Display') 
st.markdown('<p align="justify"> This page shows the new users data alongside their predictions, from the most likely country of their next booking to the least. For instance, the column Predicted First Country Destination indicates the most likely country for each user to book their next destination, while Predicted Second Country Destination is the second most likely country according to our model, and so on, up until the fifth predicted country. Feel free to use the filters by clicking on the three stripes next to each column. </p>', unsafe_allow_html=True) 

def load_data(file):
    data = pd.read_csv(file)

    return data

def show_data(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) # Paging
    gb.configure_selection('multiple', groupSelectsChildren='Group checkbox select children') 
    gb.configure_default_column(wrapHeaderText=True, autoHeaderHeight=True)

    gb.configure_column('Predicted First Country Destination', cellStyle={'color' : 'black', 'font-weight' : 'bold'})
    gb.configure_column('Predicted Second Country Destination', cellStyle={'color' : 'black', 'font-weight' : 'bold'})
    gb.configure_column('Predicted Third Country Destination', cellStyle={'color' : 'black', 'font-weight' : 'bold'})
    gb.configure_column('Predicted Fourth Country Destination', cellStyle={'color' : 'black', 'font-weight' : 'bold'})
    gb.configure_column('Predicted Fifth Country Destination', cellStyle={'color' : 'black', 'font-weight' : 'bold'})
    
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=True,   
        height=600, 
        width='100%',
        reload_data=False
    )
    return grid_response

def show_countries_labels():
    if st.checkbox('Show Countries Labels'):
        st.markdown("""
        |      **Column**      |                   **Definition**              |
        |:--------------------:|-----------------------------------------------|
        |         US           |                    United States              |
        |         FR           |                    France                     | 
        |         CA           |                    Canada                     |
        |         GB           |                    Great Britain              |
        |         ES           |                    Spain                      |
        |         IT           |                    Italy                      |
        |         PT           |                    Portugal                   |
        |         NL           |                    New Zealand                |
        |         DE           |                    Germany                    |
        |         AU           |                    Australia                  |
        |         NDF          | No destination found (there wasn't a booking) |
        |         other        |                    Other countries            |
        """)
        return None

if __name__ == "__main__":
    # Load Data
    data = load_data('new_data/final_data_pred.csv')

    # Display Data
    show_data(data)

    # Country Labels
    show_countries_labels()


    