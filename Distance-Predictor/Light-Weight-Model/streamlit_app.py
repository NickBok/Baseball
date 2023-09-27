import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="The Distance Predictor", page_icon=":baseball:", initial_sidebar_state="expanded")

st.sidebar.markdown(" ## About")
st.sidebar.markdown("This prediction model forecasts the distance of a batted baseball. The primary aspiration is to contribute meaningful insights to the baseball community."  )  


st.sidebar.markdown(" ## Resources")
st.sidebar.markdown(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pybaseball](https://github.com/jldbc/pybaseball)
""")

st.sidebar.markdown(" ## Refrences")
st.sidebar.markdown(
    """
- [NASA's Hit Simulator](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/whit/#play-ball)
- [Dynamic Hard Hit Rate](https://blogs.fangraphs.com/now-lets-tweak-hard-hit-rate-using-spray-angle/)
""")

st.sidebar.markdown(" ## Info")
st.sidebar.info("Read more about how the model works and see the code on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor).", icon="ℹ️")


st.title("The Distance Predictor")

tab_ppredictor, tab_faq = st.tabs(["The Distance Predictor", "FAQ"])

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


with tab_faq:
            st.markdown(" ### Frequently Asked Questions 🔎 ")

            expand_faq0 = st.expander(":baseball: What are the parameters for the model?")
            with expand_faq0:
                        st.write('''Launch Angle - In baseball, launch angle is the vertical angle at which the ball leaves the player's bat after being struck. It's measured in relation to the ground. A high launch angle means the ball will go further and higher into the air, and a low launch angle means the ball will go lower and not as far.''', unsafe_allow_html=True)
                        st.markdown(1 * "<br />", unsafe_allow_html=True)
                        st.write('''Exit Velocity - The speed, in miles per hour (MPH), at which the ball was launched off the bat after contact.''', unsafe_allow_html=True)
                        st.markdown(1 * "<br />", unsafe_allow_html=True)
                        st.write('''Pull % - In baseball, a "pull" refers to a batted ball hit primarily to the side of the field where the batter stands, based on their batting stance. For example, a right-handed batter hitting towards left field or a left-handed batter hitting towards right field is considered a "pull." This term is significant because it often indicates a powerful hit, but it can also lead to defensive adjustments by the opposing team.''', unsafe_allow_html=True)

            
            expand_faq1 = st.expander(":baseball: Where can I see the code for the model?")
            with expand_faq1:
                        st.write('''It's all on my [Github](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor)!''', unsafe_allow_html=True)


            expand_faq2 = st.expander(":baseball: What machine learning model did you use?")
            with expand_faq2:    
                
                st.write('''I tried various regression models and found that using an XGB regressor as my predictive model gave accurate and meaningful results. An XGBRegressor is a machine learning model that uses the gradient boosting algorithm to predict continuous numerical values. XGBoost stands for eXtreme Gradient Boosting.''')
                st.image('https://github.com/dec1costello/Baseball/assets/79241861/11a4414a-7b01-4f05-9625-90a3de21c752')
            
            expand_faq3 = st.expander(":baseball: How was the predictive model trained?", expanded=False)
            with expand_faq3:
                
                st.write('''To train my model, I collected data from [Pybaseball](https://github.com/jldbc/pybaseball), specifically from the 2022 MLB Season. For this specific Streamlit Model I only used the EV, LA, & Pull% as training features, but feel free to check out my [full model](https://github.com/dec1costello/Baseball/tree/main/Distance-Predictor) where I use more existing features and make my own as well 🧪 👨‍🔬 🧬 !''')

            expand_faq4 = st.expander(":baseball: How can the model improve?", expanded=False)
            with expand_faq4:
                
                st.write('''Adding a batted ball spin rate feature would greatly improve my model. As [Rapsodo points out](https://rapsodo.com/blogs/baseball/understanding-rapsodo-hitting-data-spin-rate/), total spin is an effective way to show hitters how well they are squaring up the ball. Effectively keeping spin rate below 2500 RPMs of backspin guarantees the best chance at success. Here is an example of how spin rate and exit speed interact for a sample player:''')
                st.image('https://cdn.shopify.com/s/files/1/0597/7853/1477/files/image_1_b49cdeac-239a-4295-b355-5dcd46c0c7ab_600x600.png?v=1657207657')


            st.success('''**A Brief Note on Methods:**  

The machine learning model deployed in this app is an XGBoost Regressor that uses Exit Velocity, Launch Angle, and Pull% to predict the distance of a batted ball all scraped from [Pybaseball](https://github.com/jldbc/pybaseball), specifically from the 2022 MLB Season.

[Pybaseball](https://github.com/jldbc/pybaseball) scraped [Baseball Reference](https://www.baseball-reference.com/), [Baseball Savant](https://baseballsavant.mlb.com/), and [FanGraphs](https://www.fangraphs.com/) so I didn't have to 😃!''')
