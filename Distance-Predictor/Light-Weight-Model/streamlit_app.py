import streamlit as st
import pandas as pd
import pickle

st.sidebar.markdown(" ## About The Distance Predictor")
st.sidebar.markdown("This prediction model forecast the distance of batted ball distances. With an interest in hitting mechanics and atmospheric influences, the primary aspiration is to contribute meaningful insights to the baseball community."  )              
st.sidebar.info("Read more about how the model works and see the code on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor).", icon="ℹ️")


st.title("The Distance Predictor")
st.markdown('''##### <span style="color:gray">Predict the distance of a batted ball from EV, LA, & Pull%</span>
            ''', unsafe_allow_html=True)

tab_ppredictor, tab_faq = st.tabs(["The Distance Predictor", "FAQ"])
#tab for model data like feature importance
#tab for ev percentiles by la, and a df a side by side for ev percentiles vs pull

with tab_ppredictor:

            st.markdown('''#### The Predicted Distance is...''', unsafe_allow_html=True)

            df = pd.read_csv('Distance-Predictor/Light-Weight-Model/sample_input.csv')
            
            df['launch_angle'].iloc[0] = st.slider("Launch Angle",0,60, value=30)
            df['launch_speed'].iloc[0] = st.slider("Exit Velocity",60,120, value=90)
            df['pull_percent'].iloc[0] = st.slider("Pull %",0.0,1.0, value = 0.5)
            
            pickled_model = pickle.load(open('Distance-Predictor/Light-Weight-Model/lw_model.pkl', 'rb'))
            pred = pickled_model.predict(df)
            
            st.title(pred[0])


            st.success('''**A Brief Note on Methods:**  

The machine learning model deployed in this app is an XGBoost Regressor that uses exit velocity, launch angle, and pull to predict the distance of a batted ball all scraped from [Pybaseball Data](https://github.com/jldbc/pybaseball).''')


with tab_faq:
            st.markdown(" ### Frequently Asked Questions 🔎 ")
            
            expand_faq1 = st.expander(":baseball: Where can I see the code for the model?")
            with expand_faq1:
                        st.write('''It's all on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor). ''', unsafe_allow_html=True)

            st.success('''**A Brief Note on Methods:**  

The machine learning model deployed in this app is an XGBoost Regressor that uses exit velocity, launch angle, and pull to predict the distance of a batted ball all scraped from [Pybaseball Data](https://github.com/jldbc/pybaseball).''')


