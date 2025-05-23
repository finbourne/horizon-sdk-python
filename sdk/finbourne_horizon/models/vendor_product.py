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
from finbourne_horizon.models.lusid_entity import LusidEntity

class VendorProduct(BaseModel):
    """
    Denormalised information about vendors, the products they provide and the LUSID entity types they can be used to populate.  # noqa: E501
    """
    vendor_name:  StrictStr = Field(...,alias="vendorName") 
    product_name:  StrictStr = Field(...,alias="productName") 
    vendor_product_key:  StrictStr = Field(...,alias="vendorProductKey") 
    lusid_entity: LusidEntity = Field(..., alias="lusidEntity")
    __properties = ["vendorName", "productName", "vendorProductKey", "lusidEntity"]

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
    def from_json(cls, json_str: str) -> VendorProduct:
        """Create an instance of VendorProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lusid_entity
        if self.lusid_entity:
            _dict['lusidEntity'] = self.lusid_entity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VendorProduct:
        """Create an instance of VendorProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VendorProduct.parse_obj(obj)

        _obj = VendorProduct.parse_obj({
            "vendor_name": obj.get("vendorName"),
            "product_name": obj.get("productName"),
            "vendor_product_key": obj.get("vendorProductKey"),
            "lusid_entity": LusidEntity.from_dict(obj.get("lusidEntity")) if obj.get("lusidEntity") is not None else None
        })
        return _obj
