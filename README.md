# Topsis Python Package

## Made By
Prarthana Samal (Roll Number 102383015)

## Description
The Topsis Python Package is a Python library that provides an implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. TOPSIS is a multi-criteria decision-making method used to determine the best alternative among a set of alternatives based on their performance on multiple criteria.

## Installation
You can install this package using pip (if published to PyPI) or clone the repository directly:
```bash
pip install topsis-prarthana
```

## Usage
Use the following command to perform TOPSIS analysis on a dataset:

```bash
topsis.py data.csv "1,0,1,0,1" "+,-,+,-,+" output.csv
```

### Arguments:
- `data.csv`: Path to the input CSV file containing the dataset.
- `"1,0,1,0,1"`: Weights for each criterion separated by commas.
- `"+,-,+,-,+"`: Impacts for each criterion (either `+` for maximizing or `-` for minimizing).

## Input
![Screenshot 2025-01-18 120924](https://github.com/user-attachments/assets/6db1365f-5681-4d65-9064-d64a9bc47b1a)

## Output
![Screenshot 2025-01-18 121833](https://github.com/user-attachments/assets/7e15bc88-a0de-48cb-80ef-6071567fb236)


