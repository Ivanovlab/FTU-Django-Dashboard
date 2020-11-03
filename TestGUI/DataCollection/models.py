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

# Class Definitions
class TestConfiguration(models.Model):
    s_TestId            = models.CharField(max_length=200, default="Corrupt")
    s_TestDesc          = models.CharField(max_length=200)
    i_DesiredTemp       = models.IntegerField(default=0)
    i_DesiredVoltage    = models.IntegerField(default=0)
    i_DesiredTestTime   = models.IntegerField(default=0)
    i_DesiredField      = models.IntegerField(default=0)
    i_DesiredSerialRate = models.IntegerField(default=0)
    def __str__(self):
        return f"ID: {self.s_TestId}, Description: {self.s_TestDesc}"

class Experiment(models.Model):
    s_ExperimentName        = models.CharField(max_length=200, default="Random")
    s_ExperimentId          = models.CharField(max_length=200)
    d_Date                  = models.DateTimeField('Trial Date')
    m_TestConfigurations    = models.ForeignKey(TestConfiguration, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.s_ExperimentName}"
