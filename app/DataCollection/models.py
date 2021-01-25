################################################################################
#   File Name: models.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file defines models used
#       in our database
#
#   File History:
#   2020-11-05: Result model added by Rohit
#   2020-11-02: Created by Rohit
#
################################################################################
# Imports ---------------------------------------------------------------------
# Django imports
from django.db import models
from django.conf import settings
# Python imports
import numpy as np
import os
import json
import paho.mqtt.client as mqtt
import serial

# Class Definitions-------------------------------------------------------------
class TestConfiguration(models.Model):
    # Constants
    i_MinimumTemperature    = 0
    i_MaximumTemperature    = 125
    i_MinimumVoltage        = -50
    i_MaximumVoltage        = 50
    i_MinimumField          = 0
    i_MaximumField          = 50
    i_MinimumTestTime       = 0
    i_MaximumTestTime       = 1000
    # Variables
    i_TestId            = models.IntegerField(default=0)
    s_TestDesc          = models.CharField(max_length=200, default="Default Test")
    i_DesiredTemp       = models.IntegerField(default=0)
    i_DesiredVoltage    = models.IntegerField(default=0)
    i_DesiredField      = models.IntegerField(default=0)
    i_DesiredTestTime   = models.IntegerField(default=0)
    i_DesiredSerialRate = models.IntegerField(default=9600)

    ############################################################################
    #   Function Name: save
    #   Function Description: Checks inputs before saving
    #   Inputs: (self) | Output: either ValueError or a saved object
    #   Function History:
    #       2020-11-08: Created by Rohit
    ############################################################################
    def save(self, *args, **kwargs):
        # Check i_TestId uniqueness
        try:
            b_TestIdIsUnique = False
            tc = TestConfiguration.objects.get(i_TestId = self.i_TestId)
        except Exception as e:
            if type(e) == self.DoesNotExist:
                # No object was found with this unique
                b_TestIdIsUnique = True

        if b_TestIdIsUnique == False:
            raise ValueError(f"Test ID: {self.i_TestId} is already in use")

        if self.i_TestId < 0:
            raise ValueError("Test ID must be a positive integer")

        if self.i_DesiredTemp < self.i_MinimumTemperature or self.i_DesiredTemp > self.i_MaximumTemperature:
            raise ValueError(f"Temperature must be between {self.i_MinimumTemperature} and {self.i_MaximumTemperature}")

        if self.i_DesiredVoltage < self.i_MinimumVoltage or self.i_DesiredVoltage > self.i_MaximumVoltage:
            raise ValueError(f"Voltage must be between {self.i_MinimumVoltage} and {self.i_MaximumVoltage}")

        if self.i_DesiredField < self.i_MinimumField or self.i_DesiredField > self.i_MaximumField:
            raise ValueError(f"Magnetic Field must be betten {self.i_MinimumField} and {self.i_MaximumField}")

        if self.i_DesiredTestTime < self.i_MinimumTestTime or self.i_DesiredTestTime > self.i_MaximumTestTime:
            raise ValueError(f"Test time must be between {self.i_MinimumTestTime} and {self.i_MaximumTestTime}")

        # TODO: Fix this thang
        if self.i_DesiredSerialRate != 9600:
            raise ValueError("Serial Rate must be 9600")

        super().save(*args, **kwargs)

    ############################################################################
    #   Function Name: GetJSONInstructions
    #   Function Description: Returns the JSON object to be sent to board
    #   Inputs: (self) | Output: JSON instructions to be sent
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def GetJSONInstructions(self):
        test_values = {
            'temperature':      self.i_DesiredTemp,
            'v_stress':         self.i_DesiredVoltage,
            'test_time':        self.i_DesiredTestTime,
            'magnetic_field':   self.i_DesiredField,
            'Test_start':       1,
            'Test_stop':        0,
            'serial_rate':      self.i_DesiredSerialRate,
            }
        measurement_params = {
            'temperature':      {"unit": "C"},
            'v_stress':         {'unit': 'mV'},
            'test_time':        {'unit': 'seconds'},
            'magnetic_field':   {'unit': "mT"},
            'serial_rate':      {'unit':'milliseconds'}
            }
        instructions = {
            'id':               self.i_TestId,
            'description':      self.s_TestDesc,
            'test_values':      test_values,
            'measurement_params': measurement_params,
            }
        js_instructions = json.dumps(instructions)
        return js_instructions

    ############################################################################
    #   Function Name: SendJsonInstructions
    #   Function Description: Sends the MQTT packet to broker
    #   Inputs: (self) | Output: Sent object
    #   Function History:
    #       2020-11-12: Created by Rohit
    ############################################################################
    def SendJsonInstructions(self):
        s_Inst  = self.GetJSONInstructions()
        try:
            o_Serial = serial.Serial("COM3")
            if not o_Serial.isOpen():
                o_Serial.open()
            o_Serial.write(bytes(s_Inst, "utf-8"))
            o_Serial.close()

        except Exception as e:
            print(e)

    def SendMqttInstructions(self):
        # Use Built-in method to retreive JSON instructions
        s_Inst = self.GetJSONInstructions()
        # Create MQTT client
        client = mqtt.Client()
        # Connect to the wireless broker
        client.connect("35.173.190.207", 1883, 60)
        # Publish the message to topic

        s_Topic = "test"
        client.publish(s_Topic, payload=s_Inst, qos=0, retain = False)
        # Save some memory by deleting the client
        del client

        return

    ############################################################################
    #   Function Name: ___str___
    #   Function Description: Returns the objects identity string
    #   Inputs: (self) | Output: "ID: 0, Description: Vibe Check"
    #   Function History:
    #       2020-11-02: Created by Rohit
    ############################################################################
    def __str__(self):
        return f"ID: {self.i_TestId}, Description: {self.s_TestDesc}"


