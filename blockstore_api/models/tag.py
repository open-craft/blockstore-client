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


class Tag(object):
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
        'taxonomy_id': 'str',
        'name': 'str',
        'path': 'str',
        'parent': 'str'
    }

    attribute_map = {
        'taxonomy_id': 'taxonomy_id',
        'name': 'name',
        'path': 'path',
        'parent': 'parent'
    }

    def __init__(self, taxonomy_id=None, name=None, path=None, parent=None):  # noqa: E501
        """Tag - a model defined in OpenAPI"""  # noqa: E501

        self._taxonomy_id = None
        self._name = None
        self._path = None
        self._parent = None
        self.discriminator = None

        if taxonomy_id is not None:
            self.taxonomy_id = taxonomy_id
        self.name = name
        if path is not None:
            self.path = path
        self.parent = parent

    @property
    def taxonomy_id(self):
        """Gets the taxonomy_id of this Tag.  # noqa: E501


        :return: The taxonomy_id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._taxonomy_id

    @taxonomy_id.setter
    def taxonomy_id(self, taxonomy_id):
        """Sets the taxonomy_id of this Tag.


        :param taxonomy_id: The taxonomy_id of this Tag.  # noqa: E501
        :type: str
        """

        self._taxonomy_id = taxonomy_id

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        Display name of this tag; also its identifier within the taxonomy.  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        Display name of this tag; also its identifier within the taxonomy.  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this Tag.  # noqa: E501

                 'path' is provided for use in         implementing searching by tag. It provides the following guarantees:         (1) 'path' is globally unique.         (2) any child tag's path string starts with its parent's tag's path.       # noqa: E501

        :return: The path of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Tag.

                 'path' is provided for use in         implementing searching by tag. It provides the following guarantees:         (1) 'path' is globally unique.         (2) any child tag's path string starts with its parent's tag's path.       # noqa: E501

        :param path: The path of this Tag.  # noqa: E501
        :type: str
        """
        if path is not None and len(path) < 1:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def parent(self):
        """Gets the parent of this Tag.  # noqa: E501


        :return: The parent of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Tag.


        :param parent: The parent of this Tag.  # noqa: E501
        :type: str
        """
        if parent is not None and len(parent) < 1:
            raise ValueError("Invalid value for `parent`, length must be greater than or equal to `1`")  # noqa: E501

        self._parent = parent

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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other