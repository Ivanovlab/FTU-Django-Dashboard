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
    # Index Path
    path('', views.index, name='index'),
    # TestConfigurations
    path('CreateNewTestConfiguration/', views.CreateNewTestConfiguration, name="CreateNewTestConfiguration"),
    path('TestConfigurations/', views.TestConfigurations, name="TestConfigurations"),
    path('TestConfiguationDetail/<int:i_TestId>', views.TestConfigurationDetail, name="TestConfiguationDetail"),
    # Experiments
    path('Experiments/', views.Experiments, name="Experiments"),
    path('CreateNewExperiment/', views.CreateNewExperiment, name="CreateNewExperiment"),
    path('ExperimentDetail/<int:experiment_id>', views.ExperimentDetail, name="ExperimentDetail"),
    path('DownloadResults/<str:s_ResultsFile>', views.DownloadResults, name="DownloadResults"),
    path('GeneratePlot/<str:s_ResultsFile>', views.GeneratePlot, name="GeneratePlot"),
]
