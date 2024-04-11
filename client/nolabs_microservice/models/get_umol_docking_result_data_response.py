# coding: utf-8

"""
    NoLabs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetUmolDockingResultDataResponse(BaseModel):
    """
    GetUmolDockingResultDataResponse
    """ # noqa: E501
    predicted_pdb: Optional[Any]
    predicted_sdf: Optional[Any]
    plddt_array: Optional[Any]
    job_id: Optional[Any]
    __properties: ClassVar[List[str]] = ["predicted_pdb", "predicted_sdf", "plddt_array", "job_id"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetUmolDockingResultDataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if predicted_pdb (nullable) is None
        # and model_fields_set contains the field
        if self.predicted_pdb is None and "predicted_pdb" in self.model_fields_set:
            _dict['predicted_pdb'] = None

        # set to None if predicted_sdf (nullable) is None
        # and model_fields_set contains the field
        if self.predicted_sdf is None and "predicted_sdf" in self.model_fields_set:
            _dict['predicted_sdf'] = None

        # set to None if plddt_array (nullable) is None
        # and model_fields_set contains the field
        if self.plddt_array is None and "plddt_array" in self.model_fields_set:
            _dict['plddt_array'] = None

        # set to None if job_id (nullable) is None
        # and model_fields_set contains the field
        if self.job_id is None and "job_id" in self.model_fields_set:
            _dict['job_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetUmolDockingResultDataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "predicted_pdb": obj.get("predicted_pdb"),
            "predicted_sdf": obj.get("predicted_sdf"),
            "plddt_array": obj.get("plddt_array"),
            "job_id": obj.get("job_id")
        })
        return _obj


