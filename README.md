# Topsis Python Package

## Made By
Prarthana Samal (Roll Number 102383015)

## Description
The Topsis Python Package is a Python library that provides an implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. TOPSIS is a multi-criteria decision-making method used to determine the best alternative among a set of alternatives based on their performance on multiple criteria.

## Features
- Easy implementation of the TOPSIS method.
- Accepts CSV datasets with multiple criteria.
- Supports weighted and impact-based decision-making.
- Generates ranked alternatives with scores.

## Installation
You can install this package using pip (if published to PyPI) or clone the repository directly:
```bash
pip install topsis-package
```

## Usage
Use the following command to perform TOPSIS analysis on a dataset:

```bash
topsis data.csv "1,0,1,0,1" "+,-,+,-,+"
```

### Arguments:
- `data.csv`: Path to the input CSV file containing the dataset.
- `"1,0,1,0,1"`: Weights for each criterion separated by commas.
- `"+,-,+,-,+"`: Impacts for each criterion (either `+` for maximizing or `-` for minimizing).

