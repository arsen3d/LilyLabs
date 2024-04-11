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

from nolabs_microservice.models.job_meta_data import JobMetaData

class TestJobMetaData(unittest.TestCase):
    """JobMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobMetaData:
        """Test JobMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobMetaData`
        """
        model = JobMetaData()
        if include_optional:
            return JobMetaData(
                experiment_id = None,
                job_id = None,
                target_id = None,
                ligand_id = None,
                folding_method = None,
                docking_method = None
            )
        else:
            return JobMetaData(
                experiment_id = None,
                job_id = None,
                target_id = None,
                ligand_id = None,
                folding_method = None,
                docking_method = None,
        )
        """

    def testJobMetaData(self):
        """Test JobMetaData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
