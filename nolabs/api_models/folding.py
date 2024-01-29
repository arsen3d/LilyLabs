from pydantic import dataclasses as pcdataclass, model_validator
import datetime
from typing import List, Optional, Any

from fastapi import UploadFile, File

from nolabs.api_models.experiment import ExperimentMetadataResponse


@pcdataclass.dataclass
class RunFoldingRequest:
    experiment_name: str
    experiment_id: str
    amino_acid_sequence: Optional[str]
    fastas: Optional[List[UploadFile]]

    @model_validator(mode='after')
    @classmethod
    def check_inputs(cls, data: Any) -> Any:
        if not isinstance(data, RunFoldingRequest):
            raise ValueError('Incorrect data type')
        if not data.amino_acid_sequence and not data.fastas:
            raise ValueError('Either specify aminoacid sequence or fastas files')
        return data


@pcdataclass.dataclass
class AminoAcidResponse:
    sequence: str
    name: str
    pdb_file_name: str
    pdb_file: str


@pcdataclass.dataclass
class RunFoldingResponse:
    experiment_id: str
    experiment_name: str
    amino_acids: List[AminoAcidResponse]


@pcdataclass.dataclass
class ExperimentFastaPropertyResponse:
    filename: str
    content: str


@pcdataclass.dataclass
class ExperimentPropertiesResponse:
    amino_acid_sequence: str | None
    fastas: List[ExperimentFastaPropertyResponse]


@pcdataclass.dataclass
class GetExperimentResponse:
    experiment_id: str
    experiment_name: str
    amino_acids: List[AminoAcidResponse]
    properties: ExperimentPropertiesResponse
