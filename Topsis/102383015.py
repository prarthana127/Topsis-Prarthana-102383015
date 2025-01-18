import sys
import pandas as pd
import numpy as np

def validate_input_parameters():
    if len(sys.argv) != 5:
        sys.exit("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")

def load_input_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        sys.exit("Error: Input file not found. Please provide a valid file.")

def validate_data(data):
    if data.shape[1] < 3:
        sys.exit("Error: Input file must have at least three columns.")
    
    if not np.issubdtype(data.iloc[:, 1:].dtypes.values.all(), np.number):
        sys.exit("Error: All columns except the first must contain numeric values.")

def validate_weights_and_impacts(weights, impacts, num_criteria):
    weights_list = list(map(float, weights.split(',')))
    impacts_list = impacts.split(',')

    if len(weights_list) != num_criteria or len(impacts_list) != num_criteria:
        sys.exit("Error: Number of weights and impacts must match the number of criteria.")

    if not all(impact in ['+', '-'] for impact in impacts_list):
        sys.exit("Error: Impacts must be either '+' or '-'.")

    return weights_list, impacts_list

def normalize_decision_matrix(data):
    return data.apply(lambda col: col / np.sqrt(np.sum(col ** 2)), axis=0)

def calculate_ideal_best_worst(data, impacts):
    ideal_best = [col.max() if impact == '+' else col.min() for col, impact in zip(data.T.values, impacts)]
    ideal_worst = [col.min() if impact == '+' else col.max() for col, impact in zip(data.T.values, impacts)]
    return np.array(ideal_best), np.array(ideal_worst)

def calculate_topsis_scores(data, weights, impacts):
    normalized_data = normalize_decision_matrix(data)
    weighted_data = normalized_data * weights

    ideal_best, ideal_worst = calculate_ideal_best_worst(weighted_data, impacts)

    distances_best = np.sqrt(np.sum((weighted_data - ideal_best) ** 2, axis=1))
    distances_worst = np.sqrt(np.sum((weighted_data - ideal_worst) ** 2, axis=1))

    scores = distances_worst / (distances_best + distances_worst)
    return scores

def main():
    validate_input_parameters()

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    data = load_input_data(input_file)
    validate_data(data)

    weights_list, impacts_list = validate_weights_and_impacts(weights, impacts, data.shape[1] - 1)

    criteria_data = data.iloc[:, 1:]
    scores = calculate_topsis_scores(criteria_data, weights_list, impacts_list)

    data['Topsis Score'] = scores
    data['Rank'] = data['Topsis Score'].rank(ascending=False, method='dense')

    data.to_csv(result_file, index=False)
    print("Topsis Implementation by Prarthana Samal")
    print("Roll Number: 102383015")
    print(f"Results have been saved to: {result_file}")

if __name__ == "__main__":
    main()
