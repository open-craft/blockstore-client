# coding: utf-8

"""
    Blockstore API

    REST API for Open edX Blockstore  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class EntityDetail(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'entity_type': 'str',
        'external_id': 'str',
        'persisted': 'bool',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'external_id': 'external_id',
        'persisted': 'persisted',
        'tags': 'tags'
    }

    def __init__(self, entity_type=None, external_id=None, persisted=None, tags=None):  # noqa: E501
        """EntityDetail - a model defined in OpenAPI"""  # noqa: E501

        self._entity_type = None
        self._external_id = None
        self._persisted = None
        self._tags = None
        self.discriminator = None

        self.entity_type = entity_type
        self.external_id = external_id
        if persisted is not None:
            self.persisted = persisted
        if tags is not None:
            self.tags = tags

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityDetail.  # noqa: E501


        :return: The entity_type of this EntityDetail.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityDetail.


        :param entity_type: The entity_type of this EntityDetail.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if entity_type is not None and len(entity_type) < 1:
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def external_id(self):
        """Gets the external_id of this EntityDetail.  # noqa: E501


        :return: The external_id of this EntityDetail.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EntityDetail.


        :param external_id: The external_id of this EntityDetail.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_id = external_id

    @property
    def persisted(self):
        """Gets the persisted of this EntityDetail.  # noqa: E501


        :return: The persisted of this EntityDetail.  # noqa: E501
        :rtype: bool
        """
        return self._persisted

    @persisted.setter
    def persisted(self, persisted):
        """Sets the persisted of this EntityDetail.


        :param persisted: The persisted of this EntityDetail.  # noqa: E501
        :type: bool
        """

        self._persisted = persisted

    @property
    def tags(self):
        """Gets the tags of this EntityDetail.  # noqa: E501

                 The list of tags that this entity has applied.           # noqa: E501

        :return: The tags of this EntityDetail.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EntityDetail.

                 The list of tags that this entity has applied.           # noqa: E501

        :param tags: The tags of this EntityDetail.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EntityDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other