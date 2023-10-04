import streamlit as st
from gensim.models import KeyedVectors
from gensim.models.word2vec import Word2Vec
import numpy as np
import plotly.express as px
from sklearn.manifold import TSNE
from streamlit.delta_generator import DeltaGenerator

# Initial Configs
st.set_page_config(layout="wide")
st.title("Visualização - Word Embedding") 

# Função tsne_plot com Plotly
def tsne_plot(model: Word2Vec) -> DeltaGenerator:
    """   
        Plots t-SNE.

        Parameters
        ----------
        model : Word2Vec
            Word2Vec model.
        
        Returns
        -------
        st.plotly_chat: DeltaGenerator
            t-SNE plot. 
    
    """ 

    labels = []
    tokens = []

    for word in model.wv.index_to_key:
        tokens.append(model.wv[word])
        labels.append(word)

    tokens = np.array(tokens)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=42)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    data = {
        "x": x,
        "y": y,
        "labels": labels
    }

    fig = px.scatter(data, x="x", y="y", text="labels", title="Visualização t-SNE com Plotly")
    fig.update_traces(textfont=dict(size=15))
    fig.update_layout(width=800, height=800)
    return st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    model = KeyedVectors.load("models/word_embedding.kvmodel")
    # Plots
    tsne_plot(model)