import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="The Distance Predictor", page_icon=":baseball:", initial_sidebar_state="expanded")

st.sidebar.markdown(" ## About")
st.sidebar.markdown("This prediction model forecasts the distance of batted ball in the MLB. The primary aspiration is to contribute meaningful insights to the baseball community."  )  


st.sidebar.markdown(" ## Resources")
st.sidebar.markdown(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pybaseball](https://github.com/jldbc/pybaseball)
""")

st.sidebar.markdown(" ## Info")
st.sidebar.info("Read more about how the model works and see the code on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor).", icon="ℹ️")


st.title("The Distance Predictor")

tab_ppredictor, tab_explore, tab_faq = st.tabs(["The Distance Predictor", "Explore", "FAQ"])
#tab for model data like feature importance
#tab for ev percentiles by la, and a df a side by side for ev percentiles vs pull

with tab_ppredictor:

            df = pd.read_csv('Distance-Predictor/Light-Weight-Model/sample_input.csv')
            df['launch_angle'].iloc[0] = st.slider(" ## Launch Angle",0,60, value=30)
            df['launch_speed'].iloc[0] = st.slider(" ## Exit Velocity",60,120, value=90)
            df['pull_percent'].iloc[0] = st.slider(" ## Pull %",0.0,1.0, value = 0.5)
            
            pickled_model = pickle.load(open('Distance-Predictor/Light-Weight-Model/lw_model.pkl', 'rb'))
            pred = pickled_model.predict(df)

            res = pred[0]
            end = ' Foot :bomb:'
            final = (str(res) + end)
    
            st.title(final)

with tab_explore:
            st.markdown(" ### Data Trends")

with tab_faq:
            st.markdown(" ### Frequently Asked Questions 🔎 ")
            
            expand_faq1 = st.expander(":baseball: Where can I see the code for the model?")
            with expand_faq1:
                        st.write('''It's all on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor)!''', unsafe_allow_html=True)


            expand_faq2 = st.expander(":baseball: What machine learning model did you use?")
            with expand_faq2:    
                
                st.write('''I tried various regression models and found that using an XGB regressor as my predictive model gave accurate and meaningful results. An XGBRegressor is a machine learning model that uses the gradient boosting algorithm to predict continuous numerical values. XGBoost stands for eXtreme Gradient Boosting and is very precise.''')
                st.image('https://github.com/dec1costello/Baseball/assets/79241861/11a4414a-7b01-4f05-9625-90a3de21c752')
            
            expand_faq3 = st.expander(":baseball: How was the predictive model trained?", expanded=False)
            with expand_faq3:
                
                st.write('''To train my model, I collected data from [Pybaseball](https://github.com/jldbc/pybaseball), specifically from the 2022 MLB Season. For this specific Streamlit Model I only used the EV, LA, & Pull% as training features, but feel free to check out my [full model](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor) where I use more existing features and make my own as well 🧪 👨‍🔬 🧬!''')

            expand_faq4 = st.expander(":baseball: How can the model imporve?", expanded=False)
            with expand_faq4:
                
                st.write('''Adding a batted ball spin rate feature woud greatly improve my model. As [Rapsodo points out](https://rapsodo.com/blogs/baseball/understanding-rapsodo-hitting-data-spin-rate/), miss hits create more spin, while flush hit balls have low spin rates. ''')
                st.image('https://github.com/dec1costello/Baseball/assets/79241861/8dfe2da6-0d54-4ad8-b6e6-236605e93ef7')


            st.success('''**A Brief Note on Methods:**  

The machine learning model deployed in this app is an XGBoost Regressor that uses Exit Velocity, Launch Angle, and Pull% to predict the distance of a batted ball all scraped from [Pybaseball](https://github.com/jldbc/pybaseball), specifically from the 2022 MLB Season.

[Pybaseball](https://github.com/jldbc/pybaseball) scraped [Baseball Reference](https://www.baseball-reference.com/), [Baseball Savant](https://baseballsavant.mlb.com/), and [FanGraphs](https://www.fangraphs.com/) so I didn't have to 😃!''')
