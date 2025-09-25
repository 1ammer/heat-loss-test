# US County Population Aggregator

This script processes a noisy US county demographics dataset, cleans it, and outputs county-level population data as a CSV (one row per county).

In addition, the script aggregates the data to produce state-level totals and a national total row, saving these results in a separate CSV.

## Requirements

- Python 3.8+
- Virtual environment recommended

## virtual envioronment setup

For Ubuntu/Linux

Install venv (if not already installed):

sudo apt update
sudo apt install python3-venv


Navigate to the project directory:

cd ~/Desktop/csv\ generator


Create a virtual environment:

python3 -m venv myenv


Activate the virtual environment:

source myenv/bin/activate

Deactivate the virtual environment (when you're done):

deactivate

For Windows (Command Prompt or PowerShell)

Navigate to the project directory:

Create a virtual environment:

python -m venv myenv


Activate the virtual environment:

Command Prompt:

myenv\Scripts\activate


PowerShell:

.\myenv\Scripts\Activate.ps1


Deactivate the virtual environment (when you're done):

deactivate

### Install dependencies
```bash
pip install -r requirements.txt


### Run_commands

The input dataset is sourced from "https://corgis-edu.github.io/corgis/csv/county_demographics/?utm_source=chatgpt.com" in the data folder, then run the script using the following command:

```bash
python main.py

The generated output csv will be save in the output folder 