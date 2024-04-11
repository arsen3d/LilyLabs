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

from nolabs_microservice.models.nolabs_api_models_small_molecules_design_get_experiment_response import NolabsApiModelsSmallMoleculesDesignGetExperimentResponse

class TestNolabsApiModelsSmallMoleculesDesignGetExperimentResponse(unittest.TestCase):
    """NolabsApiModelsSmallMoleculesDesignGetExperimentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NolabsApiModelsSmallMoleculesDesignGetExperimentResponse:
        """Test NolabsApiModelsSmallMoleculesDesignGetExperimentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NolabsApiModelsSmallMoleculesDesignGetExperimentResponse`
        """
        model = NolabsApiModelsSmallMoleculesDesignGetExperimentResponse()
        if include_optional:
            return NolabsApiModelsSmallMoleculesDesignGetExperimentResponse(
                experiment_id = None,
                experiment_name = None,
                created_at = None,
                status = nolabs_microservice.models.get_experiment_status_response.GetExperimentStatusResponse(
                    running = null, 
                    sampling_allowed = null, ),
                properties = nolabs_microservice.models.experiment_properties_response.ExperimentPropertiesResponse(
                    center_x = null, 
                    center_y = null, 
                    center_z = null, 
                    size_x = null, 
                    size_y = null, 
                    size_z = null, 
                    batch_size = null, 
                    minscore = null, 
                    epochs = null, 
                    pdb_file = null, 
                    pdb_file_name = null, )
            )
        else:
            return NolabsApiModelsSmallMoleculesDesignGetExperimentResponse(
                experiment_id = None,
                experiment_name = None,
                created_at = None,
                status = nolabs_microservice.models.get_experiment_status_response.GetExperimentStatusResponse(
                    running = null, 
                    sampling_allowed = null, ),
                properties = nolabs_microservice.models.experiment_properties_response.ExperimentPropertiesResponse(
                    center_x = null, 
                    center_y = null, 
                    center_z = null, 
                    size_x = null, 
                    size_y = null, 
                    size_z = null, 
                    batch_size = null, 
                    minscore = null, 
                    epochs = null, 
                    pdb_file = null, 
                    pdb_file_name = null, ),
        )
        """

    def testNolabsApiModelsSmallMoleculesDesignGetExperimentResponse(self):
        """Test NolabsApiModelsSmallMoleculesDesignGetExperimentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
