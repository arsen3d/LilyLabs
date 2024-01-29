import glob
import json
import os.path
import pathlib
from io import BytesIO
from typing import List

from fastapi import UploadFile
from slugify import slugify

from nolabs.api_models.folding import RunFoldingRequest, AminoAcidResponse
from nolabs.domain.experiment import ExperimentId
from nolabs.exceptions import NoLabsException, ErrorCodes
from nolabs.features.file_magement_base import ExperimentsFileManagementBase
from nolabs.infrastructure.settings import Settings


class FileManagement(ExperimentsFileManagementBase):
    def __init__(self, settings: Settings):
        super().__init__(settings.folding_experiments_folder, settings.folding_metadata_file_name)
        self._settings = settings
        self.ensure_experiments_folder_exists()
        self._experiment_properties_filename = 'properties.json'

    async def get_properties(self, experiment_id: ExperimentId) -> RunFoldingRequest:
        experiment_folder = self.experiment_folder(experiment_id)
        metadata = self.get_metadata(experiment_id=experiment_id)

        properties_path = os.path.join(experiment_folder, self._experiment_properties_filename)

        sequence: str | None = None

        if os.path.exists(properties_path):
            with open(properties_path, 'r') as f:
                sequence = json.load(f)['sequence']

        fastas = [
            UploadFile(
                BytesIO(open(fasta_path, 'rb').read()),
                filename=pathlib.Path(fasta_path).name
            ) for fasta_path in glob.glob(os.path.join(experiment_folder, '*.fasta'))
        ]

        return RunFoldingRequest(
            experiment_id=experiment_id.value,
            experiment_name=metadata.name.value,
            amino_acid_sequence=sequence,
            fastas=fastas
        )

    async def set_properties(self, experiment_id: ExperimentId, request: RunFoldingRequest):
        experiment_folder = self.experiment_folder(experiment_id)

        if request.amino_acid_sequence:
            properties_path = os.path.join(experiment_folder, self._experiment_properties_filename)
            with open(properties_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'sequence': request.amino_acid_sequence
                }, f, ensure_ascii=False, indent=4)

        if request.fastas:
            for fasta in request.fastas:
                if not fasta.filename:
                    raise NoLabsException(['Cannot obtain name of fasta file'],
                                          ErrorCodes.amino_acid_localisation_run_error)
                fasta_content = await fasta.read()
                with open(os.path.join(experiment_folder, fasta.filename), 'wb') as f:
                    f.write(fasta_content)
                await fasta.seek(0)

    def set_result(self, experiment_id: ExperimentId, data: List[AminoAcidResponse]):
        experiment_folder = self.experiment_folder(experiment_id)
        previous_files = glob.glob(os.path.join(experiment_folder, '*aminoacid.json'))
        for amino_acid in data:
            results_path = os.path.join(experiment_folder, f'{slugify(amino_acid.name)}_aminoacid.json')
            pdb_file = os.path.join(experiment_folder, amino_acid.pdb_file_name)
            with open(pdb_file, 'w') as f:
                f.write(amino_acid.pdb_file)
            with open(results_path, 'w', encoding='utf-8') as localisation_f:
                localisation_f.write(json.dumps({
                    'name': amino_acid.name,
                    'sequence': amino_acid.sequence,
                    'file_name': amino_acid.pdb_file_name
                }))
        for file in previous_files:
            os.remove(file)

    def get_result(self, experiment_id: ExperimentId) -> List[AminoAcidResponse]:
        experiment_folder = self.experiment_folder(experiment_id)

        results = []
        for file in glob.glob(os.path.join(experiment_folder, '*_aminoacid.json')):
            with open(file, 'r', encoding='utf-8') as amino_acid:
                j = json.loads(amino_acid.read())
                with open(os.path.join(experiment_folder, j['file_name']), 'r', encoding='utf-8') as f:
                    pdb_content = f.read()
                results.append(AminoAcidResponse(name=j['name'],
                                                 sequence=j['sequence'],
                                                 pdb_file=pdb_content,
                                                 pdb_file_name=j['file_name']
                                                 )
                               )
        return results
