
import pathlib
import json

from utils import process_data, calculate_statistics


with pathlib.Path("./data.json").open("r", encoding="utf-8") as f:
    DATA = json.load(f)


def main(data):
    print("Starting data processing...")
    processed_data = process_data(data)  # Set a breakpoint here

    print("Calculating statistics...")
    stats = calculate_statistics(processed_data)

    print("Final statistics:")
    print(stats)


if __name__ == '__main__':
    main(DATA)
