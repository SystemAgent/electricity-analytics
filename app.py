import altair as alt
import pandas as pd
import streamlit as st
from typing import List, Dict
import logging
import json
import time
import requests
import numpy as np
import plotly.express as px

import unittest

# from data import (load_data, clean_and_reshape_data)


def get_data():
    data_countries = pd.read_csv('countries_data.csv')
    data_countries = data_countries.drop(columns=['id', 'oil', 'unknown'], axis=1)
    # bg = data_countries[data_countries['country'] == 'bg']
    # source = data.stocks()
    # source = source[source.date.gt("2004-01-01")]
    return data_countries


def main():
    st.sidebar.header("Settings")

    # GET DATA
    source = get_data()

    # data = load_data()
    # data_unpivoted = clean_and_reshape_data(data)

    # >> DISPLAY WIDGETS <<

    # FILTER TO SELECTED LOCATION & YEAR
    year = st.sidebar.slider('Select year', min_value=2019, max_value=2022, value=2020)
    locations_list = list(source['country'].unique())
    location = st.sidebar.selectbox('Select location', locations_list, index=locations_list.index('bg'))

    data_view = source.loc[
        (source.loc[:, 'country'] == location) & (source.loc[:, 'datetime'] == year)]

    if st.checkbox('Show data', False):
        '''
        ### Data

        _The sample data used in this application is property of Oxford Economics and provided for personal use and_
        _educational purposes only. A 5yr rolling mean transformation has been applied to the original data series values_
        _and so is still representative of actual level values. Please do not redistribute this data without the express_
        _permission of the owner, Oxford Economics._
        '''
        # TABLE
        if st.checkbox('Show DataFrame', True):
            data_view

        if st.checkbox('Show Table'):
            st.table(data_view)

    '''
    ### Chart
    '''
    # chart data is calculated in two steps
    # step 1 (using data_unpivoted, filtered by location)
    chart_data = source[(source['country'] == location)]

    indicators_list = list(chart_data.loc[:, 'wind'].sort_values(ascending=True).unique())
    # this selection box is put into the reserved widget slot created above
    indicator = st.sidebar.selectbox('Select indicator', indicators_list)

    # step 2 (using chart_data, filtered by location's indicators)
    chart_data = chart_data[(chart_data['wind'] == indicator)]

    # fig = alt.Chart(chart_data, title=f'{location} | {indicator}').mark_bar().encode(
    #     alt.X('Year:O', axis=alt.Axis(domain=False, tickSize=0)),
    #     alt.Y('wind', axis=alt.Axis(domain=False, tickSize=0, title='Wind')),
    #     color='wind', tooltip=['Id', 'Datetime', 'Wind']) \
    #     .properties(width=600).interactive()
    # st.altair_chart(fig)

    st.line_chart(source, x='datetime', y=['wind', 'solar'], use_container_width=True)

    # ABOUT
    st.sidebar.header('About')
    st.sidebar.info('Using Streamlit to build a Web App.')
    st.sidebar.markdown('---')

    # Display Readme.md
    if st.sidebar.checkbox('Readme', False):
        st.markdown('---')
        '''
        ### Readme
        '''
        with open('./README.md', 'r', encoding='utf-8') as f:
            readme = f.read()
            st.markdown(readme)


if __name__ == '__main__':
    # >> DISPLAY WIDGETS <<
    # st.image('./images/logo.jpg', output_format='jpg')
    main()

