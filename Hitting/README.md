# **Distance Predictor**
Author: Declan Costello

## **Overview**

Using [Pybaseball Data](https://github.com/jldbc/pybaseball) from the 2022 MLB Season, I predict how far a batted ball will travel. I hope to provide value to the baseball community by combining my interests of hitting and weather. First I explore given feature trends in the data set, followed my creating my own. After selecting XGBost as the best model, I investiage the chosen parameters to see which ones have the best return on investments, Finalling I put the pipeline together and display the results. I encourage you to view [Parts 3-5 on NBViewer](https://nbviewer.org/github/dec1costello/Baseball/tree/main/Hitting/) as [Bokeh](http://bokeh.org/) does not render on Github.

## **Table of Context**

0. [Link to CSV]()
1. [Part 1, Data Exploration](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb)
2. [Part 2, Feature Engineering](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-2.ipynb)
3. [Part 3, Model Selection](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-3.ipynb)
4. [Part 4, Model ROI](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-4.ipynb)
5. [Part 5, Final Pipeline](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-5.ipynb)
6. [Part 6, Compare to NASA](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/whit/#play-ball)

TODO:

- Impute
- Add in Weights
- Add Humidor Stadiums, humidity, and [temp](http://baseball.physics.illinois.edu/HRProbTemp.pdf) during games
- Add in VAA vs LA, agg Dis
- Add in HAA vs Spray, agg Dis
- Consider using [pitch counts](https://blogs.fangraphs.com/hitters-are-losing-more-long-plate-appearances/)
- [Compare to NASA](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/whit/#play-ball)

FUTURE:

- Use to predict [WAR](https://blogs.fangraphs.com/an-iota-of-xwoba-does-overperformance-improve-confidence/)
