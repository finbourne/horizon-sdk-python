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


from typing import Any, Dict
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 

class ExecuteInstanceResponse(BaseModel):
    """
    Response for executing an instance.  # noqa: E501
    """
    execution_id:  StrictStr = Field(...,alias="executionId", description="Identifier for the execution of the integration instance") 
    __properties = ["executionId"]

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
    def from_json(cls, json_str: str) -> ExecuteInstanceResponse:
        """Create an instance of ExecuteInstanceResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExecuteInstanceResponse:
        """Create an instance of ExecuteInstanceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExecuteInstanceResponse.parse_obj(obj)

        _obj = ExecuteInstanceResponse.parse_obj({
            "execution_id": obj.get("executionId")
        })
        return _obj
