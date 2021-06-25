import streamlit as st
import numpy as np
import pandas as pd
import time
st.title("My first app")

st.write("He's our first attempt at using data to create a table: ")
# st.write(pd.DataFrame({'First column':[1,2,3,4], 'Second column': [10,20,30,40]}))
st.table(pd.DataFrame({'First column':[1,2,3,4], 'Second column': [10,20,30,40]}))
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)



map_data = pd.DataFrame(
    np.random.randn(1000,2),
    columns=['lat', 'lon']
)
st.map(map_data)

if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data


df = pd.DataFrame({
    'First column': [1,2,3,4],
    'Second column': [10,20,30,40]
})
st.write(df.head())

option = st.selectbox('Which number', df['First column'])
st.write('You selected: ', option)

#
option = st.sidebar.selectbox(
    'Which number do you best?',
    df['First column']
)


# st.sidebar.markdown()
#
# st.sidebar.slider()
#
# st.sidebar.line_chart()


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("You have pressed")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

"Starting a long computation...."
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    time.sleep(0.1)
"And now we're done"