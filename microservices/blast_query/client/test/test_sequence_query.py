# coding: utf-8

"""
    BLAST Query

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from blast_query_microservice.models.sequence_query import SequenceQuery

class TestSequenceQuery(unittest.TestCase):
    """SequenceQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SequenceQuery:
        """Test SequenceQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SequenceQuery`
        """
        model = SequenceQuery()
        if include_optional:
            return SequenceQuery(
                sequence = '',
                type = 'blastn',
                descriptions = 56,
                alignments = 56,
                hitlist_size = 56,
                expect = 1.337
            )
        else:
            return SequenceQuery(
                sequence = '',
                type = 'blastn',
        )
        """

    def testSequenceQuery(self):
        """Test SequenceQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
