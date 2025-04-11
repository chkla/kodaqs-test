
# Germany Election Analysis 2017 (Adapted)

This project analyzes the 2017 Germany election data (adapted dataset and analysis, see https://www.kaggle.com/code/ivy1219/germany-election-in-2017/notebook), providing visual insights into voter turnout, valid votes, and invalid vote distribution.

## 💾 Files:
- **election_analysis_adapted.py**: Python script for analysis and generating figures.
- **run_adapted.sh**: Bash script to execute the Python script.
- **figures/**: Directory for saved figures.

## 📚 Dataset: 
Link: https://www.govdata.de/suche/daten/bundestagswahl-2017 (more details in the codebook `data/2017_german_election_codebook.md`) 

## 🚀 Setup:
1. Find the provided CSV file `2017_german_election_overall.csv` in the project directory `/data`.
2. Install the required dependencies using either of the following methods:

Option 1: Install directly via pip
----------------------------------
pip install pandas==2.2.3 matplotlib==3.10.1 seaborn==0.13.2

Option 2: Install from requirements.txt
---------------------------------------
pip install -r requirements.txt

## 🏃🏽‍♀️ Running:
You can also run the analysis script using the provided bash script. This will load all requirements, execute the Python script and generate the figures in the `figures/` directory.

```bash
./run_adapted.sh
```

## 📚 Citation & Credits

If you use this project or dataset in your work, please consider citing it as follows:

**Example Citation (APA style):**
Author. (2025). *German Federal Election 2017 Data Analysis*. GitHub Repository. https://github.com/chkla/kodaqs-test

**BibTeX:**
```
@misc{german_election_2017,
  author       = {Your Name},
  title        = {German Federal Election 2017 Data Analysis},
  year         = 2025,
  url          = {https://github.com/chkla/kodaqs-test},
  note         = {Accessed April 11, 2025}
}
```
