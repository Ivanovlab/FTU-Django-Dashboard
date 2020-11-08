# FTU-Django-Dashboard - v2
## Installer Instructions
### Requirements
- Works best with either: Mac, Linux, Windows (w/ Windows Linux Subsystem enabled)
- Installer can be a little dicey with windows
- python3 must be installed and executable (`python` can be aliased by `alias python=python3`)

### Steps
	1. After downloading the installer, navigate to the directory where it is saved.
	2. run the command `bash installer.sh`
		a) If you get some "/r" errors, cancel the install and delete the created folder, then run `dos2unix installer.sh` and re-run `bash installer.sh`
	3. If the install works properly, some final instructions will be given after the script runs. Follow these instructions.
	4. Navigate to http://127.0.0.1:8000/DataCollection/ in a browser and the app should be up and running

## Development Notes

### Bugs
- Plot generation needs to be reverted back to previous version
- You'll only be able to use the plotting / results features if you specify the 'Filename for results' to `SampleTest.csv` before you create an experiment

### To-Do's
- Fix label generation for plots
- Finish V2 Documentaiton

### Features (Not updated)
- User-defined Test Configurations
  - User can specify ID, Description, Temperature, Voltage, Test Time, Field and Serial Rate as variables for a test configuration
  - User can create new Test Configurations for experiments, or can re-use pre-existing test configuraitons
- Experiment History
  - User can define new experiments by user-defined Test Configurations
  - User can download .csv file containing data from previous experiments
  - User can generate over 700 graphs using data from previous experiments, saved as images

## Changelog
2020-11-04: Version 2.0 Started

2020-11-03: Version 1.0 Complete

2020-11-02: Created by Rohit