class Experiment(models.Model):
    i_ExperimentId          = models.IntegerField(default=0)
    s_ExperimentName        = models.CharField(max_length=200, default="Default Experiment")
    i_IterationNo           = models.IntegerField(default=0)
    d_Date                  = models.DateTimeField('Trial Date')
    m_TestConfiguration     = models.ForeignKey(TestConfiguration, on_delete=models.CASCADE)
    s_ResultsFile           = models.CharField(max_length=100, default="SampleTest.csv")
    s_EmailAddress          = models.CharField(max_length=100, default='IvanovFTU2020@gmail.com')
    ############################################################################
    #   Function Name: save
    #   Function Description: Checks inputs before saving
    #   Inputs: (self) | Output: either ValueError or a saved object
    #   Function History:
    #       2020-11-09: Created by Rohit
    ############################################################################
    def save(self, *args, **kwargs):
        # Check i_ExperimentId uniqueness
        try:
            b_ExperimentIdIsUnique = False
            exp = Experiment.objects.get(i_ExperimentId = self.i_ExperimentId)
        except Exception as e:
            if type(e) == self.DoesNotExist:
                # No object was found with this unique
                b_ExperimentIdIsUnique = True

        if b_ExperimentIdIsUnique == False:
            raise ValueError(f"Experiment ID: {self.i_ExperimentId} is already in use")

        if self.i_ExperimentId < 0:
            raise ValueError(f"Experiment ID: {self.i_ExperimentId} is invalid. (ID must be a positive integer)")

        super().save(*args, **kwargs)
    ############################################################################
    #   Function Name: ___str___
    #   Function Description: Returns the objects identity string
    #   Inputs: (self) | Output: "ID: 0, (04/19/1999) Name: Vibe Check"
    #   Function History:
    #       2020-11-02: Created by Rohit
    ############################################################################
    def __str__(self):
        return f"ID: {self.i_ExperimentId}, ({str(self.d_Date.month)}/{str(self.d_Date.day)}/{str(self.d_Date.year)}) Name: {self.s_ExperimentName}"

class Result(models.Model):
    # Pre-defined variables
    i_ColumnIdx     = 0
    # User defined variables
    s_FileName              = models.CharField(max_length=200, default="SampleTest.csv")
    ############################################################################
    #   Function Name: save
    #   Function Description: Checks inputs before saving
    #   Inputs: (self) | Output: either ValueError or a saved object
    #   Function History:
    #       2020-11-08: Created by Rohit
    ############################################################################
    def save(self, *args, **kwargs):
        # Reset the column index whenever we save
        i_ColumnIdx = 0
        # TODO: Add a uniqueness check here to ensure you can't create a duplicate
        #       model (blocked until SampleTest simulations are resolved)
        super().save(*args, **kwargs)
    ############################################################################
    #   Function Name: LoadResultsFilepath
    #   Function Description: Returns the associated csv file's path
    #   Inputs: (self) | Output: './DataCollection/TestResults/SampleTest.csv'
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def LoadResultsFilepath(self):
        s_FilePath = os.path.join(settings.MEDIA_ROOT, './DataCollection/TestResults/' + self.s_FileName)
        if os.path.exists(s_FilePath):
            return s_FilePath
        else:
            return -1
    ############################################################################
    #   Function Name: LoadResultsAsMatrix
    #   Function Description: Returns a matrix of the experiments findings
    #   Inputs: (self) | Output: M_data
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def LoadResultsAsMatrix(self):
        s_csvFilePath   = self.LoadResultsFilepath()
        M_data          = np.genfromtxt(s_csvFilePath, delimiter=',', dtype=None, encoding='utf8')
        return M_data
    ############################################################################
    #   Function Name: GetColumnByIndex
    #   Function Description: Returns the nth column of the matrix
    #                           The nth column is assigned by m_Result.i_ColumnIdx
    #   Inputs: (self) | all rows of the ith column
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def GetColumnByIndex(self):
        M_data = self.LoadResultsAsMatrix()
        return M_data[:,self.i_ColumnIdx]

    ############################################################################
    #   Function Name: ___str___
    #   Function Description: Returns the objects identity string
    #   Inputs: (self) | Output: "SampleTest.csv"
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def __str__(self):
        return f"{self.s_FileName}"
