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

from nolabs_microservice.models.get_results_list_for_target_ligand_response import GetResultsListForTargetLigandResponse

class TestGetResultsListForTargetLigandResponse(unittest.TestCase):
    """GetResultsListForTargetLigandResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResultsListForTargetLigandResponse:
        """Test GetResultsListForTargetLigandResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResultsListForTargetLigandResponse`
        """
        model = GetResultsListForTargetLigandResponse()
        if include_optional:
            return GetResultsListForTargetLigandResponse(
                results_list = None
            )
        else:
            return GetResultsListForTargetLigandResponse(
                results_list = None,
        )
        """

    def testGetResultsListForTargetLigandResponse(self):
        """Test GetResultsListForTargetLigandResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
