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

from nolabs_microservice.models.check_folding_data_available_response import CheckFoldingDataAvailableResponse

class TestCheckFoldingDataAvailableResponse(unittest.TestCase):
    """CheckFoldingDataAvailableResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckFoldingDataAvailableResponse:
        """Test CheckFoldingDataAvailableResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckFoldingDataAvailableResponse`
        """
        model = CheckFoldingDataAvailableResponse()
        if include_optional:
            return CheckFoldingDataAvailableResponse(
                is_available = None
            )
        else:
            return CheckFoldingDataAvailableResponse(
                is_available = None,
        )
        """

    def testCheckFoldingDataAvailableResponse(self):
        """Test CheckFoldingDataAvailableResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
