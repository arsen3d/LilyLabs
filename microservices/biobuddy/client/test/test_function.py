# coding: utf-8

"""
    Bio Buddy

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from biobuddy_microservice.models.function import Function

class TestFunction(unittest.TestCase):
    """Function unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Function:
        """Test Function
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Function`
        """
        model = Function()
        if include_optional:
            return Function(
                arguments = '',
                name = ''
            )
        else:
            return Function(
                arguments = '',
                name = '',
        )
        """

    def testFunction(self):
        """Test Function"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
