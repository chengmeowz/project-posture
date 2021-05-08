# Project Posture

Project Posture is a project for COSC 495 Senior Capstone from Pepperdine University taught by Professor [Fabien Scalzo](http://web.cs.ucla.edu/~fab/) based on Python language development. Its purpose is to investigate for linear and/or non-linear associations between various posturography and self-reported physical activity metrics using data analytics, machine learning, and/or related techniques/processes. The project is under development.

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
- [Usage](#usage)
- [Maintainers/Developers](#maintainers_developers)
- [Contributing](#contributing)
- [License](#license)

## Progress

### Step_1
**Discrete Variable Calculations** (accomplished by Dr. Watanabe)

- [X] Calculate the variables using numpy, pandas, matplotlib.pyplot, zipfile, and welch from scipy.signal in Python.

![alt text](https://github.com/chengmeowz/project-posture/blob/main/extra/variables_calculation.jpg?)

[*copMeasures.ipynb*](https://colab.research.google.com/drive/1oOHwtgAxazdcARhygBb5DLKYAf-HDTT8?usp=sharing#scrollTo=8MrFIHv6OpQu), a file contains Python code for the variables calculation.

### Step_2
**Exploratory Analysis/Machine Learning**

* 【Overall Goal】<br/>
Predict MVPA_minutes.week from any of the four Total Area (cm²) average scores (i.e., EO/firm; EO/foam; EC/firm; EC/foam) as well as AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity.
* 【Used Algorithms】[*Reference*](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
   1. [Ridge regression](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification)
   2. [Kernel ridge regression](https://scikit-learn.org/stable/modules/kernel_ridge.html)
   3. [Adaboost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost)
   4. [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)
   5. [Neural network](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression)
   6. [Support vector machine](https://scikit-learn.org/stable/modules/svm.html#regression)


----------
**Pre-work** (accomplished by Sunny)

- [X] Average the 3 trials for each condition to get an overall average score for **Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s)** for each condition (i.e., we will have 4 average Total Area (cm²) scores)

[variables.xlsx](https://github.com/chengmeowz/project-posture/blob/main/BDS/variables.xlsx), an excel file contains an overall average score for Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), Total Velocity (cm/s), MVPA_minutes.week, Subject, Vision, and Surface for each condition.

- [X] Decide X and Y. 
   - we set X as Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s);
   - Y as MVPA_minutes.week first, and do it again later with switching them


----------
**Data Preprocessing** (accomplished by Sunny)

- [X] Apply [pre-processing](https://scikit-learn.org/stable/modules/preprocessing.html) to the data (Standardization)
[*Reference*](https://towardsdatascience.com/data-preprocessing-in-python-b52b652e37d5)
   - We implemented both [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler) and [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler).

[preprocessing_standard.py](https://github.com/chengmeowz/project-posture/blob/main/project_posture/preprocessing_standard.py), an python file to preprocess data using StandardScaler.

[preprocessing_minmax.py](https://github.com/chengmeowz/project-posture/blob/main/project_posture/preprocessing_minmax.py), an python file to preprocess data using MinMaxScaler.

[standardScaler.xlsx](https://github.com/chengmeowz/project-posture/blob/main/standardScaler/standardScaler.xlsx), an excel file contains the preprocessed data using StandardScaler for MVPA_minutes.week, Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s)).

[minMaxScaler.xlsx](https://github.com/chengmeowz/project-posture/blob/main/minMaxScaler/minMaxScaler.xlsx), an excel file contains the preprocessed data using MinMaxScaler for MVPA_minutes.week, Total Area (cm²), AP RMS (cm), ML RMS (cm), Total Displacement (cm), and Total Velocity (cm/s)).

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
**Evaluation** (accomplished by Sunny)

- [X] Perform the [evaluation using a metric for regression](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
   - We used our model to find y_true and y_pred to draw the graph for a more visualized result, comparing the result from the predicted y value using our six models with the original data.
   - We also implemented the scoring methods (built in GridSearchCV for regression) below to interpret our models: 
```diff
      metrics.mean_absolute_error (i.e. scoring='neg_mean_absolute_error')
      metrics.mean_squared_error (i.e. scoring='neg_mean_squared_error')
      metrics.r2_score (i.e. scoring=‘r2’)
```

[learning.py](https://github.com/chengmeowz/project-posture/blob/main/project_posture/learning.py), an python file to do the learning as well as evaluation part.


```diff 
+ Rehearsal (May. 10, Beijing Time) 
```
<br/>
<h1>【The Day】─=≡Σ(((つ•̀ω•́)つ 
   <br/> 
   Natural Science Seminar (send recording before 0 am, May. 12, Beijing Time)
</h1>
<br/>

## Install

Download or clone this repository.

Make sure Python 3 is installed on your machine. 

The following packages are used/imported in the scripts, please install them:

* [graphviz](https://graphviz.org/)
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [os](https://docs.python.org/3/library/os.html) ([source code](https://github.com/python/cpython/blob/3.9/Lib/os.py))
* [pandas](https://pandas.pydata.org/)
* [scikit-learn](https://scikit-learn.org/stable/index.html)
* [scipy](https://www.scipy.org/)
* [zipfile](https://docs.python.org/3/library/zipfile.html) ([source code](https://github.com/python/cpython/blob/3.9/Lib/zipfile.py))

This project uses the [Jupyter Notebook](https://jupyter.org/install). Go check it out if you don't have them locally installed.

```
sh
$ npm install --global project-posture-[placeholder]
```

## Usage

```
```

## Maintainers_Developers

[@ChengZheng](https://github.com/chengmeowz)
[@SunnyQu](https://github.com/suii-bit)

## Contributing

This project is supervised by Dr. [Fabien Scalzo](https://seaver.pepperdine.edu/academics/faculty/fabien-scalzo/) from Pepperdine University, co-advised by Dr. [Adam Pennell](https://seaver.pepperdine.edu/academics/faculty/adam-pennell/) from Pepperdine University, and assisted by Dr. [Renato Naville Watanabe](https://github.com/rnwatanabe)).

## License

[GNU GPLv3](LICENSE) © Cheng Zheng and Sunny (Mengchen) Qu
