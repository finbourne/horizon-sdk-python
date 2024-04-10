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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

class EnrichmentResponse(BaseModel):
    """
    Collated enrichment result information  # noqa: E501
    """
    enriched_instruments: conlist(StrictStr) = Field(..., alias="enrichedInstruments")
    ignored_instruments: conlist(StrictStr) = Field(..., alias="ignoredInstruments")
    error_file_id: Optional[StrictStr] = Field(None, alias="errorFileId", description="Error File ID, if one was created")
    __properties = ["enrichedInstruments", "ignoredInstruments", "errorFileId"]

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
    def from_json(cls, json_str: str) -> EnrichmentResponse:
        """Create an instance of EnrichmentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if error_file_id (nullable) is None
        # and __fields_set__ contains the field
        if self.error_file_id is None and "error_file_id" in self.__fields_set__:
            _dict['errorFileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnrichmentResponse:
        """Create an instance of EnrichmentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichmentResponse.parse_obj(obj)

        _obj = EnrichmentResponse.parse_obj({
            "enriched_instruments": obj.get("enrichedInstruments"),
            "ignored_instruments": obj.get("ignoredInstruments"),
            "error_file_id": obj.get("errorFileId")
        })
        return _obj
