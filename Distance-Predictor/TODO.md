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
