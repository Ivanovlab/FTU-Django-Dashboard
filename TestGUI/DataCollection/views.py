##################################
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
##################################
# Imports ----------------------------------------------------------------------
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import TestConfiguration, Experiment
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
# Index Functions --------------------------------------------------------------
#################################
#   Function Name: index
#   Function Author: Rohit
#   Function Description: Renders the index page
#   Inputs: request | Outputs: index.html {ctx}
#################################
def index(request):
    return render(request, 'DataCollection/index.html')
# Sub-Menu Functions -----------------------------------------------------------
# ..... TestConfigurations .....................................................
#################################
#   Function Name: TestConfigurations
#   Function Author: Rohit
#   Function Description: Renders the TestConfigurations page
#   Inputs: request | Outputs: TestConfigurations.html {ctx}
#################################
def TestConfigurations(request):
    l_TestConfigurations = TestConfiguration.objects.all()
    context = {
        'l_TestConfigurations': l_TestConfigurations,
    }
    return render(request, 'DataCollection/TestConfigurations.html', context)
#################################
#   Function Name: CreateNewTestConfiguration
#   Function Author: Rohit
#   Function Description: Creates new TestConfiguration and loads
#                           TestConfigurations page again
#   Inputs: request | Outputs: TestConfigurations.html {ctx}
#################################
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

#################################
#   Function Name: TestConfigurationDetail
#   Function Author: Rohit
#   Function Description: Renders TestConfigurationDetail.html
#   Inputs: request | Outputs: TestConfigurationDetail.html {ctx}
#################################
def TestConfigurationDetail(request, i_TestId):
    # Get tc by Id
    tc = TestConfiguration.objects.get(i_TestId = i_TestId)
    l_experiments = tc.experiment_set.all()
    ctx = {
        'tc': tc,
        'l_experiments': l_experiments,
    }
    return render(request, 'DataCollection/TestConfigurationDetail.html', ctx)

# ..... Experiments ............................................................
#################################
#   Function Name: Experiments
#   Function Author: Rohit
#   Function Description: Renders the Experiments page
#   Inputs: request | Outputs: Experiments.html {ctx}
#################################
def Experiments(request):
    l_Experiments = Experiment.objects.all()
    l_TestConfigurations = TestConfiguration.objects.all()
    context = {
        'l_Experiments': l_Experiments,
        'l_TestConfigurations': l_TestConfigurations,
    }
    return render(request, 'DataCollection/Experiments.html', context)
#################################
#   Function Name: CreateNewExperiment
#   Function Author: Rohit
#   Function Description: Creates new Experiment and loads
#                           Experiments page again
#   Inputs: request | Outputs: experiments.html {ctx}
#################################
def CreateNewExperiment(request):
    # Create our new base Experiment object
    exp = Experiment()
    # The form data is accessed by request.POST.get()
    exp.s_ExperimentName    = request.POST.get('s_ExperimentName')
    exp.i_ExperimentId      = int(request.POST.get('i_ExperimentId'))
    exp.d_Date              = timezone.now()
    testConfigId = request.POST.get('m_TestConfigurations')
    exp.m_TestConfigurations= TestConfiguration.objects.get(pk=testConfigId)
    exp.s_ResultsFile = request.POST.get('s_ResultsFile')
    # save created object
    exp.save()
    # Redirect
    return redirect('/DataCollection/Experiments')

#################################
#   Function Name: ExperimentDetail
#   Function Author: Rohit
#   Function Description: Renders ExperimentDetail.html
#   Inputs: request | Outputs: ExperimentDetail.html {ctx}
#################################
def ExperimentDetail(request, experiment_id):
    # Get Experiment by Id
    experiment = Experiment.objects.get(i_ExperimentId = int(experiment_id))
    # Get Experiments test configuration
    tc = experiment.m_TestConfigurations
    ctx = {
        'experiment': experiment,
        'tc': tc,
    }
    return render(request, 'DataCollection/ExperimentDetail.html', ctx)

#################################
#   Function Name: DownloadResults
#   Function Author: Rohit
#   Function Description: Downloads .csv file
#   Inputs: request | Outputs: .csv file
#################################
def DownloadResults(request, s_ResultsFile):
    s_FilePath = './DataCollection/TestResults/' + s_ResultsFile
    filePath = os.path.join(settings.MEDIA_ROOT, s_FilePath)
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filePath)
            return response
    raise Http404

###############################################################################
#   Function Name: GeneratePlot
#   Function Author: Rohit
#   Function Description:   Creates plot from csv data
#                           Saves plot in TestResults
#                           Downloads plot from window
#
#   Inputs: request, s_ResultsFile | Outputs: plot.png
#
#   History:
#       2020-11-03: Sliding Window Measurements added
#       2020-11-02: Created by Rohit
################################################################################
# TODO: If the path doesn't exist, give the user an error
# TODO: Add more error case handling
def GeneratePlot(request, s_ResultsFile):
    # Retrieve Data from the form
    s_XValuesLabel  = request.POST.get('s_XValuesLabel')
    s_YValuesLabel  = request.POST.get('s_YValuesLabel')
    i_StartTime     = request.POST.get('i_StartTime')
    i_EndTime       = request.POST.get('i_EndTime')
    # TODO: Fix this logic
    b_spliceData = not (i_StartTime == i_EndTime)
    if b_spliceData:
        i_StartTimeIdx  = -1
        i_EndTimeIdx    = -1
    # Create file path
    s_FilePath = './DataCollection/TestResults/' + s_ResultsFile
    filePath = os.path.join(settings.MEDIA_ROOT, s_FilePath)
    # Verify the files existence
    if os.path.exists(filePath):
        # Create a matrix from the .csv file
        X = np.genfromtxt(filePath, delimiter=',', dtype=None, encoding='utf8')
        # Create arrays to store data in
        a_XValues = []
        a_YValues = []
        # Fill the arrays by iterating over the rows
        for i in range(1, len(X)):
            a_XValues.append(float(X[i, int(s_XValuesLabel)]))
            a_YValues.append(float(X[i, int(s_YValuesLabel)]))
            # If user wants to splice their data, find the bounds
            if b_spliceData:
                # Find index for start / end times
                if float(X[i, 1]) > float(i_StartTime) and i_StartTimeIdx == -1:
                    i_StartTimeIdx = i
                if float(X[i, 1]) > float(i_EndTime) and i_EndTimeIdx == -1:
                    i_EndTimeIdx = i
        # Clear any previously saved plot info
        plt.cla()
        # If the user doesn't want their data spliced, don't!
        if b_spliceData == False:
            plt.plot(a_XValues, a_YValues)
        # Else if the user does want their data spliced, do it!
        else:
            plt.plot(a_XValues[i_StartTimeIdx:i_EndTimeIdx], a_YValues[i_StartTimeIdx:i_EndTimeIdx])
        # Decorate our plot
        plt.title(f"{X[0, int(s_YValuesLabel)]} as a function of {X[0, int(s_XValuesLabel)]}")
        plt.xlabel(f"{X[0, int(s_XValuesLabel)]}")
        plt.ylabel(f"{X[0, int(s_YValuesLabel)]}")
        plt.grid()
        # Save the plot to figures directory and download it from there
        s_FilePath = './DataCollection/TestResults/Figures/Save.png'
        filePath = os.path.join(settings.MEDIA_ROOT, s_FilePath)
        plt.savefig(filePath)
        if os.path.exists(filePath):
            with open(filePath, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filePath)
                return response
    # Otherwise get redirected
    return redirect('/DataCollection/Experiments')
