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


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 
from finbourne_horizon.models.integration_run_integration import IntegrationRunIntegration
from finbourne_horizon.models.integration_run_log import IntegrationRunLog
from finbourne_horizon.models.integration_run_version import IntegrationRunVersion

class IntegrationRunResponse(BaseModel):
    """
    IntegrationRunResponse
    """
    run_id:  StrictStr = Field(...,alias="runId") 
    instance_id:  Optional[StrictStr] = Field(None,alias="instanceId") 
    instance_name:  Optional[StrictStr] = Field(None,alias="instanceName") 
    status:  Optional[StrictStr] = Field(None,alias="status") 
    message:  Optional[StrictStr] = Field(None,alias="message") 
    integration: IntegrationRunIntegration = Field(...)
    version: IntegrationRunVersion = Field(...)
    integration_logs: Optional[Dict[str, Dict[str, IntegrationRunLog]]] = Field(None, alias="integrationLogs")
    __properties = ["runId", "instanceId", "instanceName", "status", "message", "integration", "version", "integrationLogs"]

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
    def from_json(cls, json_str: str) -> IntegrationRunResponse:
        """Create an instance of IntegrationRunResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of integration
        if self.integration:
            _dict['integration'] = self.integration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in integration_logs (dict)
        _field_dict = {}
        if self.integration_logs:
            for _key in self.integration_logs:
                if self.integration_logs[_key]:
                    _field_dict[_key] = self.integration_logs[_key].to_dict()
            _dict['integrationLogs'] = _field_dict
        # set to None if instance_id (nullable) is None
        # and __fields_set__ contains the field
        if self.instance_id is None and "instance_id" in self.__fields_set__:
            _dict['instanceId'] = None

        # set to None if instance_name (nullable) is None
        # and __fields_set__ contains the field
        if self.instance_name is None and "instance_name" in self.__fields_set__:
            _dict['instanceName'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if integration_logs (nullable) is None
        # and __fields_set__ contains the field
        if self.integration_logs is None and "integration_logs" in self.__fields_set__:
            _dict['integrationLogs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationRunResponse:
        """Create an instance of IntegrationRunResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationRunResponse.parse_obj(obj)

        _obj = IntegrationRunResponse.parse_obj({
            "run_id": obj.get("runId"),
            "instance_id": obj.get("instanceId"),
            "instance_name": obj.get("instanceName"),
            "status": obj.get("status"),
            "message": obj.get("message"),
            "integration": IntegrationRunIntegration.from_dict(obj.get("integration")) if obj.get("integration") is not None else None,
            "version": IntegrationRunVersion.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "integration_logs": dict(
                (_k, dict(
                    (_ik, IntegrationRunLog.from_dict(_iv))
                        for _ik, _iv in _v.items()
                    )
                    if _v is not None
                    else None
                )
                for _k, _v in obj.get("integrationLogs").items()
            )
            if obj.get("integrationLogs") is not None
            else None
        })
        return _obj
