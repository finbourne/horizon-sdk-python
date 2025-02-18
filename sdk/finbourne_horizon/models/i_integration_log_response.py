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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, StrictStr, conlist 
from finbourne_horizon.models.integration_log_activity import IntegrationLogActivity
from finbourne_horizon.models.integration_log_record import IntegrationLogRecord
from finbourne_horizon.models.integration_log_target_record import IntegrationLogTargetRecord

class IIntegrationLogResponse(BaseModel):
    """
    IIntegrationLogResponse
    """
    log_id: StrictInt = Field(..., alias="logId")
    run_id:  Optional[StrictStr] = Field(None,alias="runId") 
    parent_log_id: Optional[StrictInt] = Field(None, alias="parentLogId")
    log_type:  StrictStr = Field(...,alias="logType") 
    first_activity: Optional[datetime] = Field(None, alias="firstActivity")
    last_activity: Optional[datetime] = Field(None, alias="lastActivity")
    status:  Optional[StrictStr] = Field(None,alias="status") 
    source_record: Optional[IntegrationLogRecord] = Field(None, alias="sourceRecord")
    target_record: Optional[IntegrationLogTargetRecord] = Field(None, alias="targetRecord")
    activities: conlist(IntegrationLogActivity) = Field(...)
    __properties = ["logId", "runId", "parentLogId", "logType", "firstActivity", "lastActivity", "status", "sourceRecord", "targetRecord", "activities"]

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
    def from_json(cls, json_str: str) -> IIntegrationLogResponse:
        """Create an instance of IIntegrationLogResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "log_id",
                            "run_id",
                            "parent_log_id",
                            "log_type",
                            "first_activity",
                            "last_activity",
                            "status",
                            "activities",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_record
        if self.source_record:
            _dict['sourceRecord'] = self.source_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_record
        if self.target_record:
            _dict['targetRecord'] = self.target_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in activities (list)
        _items = []
        if self.activities:
            for _item in self.activities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['activities'] = _items
        # set to None if run_id (nullable) is None
        # and __fields_set__ contains the field
        if self.run_id is None and "run_id" in self.__fields_set__:
            _dict['runId'] = None

        # set to None if parent_log_id (nullable) is None
        # and __fields_set__ contains the field
        if self.parent_log_id is None and "parent_log_id" in self.__fields_set__:
            _dict['parentLogId'] = None

        # set to None if first_activity (nullable) is None
        # and __fields_set__ contains the field
        if self.first_activity is None and "first_activity" in self.__fields_set__:
            _dict['firstActivity'] = None

        # set to None if last_activity (nullable) is None
        # and __fields_set__ contains the field
        if self.last_activity is None and "last_activity" in self.__fields_set__:
            _dict['lastActivity'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IIntegrationLogResponse:
        """Create an instance of IIntegrationLogResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IIntegrationLogResponse.parse_obj(obj)

        _obj = IIntegrationLogResponse.parse_obj({
            "log_id": obj.get("logId"),
            "run_id": obj.get("runId"),
            "parent_log_id": obj.get("parentLogId"),
            "log_type": obj.get("logType"),
            "first_activity": obj.get("firstActivity"),
            "last_activity": obj.get("lastActivity"),
            "status": obj.get("status"),
            "source_record": IntegrationLogRecord.from_dict(obj.get("sourceRecord")) if obj.get("sourceRecord") is not None else None,
            "target_record": IntegrationLogTargetRecord.from_dict(obj.get("targetRecord")) if obj.get("targetRecord") is not None else None,
            "activities": [IntegrationLogActivity.from_dict(_item) for _item in obj.get("activities")] if obj.get("activities") is not None else None
        })
        return _obj
