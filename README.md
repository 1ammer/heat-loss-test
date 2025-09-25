# US County Population Aggregator

This script processes a noisy US county demographics dataset, cleans it, and aggregates county-level population data into state-level totals.  
It also appends a **national total row** and saves the final results as a CSV file.

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

Put the file in data folder and run the script with this command
python main.py