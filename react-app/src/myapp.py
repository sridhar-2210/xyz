import streamlit as st

# Custom CSS to style the Streamlit app
st.markdown("""
    <style>
    .main {
        background-color: #0E0F1C;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #0E0F1C;
    }
    input {
        background-color: #1A1B2A;
        color: white;
    }
    .css-1d391kg {
        background-color: #1A1B2A;
        color: white;
    }
    .css-1avcm0n {
        background-color: #1A1B2A;
        color: white;
    }
    .stTextArea textarea {
        background-color: #1A1B2A;
        color: white;
    }
    .stButton button {
        background-color: #5E72E4;
        color: white;
    }
    .css-1a32fsj.e1fqkh3o3 {
        background-color: #1A1B2A;
        color: white;
    }
    .css-1okebmr {
        background-color: #0E0F1C;
    }
    </style>
""", unsafe_allow_html=True)

# Title and input prompt
st.title('New Story')
prompt = st.text_area('Enter your prompt here...')

st.sidebar.title('AI Model')
model = st.sidebar.selectbox('Choose Model', ['Clio', 'Euterpe', 'Krake'])
st.sidebar.markdown('### Memory')
st.sidebar.text_area('Memory input...')
st.sidebar.markdown('### Author’s Note')
st.sidebar.text_area('Author’s Note...')
st.sidebar.markdown('### Lorebook Quick Access')
st.sidebar.text_input('Search for an entry...')

# Sidebar options
if st.sidebar.checkbox('View Story Stats'):
    st.sidebar.write("Story stats would go here.")

st.sidebar.markdown('### Export Story')
if st.sidebar.button('Export'):
    st.sidebar.write('Export functionality would go here.')

# Main area for story text and interaction
st.write("Your story will appear here based on the entered prompt.")