# Python Tutorial for Euclid Developers

This repository contains material associated with the basic and advanced Python tutorial.

***Date***: 26-27 May 2016

***Instructors***:
  - Alexandre Boucaud <alexandre.boucaud@ias.u-psud.fr>
  - Mher Kazandjian <mher@strw.leidenuniv.nl>

***Content***:
  - [General installation](#system-installation)
  - [Installation for Euclid dev.](#lodeen-virtual-machine)
  - [Getting the notebooks](#get-the-tutorial-material)
  - [Beginner tutorial list](#beginner-tutorial)
  - [Advanced tutorial list](#advanced-tutorial)

## System installation

This tutorial will be using *Python version 3.4-3.5* with the following libraries

- [NumPy](http://numpy.org) (Numerical Python) for efficient manipulation of array-based data
- [SciPy](http://scipy.org) (Scientific Python) for optimization and other routines
- [Matplotlib](http://matplotlib.org) for scientific visualization
- [AstroPy](http://www.astropy.org) community library gathering astronomical routines

Optionally one might want to install these libraries

- [IPython/Jupyter notebook](http://jupyter.org) as an interactive computing environment
- [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/index.html) a data visualization library


## Setting up lodeen 1.2 to run python3

  get a copy of lodeen virtual machine and launch it 

     http://euclid.roe.ac.uk/projects/codeen-users/wiki/User_Lodeen-installUpgrade

  to install python3.4 and all the pre-requisites for the tutorial.
  run the following in a terminal... (takes about 15 min)
   
    sudo yum install python34 python34-devel libpng-devel git
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.4 get-pip.py
    sudo pip install numpy scipy jupyter matplotlib pytest astropy pyside
    git clone https://github.com/aboucaud/python-euclid2016.git

  to install google chrome (in case firefox keeps crashing for some reason)
  
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    sudo yum install ./google-chrome-stable_current_*.rpm

  to launch the tutorial with google chrome
  
    jupyter-notebook python-euclid2016 --browser=google-chrome

  to launch the tutorial with the default browser
  
    jupyter-notebook python-euclid2016
  
## Downloading the tutorial materials

If you have ``git`` installed, you can clone the material of this tutorial with

    git clone https://github.com/aboucaud/python-euclid2016.git

If you can't or don't want to install ``git``, there is a link above to download
the contents of this repository as a zip file.  We may make minor changes to
the repository during the tutorial, so cloning the repository is the best option.

You can access a static view of the notebooks following the links below.
To modify them, first download the tutorial repository, change to the notebooks
directory, and run

    jupyter notebook

This will launch a page on web browser with the list of notebooks.
For more information on the IPython/Jupyter notebook,
see http://ipython.org/notebook.html or http://jupyter.org

Note that some of the code in these notebooks may not work outside the
directory structure of this tutorial, so it is important to clone the full
repository if possible.

---

## Beginner tutorial

### [1. General Python concepts](http://nbviewer.jupyter.org/github/aboucaud/python-euclid2016/blob/master/notebooks/01-Introduction.ipynb)

variables, collections, iteration, strings, logical operations, functions, classes, ipython, python2/3...

### [2. Scientific computing with Python: NumPy/SciPy](http://nbviewer.ipython.org/urls/github.com/aboucaud/python-euclid2016/blob/master/notebooks/02-Numpy.ipynb)

arrays creation, accessing elements, array operations, masked array, broadcasting...

### [3. Plotting with Python](http://nbviewer.ipython.org/urls/github.com/aboucaud/python-euclid2016/blob/master/notebooks/03-Plotting.ipynb)

2D plots, labeling, configuration, 3D plots, saving, Matplotlib/Seaborn

### [4. The AstroPy library](http://nbviewer.ipython.org/urls/github.com/aboucaud/python-euclid2016/blob/master/notebooks/04-Astropy.ipynb)

reading files (ascii/fits/..), physical constants, cosmological calculations, sky coordinates manipulation...


## Advanced tutorial

### [5. Euclid coding standards](https://github.com/aboucaud/python-euclid2016/blob/master/notebooks/05-Euclid.ipynb)

code formatting, naming conventions, docstring formatting, static analysis...

### [6. Project architecture](http://nbviewer.ipython.org/urls/github.com/aboucaud/python-euclid2016/blob/master/notebooks/06-Project.ipynb)

TBD

### [7. Testing](http://nbviewer.ipython.org/urls/github.com/aboucaud/python-euclid2016/blob/master/notebooks/07-Testing.ipynb)

pytest, writing unit tests, fixtures, configuration, doctests, running tests ...

### [8. Tips & Tricks](https://github.com/aboucaud/python-euclid2016/blob/master/notebooks/08-Misc.ipynb)

ipython configuration, more on classes, things to avoid, quick optimization, debugging, extending python ...

