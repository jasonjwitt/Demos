import sys
import json
import os
from datetime import datetime

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def validate_and_parse_lines(lines, config):
    header_prefix = config['header']['prefix']
    trailer_prefix = config['trailer']['prefix']

    if not lines[0].startswith(header_prefix):
        raise ValueError("Header missing or invalid.")
    if not lines[-1].startswith(trailer_prefix):
        raise ValueError("Trailer missing or invalid.")

    data_lines = lines[1:-1]
    parsed_records = []

    for line in data_lines:
        parts = line.strip().split(config['delimiter'])
        record = {}
        for field in config['fields']:
            index = field['index']
            name = field['name']
            required = field.get('required', False)
            field_type = field.get('type', 'string')

            if index >= len(parts):
                if required:
                    raise ValueError(f"Missing field '{name}' in line: {line}")
                else:
                    value = None
            else:
                raw_value = parts[index].strip()
                if field_type == "float":
                    value = float(raw_value)
                elif field_type == "date":
                    value = raw_value  # Date parsing can be added later
                else:
                    value = raw_value
            record[name] = value
        parsed_records.append(record)

    return parsed_records

def save_json_output(records):
    timestamp = datetime.now().strftime("%m%d%y_%H%M%S")
    output_filename = f"API_Transformed_{timestamp}.json"
    with open(output_filename, 'w') as f:
        json.dump(records, f, indent=2)
    print(f"\n✅ Transformed {len(records)} records to JSON.")
    print(f"📁 Output saved to: {output_filename}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python legacy_to_api_demo.py <input_file> <config_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    config_path = sys.argv[2]

    try:
        if not os.path.isfile(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(input_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        config = load_config(config_path)
        records = validate_and_parse_lines(lines, config)
        save_json_output(records)

    except Exception as e:
        print(f"❌ Error: {e}")
