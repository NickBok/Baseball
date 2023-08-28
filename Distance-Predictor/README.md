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

<tbody>
  <tr>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/a2c62f05-3ecc-4c4e-891f-9a772f2cdfd7" />
      </a>
    </td>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-1.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/68cceac6-174b-4f7e-80e7-d5669d55f849" alt="WOBA Heatmap" />
      </a>
    </td>
</tr>
</tbody>
</table>

## **Part 2 Description**

In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball



<table>

<tbody>
  <tr>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-2.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/b7cee43a-5197-412e-abdb-2f5502605b96" alt="Event Scatter" />
      </a>
    </td>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-2.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/4e07ccec-4cec-42c5-92c1-1d602053b812" alt="WOBA Heatmap" />
      </a>
    </td>
</tr>
</tbody>
</table>

## **Part 3 Description**

In Part 3, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball In Part 2, I create features based off the given data such as Dynamic Hard Hit rate and obsere trends fearues within Pybaseball



<table>

<tbody>
  <tr>
    <td>
      <a href="https://nbviewer.org/github/dec1costello/Baseball/blob/main/Hitting/Distance-Predictor-Part-2.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/11a4414a-7b01-4f05-9625-90a3de21c752" alt="Event Scatter" />
      </a>
    </td>
</tr>
</tbody>
</table>



## **Part 5**

<table>

  <tr>
    <td>residus</td>
    <td>a vs p</td>
  </tr>
    <tr>
    <th 
colspan="2"
>Feature importance h bar</th>
  </tr>
</table>

## **Task List (TODO)**

- Impute missing values
- Incorporate weighting factors
- Integrate Humidor Stadium data, humidity, and [temperature](http://baseball.physics.illinois.edu/HRProbTemp.pdf) during games
- pitch location vs la for top bottom, and spray vs side side pitch locations
- Consider utilization of [pitch counts](https://blogs.fangraphs.com/hitters-are-losing-more-long-plate-appearances/)
- Conduct a Comparative Analysis with NASA's insights: [Comparison Link](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/whit/#play-ball)

## **Future Prospects**

A potential avenue for expansion lies in the utilization of the model to predict [WAR](https://blogs.fangraphs.com/an-iota-of-xwoba-does-overperformance-improve-confidence/), thereby delving deeper into the predictive dimensions of player performance.
