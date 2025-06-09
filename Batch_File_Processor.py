import sys
import os
from datetime import datetime

def validate_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 3:
        raise ValueError("File must contain header, at least one data row, and trailer.")
    return lines

def simple_parse(lines):
    header = lines[0]
    trailer = lines[-1]
    data_lines = lines[1:-1]

    # Dummy header/trailer validation for demonstration
    if not header.startswith("HDR"):
        raise ValueError("Invalid header format.")
    if not trailer.startswith("TRL"):
        raise ValueError("Invalid trailer format.")

    # Simulate parsing and aggregation
    summary = {"records_processed": len(data_lines)}
    return header, summary

def print_report(header, summary):
    timestamp = datetime.now().strftime("%m%d%y_%H%M%S")
    output_file = f"Demo_Report_{timestamp}.txt"

    lines = [f"Header Info: {header}", "Summary:"]
    for k, v in summary.items():
        lines.append(f"  {k}: {v}")
    report = "\n".join(lines)

    print(report)
    with open(output_file, 'w') as f:
        f.write(report)
    print(f"\nReport saved to {output_file}" + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python demo_parser.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        lines = validate_file(file_path)
        header, summary = simple_parse(lines)
        print_report(header, summary)
    except Exception as e:
        print(f"Error: {e}")
