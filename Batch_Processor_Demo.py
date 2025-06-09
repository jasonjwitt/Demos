import sys
import json
import os
from datetime import datetime
from collections import defaultdict

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def validate_and_parse_lines(lines, config):
    if len(lines) < 3:
        raise ValueError("File must contain a header, at least one data line, and a trailer.")

    header = lines[0]
    trailer = lines[-1]
    data_lines = lines[1:-1]

    if not header.startswith(config.get("header", {}).get("prefix", "")):
        raise ValueError("Invalid header format.")
    if not trailer.startswith(config.get("trailer", {}).get("prefix", "")):
        raise ValueError("Invalid trailer format.")

    return header, data_lines, trailer

def parse_data_lines(data_lines, config):
    delimiter = config.get("delimiter", ",")
    fields = config.get("fields", [])
    category_field = config.get("category_field")
    amount_field = config.get("amount_field")

    category_index = next((f["index"] for f in fields if f["name"] == category_field), None)
    amount_index = next((f["index"] for f in fields if f["name"] == amount_field), None)

    if category_index is None or amount_index is None:
        raise ValueError("Config must specify valid category and amount fields.")

    summary = defaultdict(float)
    for line in data_lines:
        parts = line.strip().split(delimiter)
        try:
            category = parts[category_index].strip()
            amount = float(parts[amount_index].strip())
            summary[category] += amount
        except (IndexError, ValueError):
            continue  # Skip bad lines silently for demo purposes

    return summary

def print_report(header, summary):
    timestamp = datetime.now().strftime("%m%d%y_%H%M%S")
    output_file = f"Demo_Report_{timestamp}.txt"

    lines = [f"Header Info: {header}", "Summary by Category:"]
    for k, v in summary.items():
        lines.append(f"  {k}: ${v:,.2f}")
    report = "\n".join(lines) + "\n"

    print(report)
    with open(output_file, 'w') as f:
        f.write(report)
    print(f"\nReport saved to {output_file}" + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python batch_demo.py <input_file> <config_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    config_path = sys.argv[2]

    try:
        with open(input_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        config = load_config(config_path)
        header, data_lines, trailer = validate_and_parse_lines(lines, config)
        summary = parse_data_lines(data_lines, config)
        print_report(header, summary)
    except Exception as e:
        print(f"Error: {e}")
