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
from pydantic import BaseModel, Field, StrictInt

class RowDetails(BaseModel):
    """
    Information about the nuber of rows processed.  # noqa: E501
    """
    rows_total: Optional[StrictInt] = Field(None, alias="rowsTotal", description="The number of rows processed.")
    rows_succeeded: Optional[StrictInt] = Field(None, alias="rowsSucceeded", description="The number of rows that were successfully processed.")
    rows_ignored: Optional[StrictInt] = Field(None, alias="rowsIgnored", description="The number of rows that were not processed.")
    rows_failed: Optional[StrictInt] = Field(None, alias="rowsFailed", description="The number of rows that failed when being processed.")
    __properties = ["rowsTotal", "rowsSucceeded", "rowsIgnored", "rowsFailed"]

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
    def from_json(cls, json_str: str) -> RowDetails:
        """Create an instance of RowDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if rows_total (nullable) is None
        # and __fields_set__ contains the field
        if self.rows_total is None and "rows_total" in self.__fields_set__:
            _dict['rowsTotal'] = None

        # set to None if rows_succeeded (nullable) is None
        # and __fields_set__ contains the field
        if self.rows_succeeded is None and "rows_succeeded" in self.__fields_set__:
            _dict['rowsSucceeded'] = None

        # set to None if rows_ignored (nullable) is None
        # and __fields_set__ contains the field
        if self.rows_ignored is None and "rows_ignored" in self.__fields_set__:
            _dict['rowsIgnored'] = None

        # set to None if rows_failed (nullable) is None
        # and __fields_set__ contains the field
        if self.rows_failed is None and "rows_failed" in self.__fields_set__:
            _dict['rowsFailed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RowDetails:
        """Create an instance of RowDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RowDetails.parse_obj(obj)

        _obj = RowDetails.parse_obj({
            "rows_total": obj.get("rowsTotal"),
            "rows_succeeded": obj.get("rowsSucceeded"),
            "rows_ignored": obj.get("rowsIgnored"),
            "rows_failed": obj.get("rowsFailed")
        })
        return _obj
