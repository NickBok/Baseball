# Part 2- Feature Engineering Ideas:
- Add [My Custom Park Factors](https://github.com/dec1costello/Baseball/tree/main/Stadiums)
- [Temp and Humidity](https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859)
- Wind
- Player height, weight, throwing arm
- Hang time
- Use plate_x not pfx_x
- [Player max la arch](https://drive.google.com/file/d/1fC974yEShTAJ6PXWgbamLlriaFUzjf1r/view)
- At bats with contact per person
- HR per player per at bat contact
- Barrel per he per person at bat contact
- Day / Night Game
- Starting pitcher ERA
- [Redo barrel cassifications](https://x.com/JonPgh/status/1706726176973373637?s=20)

# Part 3 - Rerun LazyPredict
- Scale as well as one hot encode beforehand

# Part 4 - Model Viz & Metrics & More Models
- [Single XGBoost Decision Tree](https://stackoverflow.com/questions/51323595/plot-a-single-xgboost-decision-tree)
- [DTreeViz](https://github.com/parrt/dtreeviz/blob/master/notebooks/dtreeviz_xgboost_visualisations.ipynb)
- [Part 4 Restructure](https://github.com/ciaran-grant/expected-vaep-model/blob/main/notebooks/process/4_model_evaluation.ipynb)
- [Metrics (this might be a part 5 thing for total ensemble opposed to one model)](https://docs.seldon.io/projects/alibi/en/stable/overview/high_level.html)
- XGB
  - double checking im only uing boolean int and float data tyoes
  - xgb only uses spares matrices for memory

# Part 5 -  [Metrics](https://docs.seldon.io/projects/alibi/en/stable/overview/high_level.html) & Redo DFs
- Add top 8 Models to Ensemble
- [Sample Table](https://karbartolome.quarto.pub/the-grammar-of-tables/)
- [Plottable](https://github.com/znstrider/plottable)
- [Plottable Docs](https://plottable.readthedocs.io/en/latest/)
- [Add CatBoostRegressor()](https://towardsdatascience.com/catboost-regression-in-6-minutes-3487f3e5b329)
- [Huber loss](https://medium.com/analytics-vidhya/a-comprehensive-guide-to-loss-functions-part-1-regression-ff8b847675d6)
- Quantile loss

# Random
- [Rapids](https://rapids.ai/)
- [YellowBrick](https://rebeccabilbro.github.io/xgboost-and-yellowbrick/)
- [Add more partial dependence plots](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_partial_dependence_visualization_api.html#sphx-glr-auto-examples-miscellaneous-plot-partial-dependence-visualization-api-py)
- Add event location plot to readme
- Compare to https://www.omnicalculator.com/physics/projectile-motion
- Fix all vars to mean and plot ev on x axis, launch angle on y axis, and color for distance
