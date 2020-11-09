################################################################################
#   File Name: tests.py
#
#   File Author: Rohit Singh
#
#   File Description:
#     This file defines test cases
#
#   File History:
#   2020-11-05: Created by Rohit
#
################################################################################
# Imports ----------------------------------------------------------------------
from django.test import TestCase

from .models import TestConfiguration
# Test Configuration Tests------------------------------------------------------
class TestConfigurationModelTests(TestCase):
    def setUp(self):
        TestConfiguration.objects.create(i_TestId = 0, s_TestDesc = "tc0")
        TestConfiguration.objects.create(i_TestId = 1, s_TestDesc = "tc1")
        ########################################################################
        #       Test Name: test_valid_str
        #       Description:    Creates two items and checks their
        #                       __str__ method works
        #       History:    2020-11-09 - Created by Rohit
        ########################################################################
    def test_valid_str(self):
        tc0     =   TestConfiguration.objects.get(i_TestId=0)
        tc1     =   TestConfiguration.objects.get(i_TestId=1)
        self.assertEqual(str(tc0), "ID: 0, Description: tc0")
        self.assertEqual(str(tc1), "ID: 1, Description: tc1")
        ########################################################################
        #       Test Name: test_invalid_temperature
        #       Description:    tests that specified temperature is valid
        #       History:    2020-11-09 - Created by Rohit
        ########################################################################
    def test_invalid_temperature(self):
        tc0     =   TestConfiguration.objects.get(i_TestId = 0)
        # Test below minimum bound
        try:
            tc0.i_DesiredTemp = tc0.i_MinimumTemperature - 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e),ValueError)
        # Test above maximum bound
        try:
            tc0.i_DesiredTemp = tc0.i_MaximumTemperature + 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e), ValueError)

        ########################################################################
        #       Test Name:      test_invalid_voltage
        #       Description:    tests that specified voltage is valid
        #       History:        2020-11-09 - Created by Rohit
        ########################################################################
    def test_invalid_voltage(self):
        tc0     =   TestConfiguration.objects.get(i_TestId = 0)
        # Test below minimum bound
        try:
            tc0.i_DesiredVoltage = tc0.i_MinimumVoltage - 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e),ValueError)
        # Test above maximum bound
        try:
            tc0.i_DesiredVoltage = tc0.i_MaximumVoltage + 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e), ValueError)

        ########################################################################
        #       Test Name:      test_invalid_field
        #       Description:    tests that specified field is valid
        #       History:        2020-11-09 - Created by Rohit
        ########################################################################
    def test_invalid_field(self):
        tc0     =   TestConfiguration.objects.get(i_TestId = 0)
        # Test below minimum bound
        try:
            tc0.i_DesiredField = tc0.i_MinimumField - 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e),ValueError)
        # Test above maximum bound
        try:
            tc0.i_DesiredField = tc0.i_MaximumField + 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e), ValueError)

        ########################################################################
        #       Test Name:      test_invalid_test_time
        #       Description:    tests that specified test time is valid
        #       History:        2020-11-09 - Created by Rohit
        ########################################################################
    def test_invalid_test_time(self):
        tc0     =   TestConfiguration.objects.get(i_TestId = 0)
        # Test below minimum bound
        try:
            tc0.i_DesiredTestTime = tc0.i_MinimumTestTime - 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e),ValueError)
        # Test above maximum bound
        try:
            tc0.i_DesiredTestTime = tc0.i_MaximumTestTime + 1
            tc0.save()
        except Exception as e:
            self.assertEqual(type(e), ValueError)

        ########################################################################
        #       Test Name:      test_unique_id
        #       Description:    tests that specified test id is valid
        #       History:        2020-11-09 - Created by Rohit
        ########################################################################
    def test_unique_id(self):
        tc0 =   TestConfiguration.objects.get(i_TestId=0)
        tc1 =   TestConfiguration.objects.get(i_TestId=1)

        try:
            tc1.i_TestId = tc0.i_TestId
            tc1.save()
        except Exception as e:
            self.assertEqual(type(e), ValueError)
