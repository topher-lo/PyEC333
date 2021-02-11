# PyEC333
[![Open In nbviewer](https://warehouse-camo.ingress.cmh1.psfhosted.org/b76644f44625d8876b279659d108c1e5334fd8b3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76696577253230696e2d6e627669657765722d6f72616e6765)](https://nbviewer.jupyter.org/github/topher-lo/PyEC333/tree/master/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/topher-lo/PyEC333)

Python code for EC333 Lent term classes. Converted over from R code written by Rachael Meager (LSE).

## To Do
- Intro to GMM (Expected completion: TBD)
- (Optional) Non-linear panel methods (Expected completion: TBD)

Note: I am unlikely to complete the GMM notebook anytime soon as I don't really understand how GMM works, GMM in `statsmodels` is still under development, and I do not have permission to reuse the CCAPM dataset provided in EC333.

Further note: The non-linear panel notebook has been put on hold. Conditional logit in `statsmodels` is a work-in-progress
and throws out an [error](https://github.com/statsmodels/statsmodels/issues/5904) that has yet to be resolved.

## Python Preliminaries
Check out the [quick guide](https://github.com/topher-lo/PyEC333/blob/master/PRELIMINARIES.md) on setting up an Anaconda Python data science environment on your computer.

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
