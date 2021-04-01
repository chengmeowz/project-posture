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

* 【Overall Goal】<br/>Predict MVPA_minutes.week and/or IPAQ_Category from any of the four Total Area (cm²) average scores (i.e., EO/firm; EO/foam; EC/firm; EC/foam).
* 【Used Models】<br/>placeholder

<h2>Temporary schedule</h2>

```diff 
! Orange = YOUR DUE!!! 
@@ Purple = meet w/ Scalzo @@ 
+ Green = meet w/ each other 
# Gray = reminder (Your mission is right below your name.)
```

```diff
@@ Organize ideas & questions for Scalzo and/or Remind scalzo the doc. (email: Cheng; Apr. 1, Beijing Time) @@
```
**1. We set X as Total Area (cm²), Y as MVPA_minutes.week.** 
```diff
# (Step 1 according to the meeting)
```
```diff
! Sunny (Deadline: 11:55 pm, Apr. 4, Beijing Time)
# (Step 1.5 according to the meeting)
```
- [ ] Average the 3 trials for each condition to get an overall average score for Total Area (cm²) for each condition (i.e., we will have 4 average Total Area (cm²) scores) 
```diff
# Should ends with a sheet like below.
```
![alt text](https://github.com/chengmeowz/project-posture/blob/main/extra/step1.5.png)
```diff 
+ Discuss code & form. (8 am, Apr. 5, Beijing Time)
```
```diff
! Cheng (Deadline: 11:55 pm, Apr. 13, Beijing Time)
# (Step 2-3 according to the meeting)
```
- [ ] Pick one column as the test data and rest columns as the training data, then use the training data to create one model (placeholder for which one) in【Used Models】and put the result into an excel
- [ ] Repeat previous step till get an excel with all columns picked as the test data and organize the result into an excel (for one model)
```diff
# Should ends with a sheet like below.
```
![alt text](https://github.com/chengmeowz/project-posture/blob/main/extra/step3.png)
- [ ] Repeat all previous steps till get (total number of【Used Models】) excels for all models (simply just change the model variable in the code)
```diff 
+ Discuss code & form. (8 am, Apr. 14, Beijing Time)
```
```diff
@@ Meet w/ scalzo (email: Sunny; 6 am, Apr. 15, Beijing Time) @@
```
```diff
! Sunny (Deadline: 11:55 pm, Apr. 20, Beijing Time)
```
There is a confusion that we can do Step 4 in two ways:
- [ ] 1. we can just use the excels we got from Step 3 and re-organize it
- [ ] 2. Or we can re-do all the process by pick one column as the test data and rest columns as the training data, then use the training data to create for all models in【Used Models】and put the result into an excel; Repeat previous step till get (total number of【columns】) excels for all models (simply just change the column number in the code)
```diff
# Should ends with a sheet like below.
```
![alt text](https://github.com/chengmeowz/project-posture/blob/main/extra/step4.png)
```diff 
+ Discuss code & form. (8 am, Apr. 21, Beijing Time)
```
```diff
@@ Meet w/ scalzo (email: Cheng; 6 am, Apr. 22, Beijing Time) @@
```

<h3>Congratulations! Stage 1 clear (/≧▽≦)/</h3><br/>

**2. We set X as MVPA_minutes.week, Y as Total Area (cm²).**
```diff
! Cheng (Deadline: 11:55 pm, Apr. 24/25, Beijing Time)
```
- [ ] repeat Step 3

```diff 
! Sunny (Deadline: 11:55 pm, Apr. 26/27, Beijing Time)
```
- [ ] repeat Step 4
```diff 
+ Discuss code & form. (8 am, Apr. 27/28, Beijing Time)
```
```diff
@@ Meet w/ scalzo (email: Sunny; 6 am, Apr. 28/29, Beijing Time) @@
```

<h3>Congratulations! Goodbye, MVPA_minutes.week \(^o^)/</h3><br/>

```diff 
# (Using WeChat dice, higher = A; Same -> Rock-paper-scissors -> winner = A) 
```

- [ ] **A -> X as Total Area (cm²), Y as IPAQ_Category.**

- [ ] **B -> X as IPAQ_Category, Y as Total Area (cm²).**
```diff
! C&S (Deadline: 12:00 pm, May. 7, Beijing Time)
# Total Forms = 8.
```
```diff
+ Sum Up (11:55 pm, May. 7, Beijing Time)
```
```diff
@@ Meet w/ scalzo (email: Sunny; 6 am, May. 8, Beijing Time) @@
```

<h3>Project Finished (๑•̀ㅂ•́)و✧</h3><br/>

```diff 
+ Decide presentation content & assign time check (12 pm, May. 8, Beijing Time) 
```

<h4>Practicing Presentation :-O </h4>

```diff 
+ Rehearsal (8 am, May. 11, Beijing Time) 
```
<br/>
<h1>【The Day】─=≡Σ(((つ•̀ω•́)つ 
   <br/> 
   Natural Science Seminar (3 am, May. 12, Beijing Time)
</h1>
<br/>

## Install

Download or clone this repository.

Make sure Python 3 is installed on your machine. The following packages are used in the scripts.

* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [scipy](https://www.scipy.org/)
* [zipfile](https://docs.python.org/3/library/zipfile.html) ([source code](https://github.com/python/cpython/blob/3.9/Lib/zipfile.py))

This project possibly will use [Jupyter Notebook](https://jupyter.org/install). Go check it out if you don't have them locally installed.

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

This project is supervised by Dr. [Fabien Scalzo](https://seaver.pepperdine.edu/academics/faculty/fabien-scalzo/) from Pepperdine University, co-advised by Dr. [Adam Pennell](https://seaver.pepperdine.edu/academics/faculty/adam-pennell/) from Pepperdine University, and assisted by Dr. [Renato Naville Watanabe](http://ebm.ufabc.edu.br/docentes/renato/) ([*github*](https://github.com/rnwatanabe)) from Federal University of ABC.

## License

[GNU GPLv3](LICENSE) © Cheng Zheng and Sunny (Mengchen) Qu
