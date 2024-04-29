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
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from finbourne_horizon.models.resource_id import ResourceId

class LusidPropertyDefinition(BaseModel):
    """
    Defines the information in a LUSID Property Definition  # noqa: E501
    """
    key: StrictStr = Field(...)
    product_entity_item_key: constr(strict=True, min_length=1) = Field(..., alias="productEntityItemKey", description="Property key associated with the mapping")
    domain: constr(strict=True, min_length=1) = Field(..., description="The domain of this definition.")
    scope: constr(strict=True, min_length=1) = Field(..., description="The scope of this definition.")
    code: constr(strict=True, min_length=1) = Field(..., description="The code of this definition.")
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The name used when this definition is displayed.")
    data_type_id: ResourceId = Field(..., alias="dataTypeId")
    description: StrictStr = Field(...)
    lifetime: constr(strict=True, min_length=1) = Field(...)
    constraint_style: constr(strict=True, min_length=1) = Field(..., alias="constraintStyle")
    __properties = ["key", "productEntityItemKey", "domain", "scope", "code", "displayName", "dataTypeId", "description", "lifetime", "constraintStyle"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LusidPropertyDefinition:
        """Create an instance of LusidPropertyDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "key",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_type_id
        if self.data_type_id:
            _dict['dataTypeId'] = self.data_type_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LusidPropertyDefinition:
        """Create an instance of LusidPropertyDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LusidPropertyDefinition.parse_obj(obj)

        _obj = LusidPropertyDefinition.parse_obj({
            "key": obj.get("key"),
            "product_entity_item_key": obj.get("productEntityItemKey"),
            "domain": obj.get("domain"),
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "display_name": obj.get("displayName"),
            "data_type_id": ResourceId.from_dict(obj.get("dataTypeId")) if obj.get("dataTypeId") is not None else None,
            "description": obj.get("description"),
            "lifetime": obj.get("lifetime"),
            "constraint_style": obj.get("constraintStyle")
        })
        return _obj
