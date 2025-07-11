import streamlit as st

st.set_page_config(
    page_title='App', layout="wide"
)
col1, col2, col3 = st.columns(3)

tab1, tab2, tab3 = st.tabs(['cat', 'dog', 'owl'])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    st.video("https://youtu.be/yGpIzHDdq8A")
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with tab3:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/cat.jpg")
