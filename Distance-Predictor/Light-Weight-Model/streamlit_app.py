import streamlit as st
import pandas as pd
import pickle

st.title('Predicted Distance is...')

df = pd.read_csv('Distance-Predictor/sample_input.csv')

df['launch_angle'].iloc[0] = st.slider("Launch Angle",0,60, value=30)
df['launch_speed'].iloc[0] = st.slider("Exit Velocity",60,120, value=90)
df['pull_percent'].iloc[0] = st.slider("Pull %",0.0,1.0, value = 0.5)

pickled_model = pickle.load(open('Distance-Predictor/lw_model.pkl', 'rb'))
pred = pickled_model.predict(df)

st.title(pred[0])

#once extra folder throw this link in to show under predicting
#https://twitter.com/homerunreport?s=20
