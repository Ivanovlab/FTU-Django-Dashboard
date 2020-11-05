# FTU-Django-Dashboard
## Installer Instructions
This installer only currently works if the user has python3 and has either linux or windows linux subsystem enabled.

Download the installer, `FTU-Django-Dashboard/installer.sh`

After installing it, navigate to it's location and run the command:
`$ dos2unix installer.sh`
`$ bash installer.sh`

This created a virtual directory in your current location, called `ftu` in your current directory, this is where the repo and dependancies have been created.

Navigate to the `manage.py` file to start the program with the following command:
`$ cd ftu/FTU-Django-Dashboard/TestGUI `

Then run the program with the command:
`$ python3 manage.py runserver`

Then navigate to http://127.0.0.1:8000/DataCollection/ in a browser and the app should be up and running
## Version 1
### Features
- User-defined Test Configurations
  - User can specify ID, Description, Temperature, Voltage, Test Time, Field and Serial Rate as variables for a test configuration
  - User can create new Test Configurations for experiments, or can re-use pre-existing test configuraitons
- Experiment History
  - User can define new experiments by user-defined Test Configurations
  - User can download .csv file containing data from previous experiments
  - User can generate over 700 graphs using data from previous experiments, saved as images

## Changelog
2020-11-03: Version 1.0 Complete

2020-11-02: Created by Rohit
