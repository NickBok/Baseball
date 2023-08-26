# **Distance Predictor**
*Author: Declan Costello*

## **Project Overview**

Welcome to the **Distance Predictor**. This Project harnesses data from the [Pybaseball Data](https://github.com/jldbc/pybaseball) repository, specifically from the 2022 MLB Season, to forecast the trajectory of batted ball distances. With an interest in hitting mechanics and atmospheric influences, the primary aspiration is to contribute meaningful insights to the baseball community. To get a better feel for the visual details, I encourage you to check out the interactive visuals created using [Bokeh](http://bokeh.org/) for [Parts 3-5 on NBViewer](https://nbviewer.org/github/dec1costello/Baseball/tree/main/Hitting/).

## **Data Source**

Provided here is a hyperlink to access the processed [CSV dataset](https://drive.google.com/file/d/1tnhLBWTBbbo917c8f9LYwdVHwd-gr5bU/view?usp=sharing) needed for parts 3 through 5. This hyperlink is a much quicker alternative compared to waiting an hour for [Pybaseball's](https://github.com/jldbc/pybaseball) download and it only includes the most important information needed.

## **Table of Contents**

1. [Part 1, Data Exploration](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb)
2. [Part 2, Feature Engineering](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-2.ipynb)
3. [Part 3, Model Selection: XGBoost](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-3.ipynb)
4. [Part 4, XGBoost Parameter Optimization and Insights](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-4.ipynb)
5. [Part 5, Pipeline Synthesis and Results Showcase](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-5.ipynb)


## **Part 1 Description**

In Part 1, I explore the given fearues within Pybaseball

<table>
<thead>
  <tr>
    <th>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">CORR Heatmap</a>
    </th>
    <th>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">WOBA Heatmap</a>
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/666c6e90-9e3c-4937-b819-69e2da06b361" alt="CORR Heatmap" />
      </a>
    </td>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/beb0e425-99f4-4cfb-8eb1-178178025951" alt="WOBA Heatmap" />
      </a>
    </td>
</tr>
</tbody>
</table>

## **Task List (TODO)**

- Impute missing values
- Incorporate weighting factors
- Integrate Humidor Stadium data, humidity, and [temperature](http://baseball.physics.illinois.edu/HRProbTemp.pdf) during games
- Integrate Variables At-bat vs. Launch Angle, aggregated distance
- Incorporate Hit Angle at-bat vs. Spray Angle, aggregated distance
- Consider utilization of [pitch counts](https://blogs.fangraphs.com/hitters-are-losing-more-long-plate-appearances/)
- Conduct a Comparative Analysis with NASA's insights: [Comparison Link](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/whit/#play-ball)

## **Future Prospects**

A potential avenue for expansion lies in the utilization of the model to predict [WAR](https://blogs.fangraphs.com/an-iota-of-xwoba-does-overperformance-improve-confidence/), thereby delving deeper into the predictive dimensions of player performance.
