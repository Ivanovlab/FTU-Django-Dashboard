##################################
#   File Name: models.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file defines models used
#       in our database
#
#   File History:
#   2020-11-02: Created by Rohit
#
##################################
# Imports ---------------------------------------------
from django.db import models
from django.conf import settings
import numpy as np
import os

# Class Definitions
class TestConfiguration(models.Model):
    i_TestId            = models.IntegerField(default=0)
    s_TestDesc          = models.CharField(max_length=200, default="Default Test")
    i_DesiredTemp       = models.IntegerField(default=0)
    i_DesiredVoltage    = models.IntegerField(default=0)
    i_DesiredTestTime   = models.IntegerField(default=0)
    i_DesiredField      = models.IntegerField(default=0)
    i_DesiredSerialRate = models.IntegerField(default=0)
    def __str__(self):
        return f"ID: {self.i_TestId}, Description: {self.s_TestDesc}"

class Experiment(models.Model):
    s_ExperimentName        = models.CharField(max_length=200, default="Default Experiment")
    i_ExperimentId          = models.IntegerField(default=0)
    d_Date                  = models.DateTimeField('Trial Date')
    m_TestConfigurations    = models.ForeignKey(TestConfiguration, on_delete=models.CASCADE)
    s_ResultsFile           = models.CharField(max_length=100, default="SampleTest.csv")
    s_EmailAddress          = models.CharField(max_length=100, default='IvanovFTU2020@gmail.com')
    def __str__(self):
        return f"ID: {self.i_ExperimentId}, ({str(self.d_Date.month)}/{str(self.d_Date.day)}/{str(self.d_Date.year)}) Name: {self.s_ExperimentName}"

class Result(models.Model):
    s_FileName              = models.CharField(max_length=200, default="SampleTest.csv")
    def LoadResultsFilepath(self):
        s_FilePath = os.path.join(settings.MEDIA_ROOT, './DataCollection/TestResults/' + self.s_FileName)
        print(f"TEST: File Path Exists: {s_FilePath}")
        if os.path.exists(s_FilePath):
            return s_FilePath
        else:
            return -1
    def LoadResultsAsMatrix(self):
        s_csvFilePath   = self.LoadResultsFilepath()
        M_data          = np.genfromtxt(s_csvFilePath, delimiter=',', dtype=None, encoding='utf8')
        return M_data

    def LoadArrayByIndex(self, index):
        M_data = self.LoadArrayByIndex()
        return M_data[:,index]

    def __str__(self):
        return f"{self.s_FileName}"
