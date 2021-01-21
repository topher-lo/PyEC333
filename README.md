# PyEC333
[![Open In nbviewer](https://warehouse-camo.ingress.cmh1.psfhosted.org/b76644f44625d8876b279659d108c1e5334fd8b3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76696577253230696e2d6e627669657765722d6f72616e6765)](https://nbviewer.jupyter.org/github/topher-lo/PyEC333/tree/master/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/topher-lo/PyEC333)

Python code for EC333 Lent term classes. Converted over from R code written by Rachael Meager (LSE).

## Python Preliminaries
> Note: this assumes that the user has a Anaconda Python 3 distribution installed and is using either Mac OX or Linux. If you are a
Windows user and are serious about Python development, I would highly recommend setting up Windows Subsystem for Linux.
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
`(myenv) user@host:~/repos/PyEC333$`

3. Any packages **installed** while this environment this activated will be isolated from your base installation of Python and *any other environment*. 
For example, if you want to install the Python package *statsmodels*, you can run:  
`(myenv) user@host:~/repos/PyEC333$ conda install statsmodels`

4. To **deactivate** the environment, you run: `conda deactivate myenv`
Note: to work with the packages installed in the environment in the future, you can skip to step 2. and continue where you left off.

## Why use virtual environments?
1. **ISOLATION**: packages and Python versions are constantly evolving. Installing all Python packages in the base environment can lead to dependency conflicts 
between packages.

2. **REPRODUCIBILITY**: you should strive to ensure that your code can be run on any other machine. Don't be the person who says "but it works on my machine!". 
Nobody will trust you.

## Getting Started
1. Clone this repository onto your local computer with a Anaconda Python 3 distribution installed.
2. Change into the PyEC333 directory.
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

## Contributing
Found a bug? Wrote a patch? Want to add new content? Please checkout the brief [contribution guide](https://github.com/topher-lo/PyEC333/blob/master/CONTRIBUTING.md).
Any and all contributions are welcome, just open up a Github issue and let's talk metrics and Python. :heart: :snake: :raised_hands:		

## References
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://www.aeaweb.org/research/transparency-reproducibility-credibility-economics
