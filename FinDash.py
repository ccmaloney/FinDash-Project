
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("Cavins Investment Research")
#st.image('./cir_logo_new.png')
# Insert containers separated into tabs:

# You can always call this function where ever you want

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = 
    #logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path="./logo.png", width=300, height=250)
st.sidebar.image(my_logo)

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])

ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")



#from alpha_vantage.fundanentaldata import FundamentalData
#with fundamental_data:
#    key = "TBIRD3CKGGEFJCVQ"
#    fd = FundamentalData(key, output_format = 'pandas')

