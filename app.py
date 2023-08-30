import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Time series annotations", page_icon="⬇", layout="centered"
)


def get_data():
    data_countries = pd.read_csv('countries_data.csv')
    data_countries = data_countries.drop(columns=['id', 'oil', 'unknown'], axis=1)
    bg = data_countries[data_countries['country'] == 'bg']
    # source = data.stocks()
    # source = source[source.date.gt("2004-01-01")]
    return bg


source = get_data()
st.line_chart(source, x='datetime', y=['wind', 'solar'], use_container_width=True)

