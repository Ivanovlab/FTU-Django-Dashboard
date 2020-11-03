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
from .models import TestConfiguration, Experiment

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
#   Inputs: request | Outputs: index.html {ctx}
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
#   Inputs: request | Outputs: index.html {ctx}
#################################
def CreateNewTestConfiguration(request):
    # Create our new base TestConfiguration object
    t = TestConfiguration()
    # The form data is accessed by request.POST.get()
    t.s_TestId          = request.POST.get('s_TestId')
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




def NewExperiment(request):
    return render(request, 'DataCollection/NewExperiment.html')



def ExperimentHistory(request):
    l_RecentExperiments = Experiment.objects.all()
    context = {
        'l_RecentExperiments': l_RecentExperiments,
    }
    return render(request, 'DataCollection/ExperimentHistory.html', context)

def ExperimentDetail(request, experiment_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    context = {
        'experiment': experiment,
    }
    return render(request, 'DataCollection/ExperimentDetail.html', context)
