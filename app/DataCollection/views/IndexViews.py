#####################################################################
#   File Name: indexViews.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file routes our index views
#     to the backend
#
#   File History:
#   2020-11-05: ExperimentViews.py created from old views.py
#   2020-11-02: (views.py) Created by Rohit
#
######################################################################
# Imports ------------------------------------------------------------
# Django Libraries
from django.shortcuts import render, redirect


######################################################################
#   Function Name: index
#   Function Author: Rohit
#   Function Description: Renders the index page (/)
#   Inputs: request | Outputs: Experiments.html {ctx}
#######################################################################
def index(request):
    return render(request, 'DataCollection/index.html')
