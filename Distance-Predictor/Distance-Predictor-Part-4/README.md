## **Part 4, [Optimization](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Distance-Predictor/Distance-Predictor-Part-4.ipynb) & [SHAP](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Distance-Predictor/Distance-Predictor-Part-SHAP.ipynb)**

In Part 4, for each model in the final ensemble, I optimize hyperparameters with [Optuna](https://optuna.org/) alongside [sklearn](https://scikit-learn.org/stable/modules/grid_search.html) to achieve peak preformance. I then use libs suck as [dtreeviz](https://github.com/parrt/dtreeviz) to vizulise each tree of each model. I finally get the magnitude of feature attributions with [YellowBrick](https://rebeccabilbro.github.io/xgboost-and-yellowbrick/) and [SHap's game theoretic approach](https://shap.readthedocs.io/en/latest/) to identified bias and trends.

# Part 4 TODO (for each model in ensemble) - Model Viz & Metrics & More Models
- [Single XGBoost Decision Tree](https://stackoverflow.com/questions/51323595/plot-a-single-xgboost-decision-tree)
- [DTreeViz](https://github.com/parrt/dtreeviz/blob/master/notebooks/dtreeviz_xgboost_visualisations.ipynb)
- [Part 4 Restructure](https://github.com/ciaran-grant/expected-vaep-model/blob/main/notebooks/process/4_model_evaluation.ipynb)
- [Metrics (this might be a part 5 thing for total ensemble opposed to one model)](https://docs.seldon.io/projects/alibi/en/stable/overview/high_level.html)
- Continue to use [YellowBrick](https://rebeccabilbro.github.io/xgboost-and-yellowbrick/) on more models

- XGB
  - double checking im only uing boolean int and float data tyoes
  - xgb only uses spares matrices for memory
