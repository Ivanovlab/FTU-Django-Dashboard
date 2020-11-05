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

# Class Definitions-------------------------------------------------------------
class TestConfiguration(models.Model):
    i_TestId            = models.IntegerField(default=0)
    s_TestDesc          = models.CharField(max_length=200, default="Default Test")
    i_DesiredTemp       = models.IntegerField(default=0)
    i_DesiredVoltage    = models.IntegerField(default=0)
    i_DesiredTestTime   = models.IntegerField(default=0)
    i_DesiredField      = models.IntegerField(default=0)
    i_DesiredSerialRate = models.IntegerField(default=0)
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
    s_ExperimentName        = models.CharField(max_length=200, default="Default Experiment")
    i_ExperimentId          = models.IntegerField(default=0)
    d_Date                  = models.DateTimeField('Trial Date')
    m_TestConfigurations    = models.ForeignKey(TestConfiguration, on_delete=models.CASCADE)
    s_ResultsFile           = models.CharField(max_length=100, default="SampleTest.csv")
    s_EmailAddress          = models.CharField(max_length=100, default='IvanovFTU2020@gmail.com')
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
    s_FileName              = models.CharField(max_length=200, default="SampleTest.csv")
    ############################################################################
    #   Function Name: LoadResultsFilepath
    #   Function Description: Returns the associated csv file's path
    #   Inputs: (self) | Output: './DataCollection/TestResults/SampleTest.csv'
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def LoadResultsFilepath(self):
        s_FilePath = os.path.join(settings.MEDIA_ROOT, './DataCollection/TestResults/' + self.s_FileName)
        print(f"TEST: File Path Exists: {s_FilePath}")
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
    #   Function Name: LoadArrayByIndex
    #   Function Description: Returns the nth column of the matrix
    #   Inputs: (self), i | all rows of the ith column
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def LoadArrayByIndex(self, index):
        M_data = self.LoadArrayByIndex()
        return M_data[:,index]
    ############################################################################
    #   Function Name: ___str___
    #   Function Description: Returns the objects identity string
    #   Inputs: (self) | Output: "SampleTest.csv"
    #   Function History:
    #       2020-11-05: Created by Rohit
    ############################################################################
    def __str__(self):
        return f"{self.s_FileName}"
