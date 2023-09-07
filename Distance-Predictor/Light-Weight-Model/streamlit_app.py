import streamlit as st
import pandas as pd
import pickle

st.sidebar.markdown(" ## About The Distance Predictor")
st.sidebar.markdown("This prediction model forecast the distance of batted ball distances. With an interest in hitting mechanics and atmospheric influences, the primary aspiration is to contribute meaningful insights to the baseball community."  )              
st.sidebar.info("Read more about how the model works and see the code on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor).", icon="ℹ️")


st.title("Distance Predictor")
st.markdown('''##### <span style="color:gray">Predict the distance of a batted ball from EV, LA, & Pull%</span>
            ''', unsafe_allow_html=True)

tab_ppredictor, tab_faq = st.tabs(["The Distance Predictor", "FAQ"])

with tab_ppredictor:

            st.markdown('''#### Predicted Distance is...''', unsafe_allow_html=True)

            df = pd.read_csv('Distance-Predictor/Light-Weight-Model/sample_input.csv')
            
            df['launch_angle'].iloc[0] = st.slider("Launch Angle",0,60, value=30)
            df['launch_speed'].iloc[0] = st.slider("Exit Velocity",60,120, value=90)
            df['pull_percent'].iloc[0] = st.slider("Pull %",0.0,1.0, value = 0.5)
            
            pickled_model = pickle.load(open('Distance-Predictor/Light-Weight-Model/lw_model.pkl', 'rb'))
            pred = pickled_model.predict(df)
            
            st.title(pred[0])


with tab_faq:
            st.title('test')
