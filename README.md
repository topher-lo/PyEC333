# py-ec333
Python code for EC333 Lent term classes. Ported over from R code written by Rachel Meager (LSE).

## Python Preliminaries
> Note: this assumes that the user has a Anaconda Python 3 distribution installed and is using either Mac OX or Linux. If you are a
Windows user and are serious about Python development, I would highly recommend installing a Windows Linux Subsystem 
(https://docs.microsoft.com/en-us/windows/wsl/install-win10).

> Note: DO NOT run any of the commands in this section. This discussion is preliminary knowledge to the section "Getting Started".

A best practice for Python development, before executing any code, is to set-up a virtual environment.

> A virtual environment is a named, isolated, working copy of Python that that maintains its own files, directories, 
and paths so that you can work with specific versions of libraries or Python itself without affecting other Python projects.  
(https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

There are four key steps to using a virtual environment. 
1. You first **create** it using either the terminal or an Anaconda Prompt:
`conda create --name myenv`
Note: replace `myenv` with the environment name (e.g. ec333)

2. You then **activate** the environment by running: `conda activate myenv`
You have activated your environment if the beginning of your command line looks something like this:  
`(myenv) user@host:~/repos/py-ec333$`

3. Any packages **installed** while this environment this activated will be isolated from your base installation of Python and *any other environment*. 
For example, if you want to install the Python package *statsmodels*, you can run:  
`(myenv) user@host:~/repos/py-ec333$ conda install statsmodels`

4. To **deactivate** the environment, you run: `conda deactivate myenv`
Note: to work with the packages installed in the environment in the future, you can skip to step 2. and continue where you left off.

## Why use virtual environments?
1. **ISOLATION**: packages and Python versions are constantly evolving. Installing all Python packages in the base environment can lead to dependency conflicts 
between packages.

2. **REPRODUCIBILITY**: you should strive to ensure that your code can be run on any other machine. Don't be the person who says "but it works on my machine!". 
Nobody will trust you.

## Getting Started
1. Clone this repository onto your local computer with a Anaconda Python 3 distribution installed.
2. Change into the py-ec333 directory.
3. Run the following command: `conda env create -f environment.yml`. This command creates a new virtual environment and installs 
into that environment *all* the packages listed in the `environment.yml` file.
4. Activate the newly installed environment by running `conda activate ec333`
5. Run the following command to start Jupyter notebook on your browser: `jupyter notebook`
6. Run the cells in the Jupyter notebooks!

> Note: The first line of the `yml` file sets the new environment's name.

> Note: To learn how to share your own virtual environments through an `environment.yml` file, check out the following link: 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment

> Note: if you run into any "package not found" errors, option 3. in this Stackoverflow post's top comment might help 
https://stackoverflow.com/questions/58068818/how-to-use-jupyter-notebooks-in-a-conda-environment

## References
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://www.aeaweb.org/research/transparency-reproducibility-credibility-economics
