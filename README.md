# Project Posture

Project Posture is a project for COSC 490 Senior Capstone from Pepperdine University taught by Professor [Fabien Scalzo](http://web.cs.ucla.edu/~fab/) and co-advised by Professor [Adam Pennell](https://seaver.pepperdine.edu/academics/faculty/adam-pennell/) based on Python language development. Its purpose is to investigate for linear and/or non-linear associations between various posturography and self-reported physical activity metrics using data analytics, machine learning, and/or related techniques/processes. 

[![license](https://img.shields.io/github/license/chengmeowz/project-posture.svg)](https://github.com/chengmeowz/project-posture/blob/main/LICENSE)
![author](https://img.shields.io/badge/Author-Cheng&Sunny-blue.svg)

**Reference**

The data for this project is from 
* Santos, D. & Duarte, M. (2016). [*A public data set of human balance evaluations*](https://peerj.com/articles/2648/). PeerJ, 4, e2648. doi: 10.7717/peerj.2648.

The calculation for variables is based on 
* Duarte M, Freitas SM. [*Revision of posturography based on force plate for balance evaluation*](http://www.scielo.br/pdf/rbfis/v14n3/en_03.pdf). Rev Bras Fisioter. 2010;14(3):183-192.
* Duarte M. Comments on [*"Ellipse area calculations and their applicability in posturography"*](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.659.1973&rep=rep1&type=pdf) (Schubert and Kirchner, vol.39, pages 518-522, 2014). Gait Posture. 2015;41(1):44-45. doi:10.1016/j.gaitpost.2014.08.008
* Yamamoto T, Smith CE, Suzuki Y, Kiyono K, Tanahashi T, Sakoda S, Morasso P, Nomura T. [*Universal and individual characteristics of postural sway during quiet standing in healthy young adults*](https://pubmed.ncbi.nlm.nih.gov/25780094/). Physiol Rep. 2015 Mar;3(3):e12329. doi: 10.14814/phy2.12329. PMID: 25780094; PMCID: PMC4393163.

## Table of Contents

- [Progress](#progress)
   	- [Step 1: Discrete Variable Calculations](#step_1)
   	- [Step 2: Exploratory Analysis/Machine Learning](#step_2)
- [Install](#install)
- [Maintainers/Developers](#maintainers_developers)
- [Contributing](#contributing)
- [License](#license)

## Progress

### Step_1
**Discrete Variable Calculations** (accomplished by Dr. Watanabe)

- [X] Calculate the variables using numpy, pandas, matplotlib.pyplot, zipfile, and welch from scipy.signal in Python.

![Image text](https://raw.githubusercontent.com/chengmeowz/project-posture/main/extra/variables_calculation.jpg)

[*copMeasures.ipynb*](https://colab.research.google.com/drive/1oOHwtgAxazdcARhygBb5DLKYAf-HDTT8?usp=sharing#scrollTo=8MrFIHv6OpQu), a Jupyter Notebook file in Python using Google Colab for the variables calculation.

### Step_2
**Exploratory Analysis/Machine Learning**

* 【Overall Goal】<br/>
   * Predict MVPA_minutes.week and IPAQ_Category from any of the four Total Area (cm²) average scores (i.e., EO/firm; EO/foam; EC/firm; EC/foam) as well as AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity.
   * Predict Total Area (cm²) from MVPA_minutes.week and IPAQ_Category as well as AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity.
* 【Used Algorithms】[*Reference*](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
   1. [Ridge regression](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification)
   2. [Kernel ridge regression](https://scikit-learn.org/stable/modules/kernel_ridge.html)
   3. [Adaboost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost)
   4. [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)
   5. [Neural network](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression)
   6. [Support vector machine](https://scikit-learn.org/stable/modules/svm.html#regression)


----------
**Pre-work** (accomplished by Sunny)

- [X] Average the 3 trials for each condition to get an overall average score for MVPA_minutes.week, IPAQ_Category, Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s), i.e., we will have 4 average Total Area (cm²) scores.

* [variables.py](https://github.com/chengmeowz/project-posture/blob/main/code/variables.py), a Python file to average the 3 trials for each condition to get an overall average score.

* [variables.xlsx](https://github.com/chengmeowz/project-posture/blob/main/BDS/variables.xlsx), an excel file contains an overall average score for Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), Total Velocity (cm/s), MVPA_minutes.week, IPAQ_Category, Subject, Vision, and Surface for each condition.

- [X] Decide X and Y. 
   - We set Y as MVPA_minutes.week and X as the other five variables first, and 
   - do it again with Y as Total Area (cm²) and X as the other five variables.
   - Then we set Y as IPAQ_Category and X as *the other five variables first*, and 
   - do it again with Y as Total Area (cm²) and X as *the other five variables*.


----------
**Data Preprocessing** (accomplished by Sunny)

- [X] Apply [pre-processing](https://scikit-learn.org/stable/modules/preprocessing.html) to the data (Standardization)
[*Reference*](https://towardsdatascience.com/data-preprocessing-in-python-b52b652e37d5)
   - We implemented both [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler) and [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler).

* [preprocessing_standard.py](https://github.com/chengmeowz/project-posture/blob/main/code/preprocessing_standard.py), a Python file to preprocess data using StandardScaler.

* [preprocessing_minMax.py](https://github.com/chengmeowz/project-posture/blob/main/code/preprocessing_minMax.py), a Python file to preprocess data using MinMaxScaler.

* [standardScaler.xlsx](https://github.com/chengmeowz/project-posture/blob/main/standardScaler/standardScaler.xlsx), an excel file contains the preprocessed data using StandardScaler for MVPA_minutes.week, Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s)).

* [minMaxScaler.xlsx](https://github.com/chengmeowz/project-posture/blob/main/minMaxScaler/minMaxScaler.xlsx), an excel file contains the preprocessed data using MinMaxScaler for MVPA_minutes.week, Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s)).

----------
**Learning** (accomplished by Cheng)

- [X] Machine learning algorithms to evaluate. 
   - Pick one column as the test data and rest columns as the training data, then use the training data to create one model in【Used Algorithms】and put the result into an excel

- [X] Use [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html): 10-Fold.

- [X] For each machine learning algorithms, perform an [optimization](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#sphx-glr-auto-examples-miscellaneous-plot-kernel-ridge-regression-py) of the parameters. 
   - We implemented [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV) with [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold) (specifically 10-Fold).
```diff
Example for Kernel ridge regression using gridsearch to optimize the parameters alpha and gamma:
   kr = GridSearchCV(KernelRidge(kernel='rbf', gamma=0.1),
                     param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                                "gamma": np.logspace(-2, 2, 5)})
```

----------
**Evaluation** (accomplished by Cheng & Sunny)

- [X] Perform the [evaluation using a metric for regression](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
   - We used our model to find y_true and y_pred to draw the graph for a more visualized result, comparing the result from the predicted y value using our six models with the original data.
   - We also implemented the scoring methods (built in GridSearchCV for regression) below to interpret our models: 
```diff
      metrics.mean_absolute_error (i.e. scoring='neg_mean_absolute_error')
      metrics.mean_squared_error (i.e. scoring='neg_mean_squared_error')
      metrics.r2_score (i.e. scoring=‘r2’)
```

----------
* [learning.ipynb](https://github.com/chengmeowz/project-posture/blob/main/code/learning.ipynb), a Jupyter Notebook file in Python to do the learning and evaluation part.

----------
* [original](https://github.com/chengmeowz/project-posture/blob/main/original), a folder for storing the scatterplots of original data to compare X and y.
* [standardScaler](https://github.com/chengmeowz/project-posture/blob/main/standardScaler), a folder for storing the scatterplots when preprocessing uses StandardScaler. 
* [minMaxScaler](https://github.com/chengmeowz/project-posture/blob/main/minMaxScaler), a folder for storing the scatterplots when preprocessing uses MinMaxScaler.
   * For both folders, the explanation of folders inside them is: 
```diff
      x_MVPA_y_totalArea: a folder for storing the scatterplots when y is Total Area and X is MVPA.
      x_totalArea_y_MVPA: a folder for storing the scatterplots when y is MVPA and X is Total Area.
      y_MVPA: a folder for storing the scatterplots when y is MVPA and X is the other five variables.
      y_totalArea: a folder for storing the scatterplots when y is totalArea and X is the other five variables.
```

----------
* Additional Documents:
   * [COSC 490_Project Posture Document](https://docs.google.com/document/d/1V-mI-3vDQ6-GY3iUvb9CrLeeRYSuZqQdGyy8Qzy82oA/edit#), a google doc of things related to our project in full version.
   * [COSC 490_Project Posture](https://docs.google.com/presentation/d/1cfuVeE14G9vV4S8qKKgroqwdNNoAP2vRqOGpF-i5RBg/edit#slide=id.gd62683932d_6_79), a google slide for Capstone Project presentation.
   * [project_document](https://docs.google.com/document/d/10KtgQHE-h6mvhIXldY2FiXEathW0SQT0a4IE7J_cbfc/edit#), a google doc (some in Chinese) contains our temporary schedule, links when we share w/ each other for new information, steps, etc.
   * [Posturography project](https://docs.google.com/document/d/187VSRm5dXfQdjyiPVOmLSTtaU2VaujCz8QU5Zh54fZw/edit?ts=606652d3), a google doc w/ instructions from Professor Scalzo.
   * [learning_1st_ver](https://github.com/chengmeowz/project-posture/blob/main/code/learning_1st_ver), a folder contains six Jupyter Notebook files in Python which are our first version to do the learning and evaluation part, because we wrote the code at first for each algorithm and combined them later to the [learning.ipynb](https://github.com/chengmeowz/project-posture/blob/main/code/learning.ipynb) when we found there're lots of similar codes.
   * Other folders are mostly for storing the original data files or the article we read, and [extra](https://github.com/chengmeowz/project-posture/blob/main/extrab) folder is to store pictures for the ReadMe.


## Install

Download or clone this repository.

Make sure Python 3 is installed on your machine. 

The following packages are used/imported in the scripts, please install them:

* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [openpyxl](https://pypi.org/project/openpyxl/)
* [os](https://docs.python.org/3/library/os.html) ([source code](https://github.com/python/cpython/blob/3.9/Lib/os.py))
* [pandas](https://pandas.pydata.org/)
* [scikit-learn OR sklearn](https://scikit-learn.org/stable/index.html)
* [scipy](https://www.scipy.org/)
* [zipfile](https://docs.python.org/3/library/zipfile.html) ([source code](https://github.com/python/cpython/blob/3.9/Lib/zipfile.py))

This project uses the [Jupyter Notebook](https://jupyter.org/install) partially. Go check it out if you don't have them locally installed.

```
sh
$ npm install --global project-posture-[placeholder]
```

## Maintainers_Developers

[@ChengZheng](https://github.com/chengmeowz)
[@SunnyQu](https://github.com/suii-bit)

## Contributing

This project is supervised by Dr. [Fabien Scalzo](https://seaver.pepperdine.edu/academics/faculty/fabien-scalzo/) from Pepperdine University, co-advised by Dr. [Adam Pennell](https://seaver.pepperdine.edu/academics/faculty/adam-pennell/) from Pepperdine University, and assisted by Dr. [Renato Naville Watanabe](https://github.com/rnwatanabe).

## License

[GNU GPLv3](LICENSE) © Cheng Zheng and Sunny (Mengchen) Qu
