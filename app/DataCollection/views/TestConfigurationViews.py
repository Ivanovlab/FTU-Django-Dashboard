###############################################################################
#   File Name: TestConfigurationViews.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file routes our test configuration views
#     to the backend
#
#   File History:
#   2020-11-05: TestConfigurationViews.py created from old views.py
#   2020-11-02: (views.py) Created by Rohit
#
###############################################################################
# Imports ---------------------------------------------------------------------
# Django Libraries
from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
# Local Imports
from ..models import TestConfiguration, Experiment


# ..... TestConfigurations .....................................................
################################################################################
#   Function Name: TestConfigurations
#   Function Author: Rohit
#   Function Description: Renders the TestConfigurations page
#   Inputs: request | Outputs: TestConfigurations.html {ctx}
################################################################################
def TestConfigurations(request):
    # Create an empty TestConfiguration object to access constants in HTMl
    tc = TestConfiguration()
    l_TestConfigurations = TestConfiguration.objects.all()
    s_Error = "None"
    b_Saved = False
    context = {
        'l_TestConfigurations': l_TestConfigurations,
        's_Error': s_Error,
        'b_Saved': b_Saved,
        'tc': tc
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
    # Create an empty TestConfiguration object to access constants in HTML
    tc = TestConfiguration()
    # Create our new base TestConfiguration object
    t = TestConfiguration()
    # The form data is accessed by request.POST.get()
    try:
        t.i_TestId = int(request.POST.get('i_TestId'))
        t.s_TestDesc = request.POST.get('s_TestDesc')
        t.i_DesiredTemp = int(request.POST.get('i_DesiredTemp'))
        t.i_DesiredVoltage = int(request.POST.get('i_DesiredVoltage'))
        t.i_DesiredTestTime = int(request.POST.get('i_DesiredTestTime'))
        t.i_DesiredField = int(request.POST.get('i_DesiredField'))
        t.i_DesiredSerialRate = int(request.POST.get('i_DesiredSerialRate'))
        # Save our new form
        t.save()
        s_Error = "None"
        b_Saved = True
    except Exception as e:
        s_Error = str(e)
        if s_Error == "invalid literal for int() with base 10: ''":
            s_Error = "Please enter a value for all fields"
        b_Saved = False
    l_TestConfigurations = TestConfiguration.objects.all()

    context = {
        'l_TestConfigurations': l_TestConfigurations,
        's_Error': s_Error,
        'b_Saved': b_Saved,
        'tc': tc,
    }
    return render(request, 'DataCollection/TestConfigurations.html', context)


################################################################################
#   Function Name: TestConfigurationDetail
#   Function Author: Rohit
#   Function Description: Renders TestConfigurationDetail.html
#   Inputs: request | Outputs: TestConfigurationDetail.html {ctx}
################################################################################
def TestConfigurationDetail(request, i_TestId):
    # Get tc by Id
    tc = TestConfiguration.objects.get(i_TestId=i_TestId)
    l_experiments = tc.experiment_set.all()
    ctx = {
        'tc': tc,
        'l_experiments': l_experiments,
    }
    return render(request, 'DataCollection/TestConfigurationDetail.html', ctx)


################################################################################
#   Function Name: SendSerialData
#   Function Author: Rohit
#   Function Description: Sends serial data
#   Inputs: request | Outputs: TestConfigurationDetail.html {ctx}
################################################################################
def SendSerialData(request, i_TestId):
    # Get TC by id
    tc = TestConfiguration.objects.get(i_TestId=i_TestId)
    # Get the JSON instruction string
    tc.SendJsonInstructions()
    l_experiments = tc.experiment_set.all()
    ctx = {
        'tc': tc,
        'l_experiments': l_experiments,
    }
    return render(request, 'DataCollection/TestConfigurationDetail.html', ctx)
