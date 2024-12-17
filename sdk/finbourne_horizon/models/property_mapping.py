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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, Field
from finbourne_horizon.models.lusid_property_definition import LusidPropertyDefinition
from finbourne_horizon.models.optionality import Optionality
from finbourne_horizon.models.vendor_field import VendorField

class PropertyMapping(BaseModel):
    """
    Mapping from a set of VendorFields to a LUSID Property  # noqa: E501
    """
    var_property: LusidPropertyDefinition = Field(..., alias="property")
    vendor_fields: conlist(VendorField) = Field(..., alias="vendorFields", description="Fields that will be used to map to this Property Definition")
    optionality: Optionality = Field(...)
    entity_type: constr(strict=True) = Field(...,alias="entityType", description="The LUSID Entity this is valid for") 
    entity_sub_type: constr(strict=True) = Field(None,alias="entitySubType", description="The LUSID Entity sub type this is valid for") 
    transformation_description: constr(strict=True) = Field(None,alias="transformationDescription", description="The transformation, if required, to map from VendorFields to the LUSID Property") 
    versions: conlist(StrictStr) = Field(..., description="The versions of the Vendor integration this mapping is valid for")
    __properties = ["property", "vendorFields", "optionality", "entityType", "entitySubType", "transformationDescription", "versions"]

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
    def from_json(cls, json_str: str) -> PropertyMapping:
        """Create an instance of PropertyMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_property
        if self.var_property:
            _dict['property'] = self.var_property.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vendor_fields (list)
        _items = []
        if self.vendor_fields:
            for _item in self.vendor_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vendorFields'] = _items
        # set to None if entity_sub_type (nullable) is None
        # and __fields_set__ contains the field
        if self.entity_sub_type is None and "entity_sub_type" in self.__fields_set__:
            _dict['entitySubType'] = None

        # set to None if transformation_description (nullable) is None
        # and __fields_set__ contains the field
        if self.transformation_description is None and "transformation_description" in self.__fields_set__:
            _dict['transformationDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertyMapping:
        """Create an instance of PropertyMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertyMapping.parse_obj(obj)

        _obj = PropertyMapping.parse_obj({
            "var_property": LusidPropertyDefinition.from_dict(obj.get("property")) if obj.get("property") is not None else None,
            "vendor_fields": [VendorField.from_dict(_item) for _item in obj.get("vendorFields")] if obj.get("vendorFields") is not None else None,
            "optionality": obj.get("optionality"),
            "entity_type": obj.get("entityType"),
            "entity_sub_type": obj.get("entitySubType"),
            "transformation_description": obj.get("transformationDescription"),
            "versions": obj.get("versions")
        })
        return _obj
