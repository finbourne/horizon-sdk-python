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


from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, Field
from finbourne_horizon.models.field_mapping import FieldMapping
from finbourne_horizon.models.property_mapping import PropertyMapping

class IntegrationPropertyConfiguration(BaseModel):
    """
    Response containing the description of an integration.  # noqa: E501
    """
    type: constr(strict=True) = Field(...,alias="type", description="The Integration this property configuration applies to") 
    properties: conlist(PropertyMapping) = Field(..., description="The mandatory and optional properties available in this integration")
    fields: conlist(FieldMapping) = Field(..., description="The fields available in this integration")
    __properties = ["type", "properties", "fields"]

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
    def from_json(cls, json_str: str) -> IntegrationPropertyConfiguration:
        """Create an instance of IntegrationPropertyConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationPropertyConfiguration:
        """Create an instance of IntegrationPropertyConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationPropertyConfiguration.parse_obj(obj)

        _obj = IntegrationPropertyConfiguration.parse_obj({
            "type": obj.get("type"),
            "properties": [PropertyMapping.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None,
            "fields": [FieldMapping.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None
        })
        return _obj
