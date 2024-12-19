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
from pydantic.v1 import BaseModel, Field
from finbourne_horizon.models.open_figi_data import OpenFigiData
from finbourne_horizon.models.perm_id_data import PermIdData

class OpenFigiPermIdResult(BaseModel):
    """
    A packed WebAPI OpenFigi DTO and PermId DTO  # noqa: E501
    """
    open_figi_result: OpenFigiData = Field(..., alias="openFigiResult")
    perm_id_result: Optional[PermIdData] = Field(None, alias="permIdResult")
    __properties = ["openFigiResult", "permIdResult"]

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
    def from_json(cls, json_str: str) -> OpenFigiPermIdResult:
        """Create an instance of OpenFigiPermIdResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of open_figi_result
        if self.open_figi_result:
            _dict['openFigiResult'] = self.open_figi_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of perm_id_result
        if self.perm_id_result:
            _dict['permIdResult'] = self.perm_id_result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OpenFigiPermIdResult:
        """Create an instance of OpenFigiPermIdResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OpenFigiPermIdResult.parse_obj(obj)

        _obj = OpenFigiPermIdResult.parse_obj({
            "open_figi_result": OpenFigiData.from_dict(obj.get("openFigiResult")) if obj.get("openFigiResult") is not None else None,
            "perm_id_result": PermIdData.from_dict(obj.get("permIdResult")) if obj.get("permIdResult") is not None else None
        })
        return _obj
