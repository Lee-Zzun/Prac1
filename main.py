# main.py

import streamlit as st
from data_loader import load_data

def main():
    st.title('This is Dashboard')

    df = load_data()

    st.write(df)
    
if __name__ == '__main__':
    main()
