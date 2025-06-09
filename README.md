keywords: legacy modernization, flat file to JSON, batch automation, python scripting, REST API transformation, data conversion demo

# 🧩 Legacy File to REST API Transformer — Demo

This repository contains a **simplified demo** of a Python-based transformer that converts structured legacy flat files into JSON-formatted records suitable for REST API ingestion. It’s a stripped-down version of a tool used in real-world automation projects to help teams modernize data pipelines and replace manual or batch-oriented workflows.

---

## 🚀 What It Does

Given:

* A structured text file (CSV-style with a header/trailer)
* A config file defining field names, positions, and types

This demo:

* Skips header and trailer lines
* Parses and validates each line of data
* Applies simple type transformations (e.g., strings, floats, dates)
* Outputs clean JSON in array format

---

## 📁 Project Structure

```bash
.
├── legacy_to_api_demo.py         # Main transformation script
├── config_demo.json              # JSON config describing field mappings
├── sample_input.txt              # Example input file with header/trailer
├── expected_output.json          # What the script should produce
└── README.md                     # This file
```

---

## 🚰 How to Use

Run the script from the command line:

```bash
python legacy_to_api_demo.py sample_input.txt config_demo.json
```

The output will be saved as `API_Transformed_<timestamp>.json` in the working directory.

---

## 🔐 Notes

* **Header/trailer handling** is basic and assumes a known prefix.
* **Type casting** supports basic `string`, `float`, and `date` (no format validation in this demo).
* **Output** is a JSON array compatible with most modern REST APIs.
* This version avoids using external libraries and is ready to expand into more robust use cases.

---

## ✅ Use Case

This is a great starting point for clients who:

* Have legacy systems outputting delimited or fixed-width text files
* Want to modernize by transforming these into clean, REST-friendly JSON
* Need help scripting, testing, or deploying one-off or reusable converters

---

## 🤝 About the Developer

👋 Hi, I’m Jason Witt — I help teams modernize legacy systems with simple, reliable Python tools.

Whether you’re stuck with COBOL-era batch files or just want to automate manual data prep, I can help bridge the gap with lightweight Python scripts tailored to your workflow.

📌 **Upwork Profile**: [COBOL & Python Developer | Hands-On Legacy Modernization](https://www.upwork.com/freelancers/~01c786da236de4a7ee?mp_source=share)

> *Not sure where to start? Let’s have a quick conversation and take the first step toward modernizing your legacy systems.*

---

## 📄 License

This demo is released under the [MIT License](LICENSE).
