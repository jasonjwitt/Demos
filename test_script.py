import subprocess
import glob
import os
import time

def run_demo(input_file, config_file):
    print(f"Running Batch_Processor_Demo.py with input '{input_file}' and config '{config_file}'...")
    result = subprocess.run(
        ['python3', 'Batch_Processor_Demo.py', input_file, config_file],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running script: {result.stderr}")
        return False
    return True

def find_latest_report():
    reports = glob.glob('Demo_Report_*.txt')
    if not reports:
        print("No report files found.")
        return None
    latest_report = max(reports, key=os.path.getmtime)
    return latest_report

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read().strip()
        content2 = f2.read().strip()
    return content1 == content2

if __name__ == '__main__':
    input_file = 'sample_input.txt'
    config_file = 'config/default_config.json'
    expected_output_file = 'expected_output.txt'

    if not run_demo(input_file, config_file):
        exit(1)

    time.sleep(1)  # Ensure file system has updated timestamp

    output_file = find_latest_report()
    if output_file is None:
        print("❌ Test Failed: No output file generated.")
        exit(1)

    print(f"Comparing output file '{output_file}' with expected output '{expected_output_file}'...")

    if compare_files(output_file, expected_output_file):
        print("✅ Test Passed: Output matches expected output.")
    else:
        print("❌ Test Failed: Output differs from expected.")
