# Project Posture

Project Posture is a project based on Python language development. Its purpose is to investigate for linear and/or non-linear associations between various posturography and self-reported physical activity metrics using data analytics, machine learning, and/or related techniques/processes. The project is under development.

[![license](https://img.shields.io/github/license/chengmeowz/project-posture.svg)](https://github.com/chengmeowz/project-posture/blob/main/LICENSE)
![author](https://img.shields.io/badge/Author-Cheng&Sunny-blue.svg)

The data for this project is from 
* [Santos, D. & Duarte, M. (2016). *A public data set of human balance evaluations*. PeerJ, 4, e2648. doi: 10.7717/peerj.2648.](https://peerj.com/articles/2648/).

The calculation for variables is based on 
* [Duarte M, Freitas SM. *Revision of posturography based on force plate for balance evaluation*. Rev Bras Fisioter. 2010;14(3):183-192.](http://www.scielo.br/pdf/rbfis/v14n3/en_03.pdf)

  and 

* [Duarte M. Comments on *"Ellipse area calculations and their applicability in posturography"* (Schubert and Kirchner, vol.39, pages 518-522, 2014). Gait Posture. 2015;41(1):44-45. doi:10.1016/j.gaitpost.2014.08.008](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.659.1973&rep=rep1&type=pdf)

## Table of Contents

- [Progress](#progress)
   	- [Step 1 Discrete Variable Calculations](#step_1)
   	- [Step 2 Discrete Variable Calculations](#step_2)
- [Install](#install)
- [Usage](#usage)
- [Maintainers/Developers](#maintainers_developers)
- [Contributing](#contributing)
- [License](#license)

## Progress

### Step_1
**Discrete Variable Calculations** (accomplished by Dr. Watanabe)

- [X] Calculate the variables using numpy, pandas, matplotlib.pyplot, zipfile, and welch from scipy.signal in Python.

![alt text](https://github.com/chengmeowz/project-posture/blob/main/extra/variables_calculation.jpg?raw=true)

[*copMeasures.ipynb*](https://colab.research.google.com/drive/1oOHwtgAxazdcARhygBb5DLKYAf-HDTT8?usp=sharing#scrollTo=8MrFIHv6OpQu), a file contains Python code for the variables calculation.

### Step_2
**Exploratory Analysis/Machine Learning**

- [ ] Predict MVPA_minutes.week and/or IPAQ_Category from any of the four Total Area (cm²) average scores (i.e., EO/firm; EO/foam; EC/firm; EC/foam).

## Install

This project uses [Jupyter Notebook](https://jupyter.org/install). Go check it out if you don't have them locally installed.

```
sh
$ npm install --global project-posture-[placeholder]
```

## Usage

```
```

## Maintainers_Developers

[@ChengZheng](https://github.com/chengmeowz).
[@SunnyQu](https://github.com/suii-bit)

## Contributing

This project is supervised by Prof. [Fabien Scalzo](https://seaver.pepperdine.edu/academics/faculty/fabien-scalzo/) from Pepperdine University, co-advised by Prof. [Adam Pennell](https://seaver.pepperdine.edu/academics/faculty/adam-pennell/) from Pepperdine University, and assisted by Dr. [Renato Naville Watanabe](http://ebm.ufabc.edu.br/docentes/renato/) ([*github*](https://github.com/rnwatanabe)) from Federal University of ABC.

## License

[GNU GPLv3](LICENSE) © Cheng Zheng and Sunny (Mengchen) Qu
