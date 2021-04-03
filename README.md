# MLOPS (WINE QUALITY PREDICTION)

This repository is a demo of building a Machine Learning pipeline with Continuous Integration using GITHUB Actions and DVC.

### BASIC INSTALLATION STEPS
```
$ conda create -n wineq python=3.7 -y
$ conda activate wineq
$ pip install -r requirements.txt
$ dvc init 
$ dvc add data_given/winequality.csv
```

### Dataset:

Download dataset from the following link.

Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── data_given
    │
    ├── saved_models       <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── report            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    |
    ├── src                <- Source code for use in this project.
        │
        ├── get_data.py
        │
        ├── load_data.py
        │
        ├── split_data.py        
        │
        └── train_evaluate.py



--------
