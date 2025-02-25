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
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, conlist, constr 
from finbourne_horizon.models.audit_complete_status import AuditCompleteStatus
from finbourne_horizon.models.audit_file_details import AuditFileDetails

class AuditCompleteRequest(BaseModel):
    """
    An incoming request for a Horizon Complete Event  # noqa: E501
    """
    id:  StrictStr = Field(...,alias="id", description="A unique ID identifiying the source of the event") 
    user_id:  StrictStr = Field(...,alias="userId", description="A unique ID identifiying who owns the schedule") 
    scheduler_run_id:  StrictStr = Field(...,alias="schedulerRunId", description="The GUID of the schedule run") 
    start_time: datetime = Field(..., alias="startTime", description="When the run was started in UTC")
    end_time: datetime = Field(..., alias="endTime", description="When the run finished in UTC")
    message:  StrictStr = Field(...,alias="message", description="A descriptive message to accompany the status") 
    status: AuditCompleteStatus = Field(...)
    rows_total: StrictInt = Field(..., alias="rowsTotal", description="The number of data rows operated on")
    rows_succeeded: StrictInt = Field(..., alias="rowsSucceeded", description="The number of data rows successfully operated on")
    rows_failed: StrictInt = Field(..., alias="rowsFailed", description="The number of data rows that failed to be operated on")
    rows_ignored: StrictInt = Field(..., alias="rowsIgnored", description="The number of data rows that had no actions taken")
    audit_files: conlist(AuditFileDetails) = Field(..., alias="auditFiles", description="A list of file details for attaching to the event")
    process_name_override:  Optional[StrictStr] = Field(None,alias="processNameOverride", description="Optional Name for how the process appears in Data Feed Monitoring") 
    __properties = ["id", "userId", "schedulerRunId", "startTime", "endTime", "message", "status", "rowsTotal", "rowsSucceeded", "rowsFailed", "rowsIgnored", "auditFiles", "processNameOverride"]

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
    def from_json(cls, json_str: str) -> AuditCompleteRequest:
        """Create an instance of AuditCompleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in audit_files (list)
        _items = []
        if self.audit_files:
            for _item in self.audit_files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['auditFiles'] = _items
        # set to None if process_name_override (nullable) is None
        # and __fields_set__ contains the field
        if self.process_name_override is None and "process_name_override" in self.__fields_set__:
            _dict['processNameOverride'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditCompleteRequest:
        """Create an instance of AuditCompleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditCompleteRequest.parse_obj(obj)

        _obj = AuditCompleteRequest.parse_obj({
            "id": obj.get("id"),
            "user_id": obj.get("userId"),
            "scheduler_run_id": obj.get("schedulerRunId"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "message": obj.get("message"),
            "status": obj.get("status"),
            "rows_total": obj.get("rowsTotal"),
            "rows_succeeded": obj.get("rowsSucceeded"),
            "rows_failed": obj.get("rowsFailed"),
            "rows_ignored": obj.get("rowsIgnored"),
            "audit_files": [AuditFileDetails.from_dict(_item) for _item in obj.get("auditFiles")] if obj.get("auditFiles") is not None else None,
            "process_name_override": obj.get("processNameOverride")
        })
        return _obj
