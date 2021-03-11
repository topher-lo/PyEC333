# PyEC333
[![Open In nbviewer](https://warehouse-camo.ingress.cmh1.psfhosted.org/b76644f44625d8876b279659d108c1e5334fd8b3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76696577253230696e2d6e627669657765722d6f72616e6765)](https://nbviewer.jupyter.org/github/topher-lo/PyEC333/tree/main/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/topher-lo/PyEC333)

Python code for EC333 Lent term classes. Converted over from R code written by Rachael Meager (LSE).

## Project Status
- Intro to GMM (Expected completion: TBD)
- (Optional) Non-linear panel methods (Expected completion: TBD)

Note: I am unlikely to complete the GMM notebook anytime soon as I don't really understand how GMM works, GMM in `statsmodels` is still under development, and I do not have permission to reuse the CCAPM dataset provided in EC333.

Further note: The non-linear panel notebook has been put on hold. Conditional logit in `statsmodels` is a work-in-progress
and throws out an [error](https://github.com/statsmodels/statsmodels/issues/5904) that has yet to be resolved.

## Python Preliminaries
Check out the [quick guide](https://github.com/topher-lo/PyEC333/blob/main/PRELIMINARIES.md) on setting up Python virtual environments on your computer.

## :rocket: Getting Started
1. Clone this repository onto your local computer with Python 3 installed
2. Change into the PyEC333 directory.
3. Run the following command: `python3 -m venv ec333_env`. This command creates a new virtual environment called `ec333_env`
5. Activate the newly installed environment by running `source env/bin/activate`
6. Run `pip3 install -r requirements.txt`. This installs into `ec333_env` *all* the packages listed in the `requirements.txt` file
7. Run `python3 -m ipykernel install --user --name=ec333_env`
8. Run the following command to start Jupyter notebook on your browser: `jupyter notebook`
9. Run the cells in the Jupyter notebooks!

> Note: using virtual environments in Jupyter can be a bit tricky. Check out this blog [post](https://janakiev.com/blog/jupyter-virtual-envs/) for a step-by-step guide on the installation process.

## Contributing
Found a bug? Wrote a patch? Want to add new content? Please checkout the brief [contribution guide](https://github.com/topher-lo/PyEC333/blob/main/CONTRIBUTING.md).
Any and all contributions are welcome, just open up a Github issue and let's talk metrics and Python. :heart: :snake: :raised_hands:		

## References
- https://www.aeaweb.org/research/transparency-reproducibility-credibility-economics
