import streamlit as st

import numpy as np

import pandas as pd

st.title("MyCovergenius ML API Auto Detection")

phrase="This page is generated from Streamlit app for the My Cover api"

phrase

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data
option = st.selectbox(
    'Which number do you like best?',
     chart_data['a'])

'You selected: ', option
option = st.sidebar.selectbox(
    'Which number do you like best?',
     chart_data['b'])

'You selected: ', option

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
