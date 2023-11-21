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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from finbourne_horizon.models.file_details import FileDetails
from finbourne_horizon.models.row_details import RowDetails

class ProcessSummary(BaseModel):
    """
    Completed event details  # noqa: E501
    """
    end_time: Optional[datetime] = Field(None, alias="endTime")
    category: Optional[StrictStr] = None
    status: StrictStr = Field(...)
    message: StrictStr = Field(...)
    rows: RowDetails = Field(...)
    file_details: Optional[conlist(FileDetails)] = Field(None, alias="fileDetails")
    __properties = ["endTime", "category", "status", "message", "rows", "fileDetails"]

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
    def from_json(cls, json_str: str) -> ProcessSummary:
        """Create an instance of ProcessSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rows
        if self.rows:
            _dict['rows'] = self.rows.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in file_details (list)
        _items = []
        if self.file_details:
            for _item in self.file_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fileDetails'] = _items
        # set to None if end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.end_time is None and "end_time" in self.__fields_set__:
            _dict['endTime'] = None

        # set to None if category (nullable) is None
        # and __fields_set__ contains the field
        if self.category is None and "category" in self.__fields_set__:
            _dict['category'] = None

        # set to None if file_details (nullable) is None
        # and __fields_set__ contains the field
        if self.file_details is None and "file_details" in self.__fields_set__:
            _dict['fileDetails'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessSummary:
        """Create an instance of ProcessSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessSummary.parse_obj(obj)

        _obj = ProcessSummary.parse_obj({
            "end_time": obj.get("endTime"),
            "category": obj.get("category"),
            "status": obj.get("status"),
            "message": obj.get("message"),
            "rows": RowDetails.from_dict(obj.get("rows")) if obj.get("rows") is not None else None,
            "file_details": [FileDetails.from_dict(_item) for _item in obj.get("fileDetails")] if obj.get("fileDetails") is not None else None
        })
        return _obj
