import configparser
import os.path
from dataclasses import dataclass

__all__ = ['Settings', ]

from nolabs.infrastructure.environment import is_dev

import configparser
import os


class Settings:
    def __init__(self):
        self._config = configparser.ConfigParser()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        settings_path = 'settings.ini' if is_dev() else 'settings.ini'

        self._config.read(os.path.join(dir_path, settings_path))

    @property
    def is_test(self) -> bool:
        return self._config.getboolean('features', 'test')

    @property
    def is_light_infrastructure(self) -> str:
        return self._config.get('features', 'light')

    @property
    def solubility_host(self) -> str:
        return self._config.get('microservices', 'solubility_host')

    @property
    def conformations_host(self) -> str:
        return self._config.get('microservices', 'conformations_host')

    @property
    def localisation_host(self) -> str:
        return self._config.get('microservices', 'localisation_host')

    @property
    def gene_ontology_host(self) -> str:
        return self._config.get('microservices', 'gene_ontology_host')

    @property
    def conformations_simulations_file_name(self) -> str:
        return self._config.get('conformations', 'file_name')

    @property
    def conformations_experiments_folder(self) -> str:
        import nolabs
        exp_folder = self._config.get('conformations', 'experiments_path')
        return os.path.join(os.path.dirname(nolabs.__file__), exp_folder)

    @property
    def conformations_metadata_file_name(self) -> str:
        return self._config.get('conformations', 'metadata_file_name')

    @property
    def protein_design_file_name(self) -> str:
        return self._config.get('protein-design', 'file_name')

    @property
    def protein_design_experiments_folder(self) -> str:
        import nolabs
        exp_folder = self._config.get('protein-design', 'experiments_path')
        return os.path.join(os.path.dirname(nolabs.__file__), exp_folder)

    @property
    def protein_design_metadata_file_name(self) -> str:
        return self._config.get('protein-design', 'metadata_file_name')

    @property
    def go_file_name(self) -> str:
        return self._config.get('go', 'file_name')

    @property
    def go_experiments_folder(self) -> str:
        import nolabs
        exp_folder = self._config.get('go', 'experiments_path')
        return os.path.join(os.path.dirname(nolabs.__file__), exp_folder)

    @property
    def go_metadata_file_name(self) -> str:
        return self._config.get('go', 'metadata_file_name')

    @property
    def solubility_experiments_folder(self) -> str:
        import nolabs
        exp_folder = self._config.get('solubility', 'experiments_path')
        return os.path.join(os.path.dirname(nolabs.__file__), exp_folder)

    @property
    def solubility_metadata_file_name(self) -> str:
        return self._config.get('solubility', 'metadata_file_name')

    @property
    def drug_discovery_experiments_folder(self):
        import nolabs
        exp_folder = self._config.get('drug-discovery', 'experiments_path')
        return os.path.join(os.path.dirname(nolabs.__file__), exp_folder)

    @property
    def drug_discovery_experiment_metadata_file_name(self) -> str:
        return self._config.get('drug-discovery', 'experiment_metadata_file_name')

    @property
    def drug_discovery_target_metadata_file_name(self) -> str:
        return self._config.get('drug-discovery', 'target_metadata_file_name')

    @property
    def drug_discovery_ligand_metadata_file_name(self) -> str:
        return self._config.get('drug-discovery', 'ligand_metadata_file_name')

    @property
    def drug_discovery_pocket_directory_name(self) -> str:
        return self._config.get('drug-discovery', 'pocket_directory_name')

    @property
    def drug_discovery_pocket_file_name(self) -> str:
        return self._config.get('drug-discovery', 'pocket_file_name')

    @property
    def drug_discovery_self_hosted_msa(self) -> str:
        return self._config.get('drug-discovery', 'self_hosted_msa')

    @property
    def drug_discovery_msa_url(self) -> str:
        return self._config.get('drug-discovery', 'msa_server_url')
    @property
    def drug_discovery_msa_file_name(self) -> str:
        return self._config.get('drug-discovery', 'msa_file_name')

    @property
    def drug_discovery_docking_result_directory_name(self) -> str:
        return self._config.get('drug-discovery', 'docking_result_directory_name')

    @property
    def drug_discovery_docking_result_metadata_filename_name(self) -> str:
        return self._config.get('drug-discovery', 'docking_result_metadata_file_name')

    @property
    def drug_discovery_docking_result_sdf_file_name(self) -> str:
        return self._config.get('drug-discovery', 'docking_result_sdf_file_name')

    @property
    def drug_discovery_docking_result_pdb_file_name(self) -> str:
        return self._config.get('drug-discovery', 'docking_result_pdb_file_name')

    @property
    def drug_discovery_docking_result_plddt_file_name(self) -> str:
        return self._config.get('drug-discovery', 'docking_result_plddt_file_name')

