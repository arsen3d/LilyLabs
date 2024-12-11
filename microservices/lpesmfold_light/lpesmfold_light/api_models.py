from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class RunEsmFoldPredictionRequest:
    protein_sequence: str
    job_id: str = None
    def to_dict(self):
        return dataclasses.asdict(self)
        # return {
        #     'protein_sequence': self.protein_sequence,
        #     'job_id': self.job_id
        # }

@dataclasses.dataclass
class RunEsmFoldPredictionResponse:
    pdb_content: str

@dataclasses.dataclass
class IsJobRunningResponse:
    is_running: bool