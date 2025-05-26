
import pandas as pd


def process_entry(entry):
    # Conditional breakpoint example: stop when name == 'Charlie'
    scores = entry.get("scores", [])
    entry["average"] = sum(scores) / len(scores)
    return entry

def process_data(data):
    result = []
    for entry in data:
        processed = process_entry(entry)
        result.append(processed)
    return result

def calculate_statistics(data):
    df = pd.DataFrame(data)
    # Use PyCharm's pandas DataFrame viewer here
    df["adjusted"] = df["average"] * 1.1  # Watch this column
    return df