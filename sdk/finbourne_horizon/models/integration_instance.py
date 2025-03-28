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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, StrictStr, conlist 
from finbourne_horizon.models.trigger import Trigger

class IntegrationInstance(BaseModel):
    """
    Response containing an integration instance.  # noqa: E501
    """
    id:  StrictStr = Field(...,alias="id", description="Identifies the instance within the integration.") 
    integration_type:  StrictStr = Field(...,alias="integrationType", description="The integration type.") 
    name:  StrictStr = Field(...,alias="name", description="Name of the instance.") 
    description:  StrictStr = Field(...,alias="description", description="Description of the instance.") 
    enabled: StrictBool = Field(..., description="If true the instance will be executed if its trigger is satisfied.")
    triggers: conlist(Trigger) = Field(..., description="Defines what triggers execution of the instance.")
    details: Dict[str, Any] = Field(...)
    __properties = ["id", "integrationType", "name", "description", "enabled", "triggers", "details"]

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
    def from_json(cls, json_str: str) -> IntegrationInstance:
        """Create an instance of IntegrationInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item in self.triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['triggers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationInstance:
        """Create an instance of IntegrationInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationInstance.parse_obj(obj)

        _obj = IntegrationInstance.parse_obj({
            "id": obj.get("id"),
            "integration_type": obj.get("integrationType"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled"),
            "triggers": [Trigger.from_dict(_item) for _item in obj.get("triggers")] if obj.get("triggers") is not None else None,
            "details": obj.get("details")
        })
        return _obj
