# coding: utf-8

"""
    FINBOURNE Horizon API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class JSchemaType(str, Enum):
    """
    JSchemaType
    """

    """
    allowed enum values
    """
    NONE = 'None'
    STRING = 'String'
    NUMBER = 'Number'
    INTEGER = 'Integer'
    BOOLEAN = 'Boolean'
    OBJECT = 'Object'
    ARRAY = 'Array'
    NULL = 'Null'

    @classmethod
    def from_json(cls, json_str: str) -> JSchemaType:
        """Create an instance of JSchemaType from a JSON string"""
        return JSchemaType(json.loads(json_str))
