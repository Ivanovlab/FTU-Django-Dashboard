# FTU-Django-Dashboard
## Version 2
### Requirements
- Interface COM port
  - By interfacing the COM ports, we are able to communicate to the arduino to transmit/receive test data
- MQTT Functionality
  - By implementing MQTT, we are able to communicate wirelessly to the arduino to transmit/receive test data
- Error case handling
  - Add error case handling to avoid user errors such as specifying temperature as a non-int value
- More configurable graphs
  - Allow user to change graph type, add legends, etc.
  - Allow user to apply filters directly to collected data from GUI
  - Allow user to specify a start and end time for plot diagram
  
### Features
- User-defined Test Configurations
  - User can specify ID, Description, Temperature, Voltage, Test Time, Field and Serial Rate as variables for a test configuration
  - User can create new Test Configurations for experiments, or can re-use pre-existing test configuraitons
- Experiment History
  - User can define new experiments by user-defined Test Configurations
  - User can download .csv file containing data from previous experiments
  - User can generate over 700 graphs using data from previous experiments, saved as images


## Changelog
2020-11-03: Version 2.0 Started

2020-11-03: Version 1.0 Complete

2020-11-02: Created by Rohit
