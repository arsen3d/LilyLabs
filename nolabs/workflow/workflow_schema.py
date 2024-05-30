import uuid
from typing import Optional, List, Any, Dict, Union

from pydantic import BaseModel, Field


class PropertyModel(BaseModel):
    type: Optional[Union[str, List[str]]] = None
    properties: Optional[Dict[str, 'PropertyModel']] = Field(default_factory=dict)
    required: List[str] = Field(default_factory=list)
    description: Optional[str] = None
    enum: List[Any] = Field(default_factory=list)
    const: Optional[Any] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    example: Optional[Any] = None
    title: Optional[str] = None
    anyOf: List[Union['PropertyModel', dict]] = Field(default_factory=list)
    ref: Optional[str] = Field(default=None)


class ComponentModel(BaseModel):
    name: str
    input: Dict[str, PropertyModel]
    output: Dict[str, PropertyModel]


class MappingModel(BaseModel):
    source_path: List[str]
    target_path: List[str]
    source_component_id: uuid.UUID
    error: Optional[str] = None


class DefaultWorkflowComponentModelValue(BaseModel):
    path_to: List[str]
    value: Optional[Any] = None
    error: Optional[str] = None


class JobValidationError(BaseModel):
    job_id: uuid.UUID
    msg: str


class WorkflowComponentModel(BaseModel):
    name: str
    component_id: uuid.UUID
    job_ids: List[uuid.UUID] = Field(default_factory=list)
    mappings: List[MappingModel] = Field(default_factory=list)
    error: Optional[str] = None
    defaults: List[DefaultWorkflowComponentModelValue] = Field(default_factory=list)
    jobs_errors: List[JobValidationError]


class WorkflowSchemaModel(BaseModel):
    experiment_id: uuid.UUID
    components: List[ComponentModel]
    workflow_components: List[WorkflowComponentModel]
    error: Optional[str] = None
    valid: bool = True

    def get_wf_component(self, component_id: uuid.UUID):
        return [wc for wc in self.workflow_components if wc.component_id == component_id]
