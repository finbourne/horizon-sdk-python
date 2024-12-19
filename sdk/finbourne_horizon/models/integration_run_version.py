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
from pydantic.v1 import BaseModel, Field

class IntegrationRunVersion(BaseModel):
    """
    IntegrationRunVersion
    """
    as_at_created: Optional[datetime] = Field(None, alias="asAtCreated")
    as_at_modified: Optional[datetime] = Field(None, alias="asAtModified")
    __properties = ["asAtCreated", "asAtModified"]

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
    def from_json(cls, json_str: str) -> IntegrationRunVersion:
        """Create an instance of IntegrationRunVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if as_at_created (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_created is None and "as_at_created" in self.__fields_set__:
            _dict['asAtCreated'] = None

        # set to None if as_at_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_modified is None and "as_at_modified" in self.__fields_set__:
            _dict['asAtModified'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationRunVersion:
        """Create an instance of IntegrationRunVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationRunVersion.parse_obj(obj)

        _obj = IntegrationRunVersion.parse_obj({
            "as_at_created": obj.get("asAtCreated"),
            "as_at_modified": obj.get("asAtModified")
        })
        return _obj
