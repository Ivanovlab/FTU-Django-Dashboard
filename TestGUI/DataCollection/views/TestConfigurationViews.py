###############################################################################
#   File Name: views.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file routes our views
#     to the backend
#
#   File History:
#   2020-11-02: Created by Rohit
#
###############################################################################
# Imports ----------------------------------------------------------------------
# Django Libraries
from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse, Http404
# Local Imports
from .models import TestConfiguration, Experiment
# Python Libraries
import os
import csv
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib
# ..... TestConfigurations .....................................................
################################################################################
#   Function Name: TestConfigurations
#   Function Author: Rohit
#   Function Description: Renders the TestConfigurations page
#   Inputs: request | Outputs: TestConfigurations.html {ctx}
################################################################################
def TestConfigurations(request):
    l_TestConfigurations = TestConfiguration.objects.all()
    context = {
        'l_TestConfigurations': l_TestConfigurations,
    }
    return render(request, 'DataCollection/TestConfigurations.html', context)
################################################################################
#   Function Name: CreateNewTestConfiguration
#   Function Author: Rohit
#   Function Description: Creates new TestConfiguration and loads
#                           TestConfigurations page again
#   Inputs: request | Outputs: TestConfigurations.html {ctx}
################################################################################
def CreateNewTestConfiguration(request):
    # Create our new base TestConfiguration object
    t = TestConfiguration()
    # The form data is accessed by request.POST.get()
    t.i_TestId          = int(request.POST.get('i_TestId'))
    t.s_TestDesc        = request.POST.get('s_TestDesc')
    t.i_DesiredTemp     = int(request.POST.get('i_DesiredTemp'))
    t.i_DesiredVoltage  = int(request.POST.get('i_DesiredVoltage'))
    t.i_DesiredTestTime = int(request.POST.get('i_DesiredTestTime'))
    t.i_DesiredField    = int(request.POST.get('i_DesiredField'))
    t.i_DesiredSerialRate = int(request.POST.get('i_DesiredSerialRate'))
    # Save our new form
    t.save()
    l_TestConfigurations = TestConfiguration.objects.all()
    context = {
        'l_TestConfigurations': l_TestConfigurations,
    }
    # Redirect
    return redirect('/DataCollection/TestConfigurations')

################################################################################
#   Function Name: TestConfigurationDetail
#   Function Author: Rohit
#   Function Description: Renders TestConfigurationDetail.html
#   Inputs: request | Outputs: TestConfigurationDetail.html {ctx}
################################################################################
def TestConfigurationDetail(request, i_TestId):
    # Get tc by Id
    tc = TestConfiguration.objects.get(i_TestId = i_TestId)
    l_experiments = tc.experiment_set.all()
    ctx = {
        'tc': tc,
        'l_experiments': l_experiments,
    }
    return render(request, 'DataCollection/TestConfigurationDetail.html', ctx)
