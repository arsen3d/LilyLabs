# coding: utf-8

"""
    NoLabs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nolabs_microservice.models.get_experiment_status_response import GetExperimentStatusResponse

class TestGetExperimentStatusResponse(unittest.TestCase):
    """GetExperimentStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetExperimentStatusResponse:
        """Test GetExperimentStatusResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetExperimentStatusResponse`
        """
        model = GetExperimentStatusResponse()
        if include_optional:
            return GetExperimentStatusResponse(
                running = None,
                sampling_allowed = None
            )
        else:
            return GetExperimentStatusResponse(
                running = None,
                sampling_allowed = None,
        )
        """

    def testGetExperimentStatusResponse(self):
        """Test GetExperimentStatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
