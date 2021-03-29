# Python Preliminaries

> Note: this assumes that the user has Python 3 installed and is using either Mac OX or Linux. If you are a
Windows user and are serious about Python development, I would highly recommend setting up Windows Subsystem for Linux.
(https://docs.microsoft.com/en-us/windows/wsl/install-win10).

> Note: DO NOT run any of the commands in this section. This discussion is preliminary knowledge to the section "Getting Started".

A best practice for Python development, before executing any code, is to set-up a virtual environment.

> A virtual environment is a named, isolated, working copy of Python that that maintains its own files, directories, 
and paths so that you can work with specific versions of libraries or Python itself without affecting other Python projects.  
(https://docs.python.org/3/library/venv.html)

There are four key steps to using a Python 3 virtual environment. 
1. You first **create** it using the terminal:
```bash
python3 -m venv myenv
```
Note: replace `myenv` with the environment name (e.g. ec333)

2. You then **activate** the environment by running: `source myenv/bin/activate`
You have activated your environment if the beginning of your command line looks something like this:  
```bash
(myenv) user@host:~/repos/PyEC333$
```

3. Any packages **installed** while this environment this activated will be isolated from your base installation of Python and *any other environment*. 
For example, if you want to install the Python package *statsmodels*, you can run:  
```bash
(myenv) user@host:~/repos/PyEC333$ pip3 install statsmodels
```

Note: `pip3` is the package installer (and management tool) for Python 3.

4. To **deactivate** the environment, you run: `source deactivate`
Note: to work with the packages installed in the environment in the future, you can skip to step 2. and continue where you left off.

## Why use virtual environments?
1. **ISOLATION**: packages and Python versions are constantly evolving. Installing all Python packages in the base environment can lead to dependency conflicts 
between packages.

2. **REPRODUCIBILITY**: other people should be able to reproduce your work with minimal difficulty. Don't be the person who says "but it works on my machine!".
