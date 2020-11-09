# FTU-Django-Dashboard - V3
## New features
- New tests can easily be defined by adding edge cases into the `DataCollection/tests.py` for each object
- Automated tests can now be run before launching the server using `python3 manage.py test` which will test that all the cases outlined in `DataCollection/tests.py` are validated
- Before objects are saved, entries are validated to ensure only valid test configuration inputs are accepted
	- Object IDs must be unique
	- Temperature, Voltage, Field, Time must be bounded between User-Hidden variables for each property

## Configuration Instructions
Configuration instructions are found [here](https://www.youtube.com/watch?v=tXPInUTOc4o&ab_channel=FTUReliability)

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

## Changelog
2020-11-08: Version 3.0 Started

2020-11-08: Version 2.0 merged as main branch

2020-11-04: Version 2.0 Started

2020-11-03: Version 1.0 Complete

2020-11-02: Created by Rohit
