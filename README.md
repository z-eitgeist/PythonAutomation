# PythonAutomation
Short Python scripts to automate everyday tasks

## Introduction
This repository contains a collection of Python scripts for automating various tasks. Each script is standalone and can be executed independently. 
Each script has its own requirements.txt file, listing the dependencies that need to be installed for the script to run.  

## Requirements
  Python 3.x
  
## Installation

Clone the repository: 

    git clone https://github.com/z-eitgeist/PythonAutomation.git
    
Change directory to the cloned repository or the directory of the script you want to use: 

    cd <repository>
    
Create a virtual environment: 

    python3 -m venv venv

Activate the virtual environment: 

    source venv/bin/activate (Linux/MacOS) 

or 

    venv\Scripts\activate (Windows)

Install the required dependencies for a specific script: 

    pip install -r <script_directory>/requirements.txt

## Usage
    
Run the script: 

    python <script_name>.py


## Script List

URLShortener.py: Shortens any URL you type into interface

folderCleaner.py: Cleans your Downloads folder, move all files older then 30 day into a seperate folder named old_files so you can delete it easily

sortDownloads.py: Sorts downloaded files into folders by extentions


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
