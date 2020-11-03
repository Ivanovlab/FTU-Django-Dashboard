##################################
#   File Name: urls.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file maps our views to
#     their respective urls
#
#   File History:
#   2020-11-02: Created by Rohit
#
##################################
# Imports ------------------------
from django.urls import path
from . import views

# Definitions --------------------
app_name = 'DataCollection'
urlpatterns = [
    path('', views.index, name='index'),
    path('NewExperiment/', views.NewExperiment, name="NewExperiment"),
    path('CreateNewTestConfiguration/', views.CreateNewTestConfiguration, name="CreateNewTestConfiguration"),
    path('TestConfigurations/', views.TestConfigurations, name="TestConfigurations"),
    path('ExperimentHistory/',  views.ExperimentHistory, name="ExperimentHistory"),
    path('ExperimentDetail/<int:experiment_id>/', views.ExperimentDetail, name="ExperimentDetail"),
]
