import streamlit as st
from utils import logo_display

# Initial Configs
st.set_page_config(
    page_title='Word Embedding App',
    page_icon=':chart_with_upwards_trend:', 
    layout='wide')

# Título centralizado
st.markdown('<h1 align="center">Word Embedding App</h1>', unsafe_allow_html=True)

# Texto "Dadosfera" centralizado
st.markdown('<h2 align="center">Dadosfera</h2>', unsafe_allow_html=True)

if __name__ == "__main__":    
    logo_display("pic/logo.png")
    st.markdown('- #### Olá, aqui você irá encontrar uma visualização com t-SNE de um embedding das palavras (tokens) mais comuns utilizadas no título e descrição dos produtos do dataset spacemanidol/product-search-corpus, disponível no site Hugging Face.')
    st.markdown('#')

    st.markdown('- ##### A segunda página, nomeada Visualization, mostra essa visualização.')
    st.markdown('#')

    st.markdown('- ##### Feito por: Bruno Di Franco Albuquerque')
    st.markdown('#')

