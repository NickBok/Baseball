Feature Engineering:
- Impute missing values
- Add [My Custom Park Factors](https://github.com/dec1costello/Baseball/tree/main/Stadiums)
- [Temp and Humidity](https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859)
- Wind
- Hang time
- Player max la arch
- At bats with contact per person
- HR per player per at bat contact
- Barrel per he per person at bat contact
- Day / Night Game
- Starting pitcher ERA
- [Redo barrel cassifications](https://x.com/JonPgh/status/1706726176973373637?s=20)


[Metrics](https://docs.seldon.io/projects/alibi/en/stable/overview/high_level.html):
- [Huber loss](https://medium.com/analytics-vidhya/a-comprehensive-guide-to-loss-functions-part-1-regression-ff8b847675d6)
- Quantile loss
- Try to use LIME to measure the magnitude of feature attributions of the finla ensemble because its a model agnostic opposed to SHAP
  -  explainer = lime.LimeRegressor(er)
  -  explanation = explainer.explain_instance(X_test[0], voting_regressor.predict)

Auto EDA:
- [IPyWidgets](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6)
- [Ydata-profiling](https://github.com/ydataai)
- [Dtale](https://github.com/man-group/dtale)
- [Sweetviz](https://towardsdatascience.com/sweetviz-automated-eda-in-python-a97e4cabacde)
- [Autoviz](https://towardsdatascience.com/autoviz-automatically-visualize-any-dataset-75876a4eede4)

Not, When using cat feats in SHAP, it kills almost every feature... code that does so when used in part 4 / shap:
feature_cols = ['launch_angle','launch_speed','pfx_x','pfx_z',"release_speed","domed", "spray_angle",'is_barrel','Pop','pull_percent','home_team',"stand","p_throws",'grouped_pitch_type','fav_platoon_split_for_batter']

X = data.loc[:, feature_cols]

# Assuming 'pitch_type' is the categorical feature
categorical_cols = ['home_team',"stand","p_throws",'grouped_pitch_type','fav_platoon_split_for_batter']
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

target_cols = ['hit_distance_sc']
y = data.loc[:, target_cols]

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.95, test_size=0.05, random_state=0)

ter_xg = XGBRegressor(learning_rate=0.1, max_depth=5, min_child_weight=1, subsample=1.0, n_estimators=10).fit(X_train, y_train.values.ravel())

explainer = shap.TreeExplainer(ter_xg, DMatrix=True)

shap_values = explainer(X_valid)

shap.initjs()

