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
from pydantic.v1 import BaseModel
from finbourne_horizon.models.query_specification import QuerySpecification

class QueryRequest(BaseModel):
    """
    Used to control queries, including getting \"pages\" of data  # noqa: E501
    """
    specification: Optional[QuerySpecification] = None
    __properties = ["specification"]

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
    def from_json(cls, json_str: str) -> QueryRequest:
        """Create an instance of QueryRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of specification
        if self.specification:
            _dict['specification'] = self.specification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryRequest:
        """Create an instance of QueryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryRequest.parse_obj(obj)

        _obj = QueryRequest.parse_obj({
            "specification": QuerySpecification.from_dict(obj.get("specification")) if obj.get("specification") is not None else None
        })
        return _obj
