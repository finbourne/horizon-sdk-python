# coding: utf-8

"""
    FINBOURNE Horizon API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, Field
from finbourne_horizon.models.process_summary import ProcessSummary

class ProcessInformation(BaseModel):
    """
    Required information for each process  # noqa: E501
    """
    domain: constr(strict=True) = Field(...,alias="domain", description="") 
    process_name: constr(strict=True) = Field(...,alias="processName", description="") 
    run_id: constr(strict=True) = Field(...,alias="runId", description="") 
    start_time: datetime = Field(..., alias="startTime")
    data_action: constr(strict=True) = Field(...,alias="dataAction", description="") 
    schema_version: constr(strict=True) = Field(None,alias="schemaVersion", description="") 
    user_id: constr(strict=True) = Field(...,alias="userId", description="") 
    process_summary: Optional[ProcessSummary] = Field(None, alias="processSummary")
    __properties = ["domain", "processName", "runId", "startTime", "dataAction", "schemaVersion", "userId", "processSummary"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ProcessInformation:
        """Create an instance of ProcessInformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of process_summary
        if self.process_summary:
            _dict['processSummary'] = self.process_summary.to_dict()
        # set to None if schema_version (nullable) is None
        # and __fields_set__ contains the field
        if self.schema_version is None and "schema_version" in self.__fields_set__:
            _dict['schemaVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessInformation:
        """Create an instance of ProcessInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessInformation.parse_obj(obj)

        _obj = ProcessInformation.parse_obj({
            "domain": obj.get("domain"),
            "process_name": obj.get("processName"),
            "run_id": obj.get("runId"),
            "start_time": obj.get("startTime"),
            "data_action": obj.get("dataAction"),
            "schema_version": obj.get("schemaVersion"),
            "user_id": obj.get("userId"),
            "process_summary": ProcessSummary.from_dict(obj.get("processSummary")) if obj.get("processSummary") is not None else None
        })
        return _obj
