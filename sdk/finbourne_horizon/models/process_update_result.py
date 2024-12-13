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
from pydantic.v1 import BaseModel, Field, StrictStr

class ProcessUpdateResult(BaseModel):
    """
    Shows details relevant to update events for a query  # noqa: E501
    """
    domain: StrictStr = Field(...)
    entry_id: StrictStr = Field(..., alias="entryId")
    process_name: StrictStr = Field(..., alias="processName")
    run_id: StrictStr = Field(..., alias="runId")
    entry_date: datetime = Field(..., alias="entryDate")
    status: StrictStr = Field(...)
    message: StrictStr = Field(...)
    schema_version: Optional[StrictStr] = Field(None, alias="schemaVersion")
    __properties = ["domain", "entryId", "processName", "runId", "entryDate", "status", "message", "schemaVersion"]

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
    def from_json(cls, json_str: str) -> ProcessUpdateResult:
        """Create an instance of ProcessUpdateResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if schema_version (nullable) is None
        # and __fields_set__ contains the field
        if self.schema_version is None and "schema_version" in self.__fields_set__:
            _dict['schemaVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessUpdateResult:
        """Create an instance of ProcessUpdateResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessUpdateResult.parse_obj(obj)

        _obj = ProcessUpdateResult.parse_obj({
            "domain": obj.get("domain"),
            "entry_id": obj.get("entryId"),
            "process_name": obj.get("processName"),
            "run_id": obj.get("runId"),
            "entry_date": obj.get("entryDate"),
            "status": obj.get("status"),
            "message": obj.get("message"),
            "schema_version": obj.get("schemaVersion")
        })
        return _obj
