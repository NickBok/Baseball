import streamlit as st
import pandas as pd
import pickle
import numpy as np


st.title('Predicted Distance is...')

la = st.slider("Launch Angle",0,50, value=25)
ev = st.slider("Exit Velocity",0,120, value=60)
pull_percent =  st.slider("Pull %",0.0,1.0, value = 0.5)

df = pd.read_csv('Distance-Predictor/sample_input.csv')

df['launch_angle'].iloc[0] = la
df['launch_speed'].iloc[0] = ev
df['pull_percent'].iloc[0] = pull_percent

pickled_model = pickle.load(open('light_weight_model.pkl', 'rb'))
pred = pickled_model.predict(df)

st.title(pred[0])
