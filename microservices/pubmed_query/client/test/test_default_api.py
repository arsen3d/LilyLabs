# coding: utf-8

"""
    Pubmed Query API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pubmed_query_microservice.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_get_running_jobs_jobs_running_get(self) -> None:
        """Test case for get_running_jobs_jobs_running_get

        Get Running Jobs
        """
        pass

    def test_is_job_running_job_job_id_is_running_get(self) -> None:
        """Test case for is_job_running_job_job_id_is_running_get

        Is Job Running
        """
        pass

    def test_search_search_pubmed_articles_post(self) -> None:
        """Test case for search_search_pubmed_articles_post

        Search
        """
        pass


if __name__ == '__main__':
    unittest.main()
