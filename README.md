# dataquest

Learning data science with https://dataquest.io

## Basemap

The Matplotlib [Basemap](https://matplotlib.org/basemap/) library is a little tricky to install on Windows.

The steps I followed:

1. Install [Miniconda](https://conda.io/miniconda.html)
1. `conda create -n dataquest python=3.6`
1. `activate dataquest`
1. `conda install -c conda-forge basemap=1.1.0`
1. `conda install -c conda-forge basemap-data-hires`
1. Install the rest of the data science packages: `conda install jupyter numpy scipy scikit-learn pandas`
1. Export the environment with `conda env export > environment.yml`

In theory, one should be able to recreate this environment with these commands:

```
> conda env create -f environment.yml
> activate dataquest
> conda list
```
