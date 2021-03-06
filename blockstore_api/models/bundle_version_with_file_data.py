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


class BundleVersionWithFileData(object):
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
        'bundle': 'str',
        'bundle_uuid': 'str',
        'change_description': 'str',
        'url': 'str',
        'version_num': 'int',
        'snapshot': 'str'
    }

    attribute_map = {
        'bundle': 'bundle',
        'bundle_uuid': 'bundle_uuid',
        'change_description': 'change_description',
        'url': 'url',
        'version_num': 'version_num',
        'snapshot': 'snapshot'
    }

    def __init__(self, bundle=None, bundle_uuid=None, change_description=None, url=None, version_num=None, snapshot=None):  # noqa: E501
        """BundleVersionWithFileData - a model defined in OpenAPI"""  # noqa: E501

        self._bundle = None
        self._bundle_uuid = None
        self._change_description = None
        self._url = None
        self._version_num = None
        self._snapshot = None
        self.discriminator = None

        if bundle is not None:
            self.bundle = bundle
        if bundle_uuid is not None:
            self.bundle_uuid = bundle_uuid
        if change_description is not None:
            self.change_description = change_description
        if url is not None:
            self.url = url
        if version_num is not None:
            self.version_num = version_num
        self.snapshot = snapshot

    @property
    def bundle(self):
        """Gets the bundle of this BundleVersionWithFileData.  # noqa: E501


        :return: The bundle of this BundleVersionWithFileData.  # noqa: E501
        :rtype: str
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this BundleVersionWithFileData.


        :param bundle: The bundle of this BundleVersionWithFileData.  # noqa: E501
        :type: str
        """

        self._bundle = bundle

    @property
    def bundle_uuid(self):
        """Gets the bundle_uuid of this BundleVersionWithFileData.  # noqa: E501


        :return: The bundle_uuid of this BundleVersionWithFileData.  # noqa: E501
        :rtype: str
        """
        return self._bundle_uuid

    @bundle_uuid.setter
    def bundle_uuid(self, bundle_uuid):
        """Sets the bundle_uuid of this BundleVersionWithFileData.


        :param bundle_uuid: The bundle_uuid of this BundleVersionWithFileData.  # noqa: E501
        :type: str
        """

        self._bundle_uuid = bundle_uuid

    @property
    def change_description(self):
        """Gets the change_description of this BundleVersionWithFileData.  # noqa: E501


        :return: The change_description of this BundleVersionWithFileData.  # noqa: E501
        :rtype: str
        """
        return self._change_description

    @change_description.setter
    def change_description(self, change_description):
        """Sets the change_description of this BundleVersionWithFileData.


        :param change_description: The change_description of this BundleVersionWithFileData.  # noqa: E501
        :type: str
        """
        if change_description is not None and len(change_description) > 1000:
            raise ValueError("Invalid value for `change_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._change_description = change_description

    @property
    def url(self):
        """Gets the url of this BundleVersionWithFileData.  # noqa: E501


        :return: The url of this BundleVersionWithFileData.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BundleVersionWithFileData.


        :param url: The url of this BundleVersionWithFileData.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def version_num(self):
        """Gets the version_num of this BundleVersionWithFileData.  # noqa: E501


        :return: The version_num of this BundleVersionWithFileData.  # noqa: E501
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        """Sets the version_num of this BundleVersionWithFileData.


        :param version_num: The version_num of this BundleVersionWithFileData.  # noqa: E501
        :type: int
        """

        self._version_num = version_num

    @property
    def snapshot(self):
        """Gets the snapshot of this BundleVersionWithFileData.  # noqa: E501


        :return: The snapshot of this BundleVersionWithFileData.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this BundleVersionWithFileData.


        :param snapshot: The snapshot of this BundleVersionWithFileData.  # noqa: E501
        :type: str
        """
        if snapshot is None:
            raise ValueError("Invalid value for `snapshot`, must not be `None`")  # noqa: E501

        self._snapshot = snapshot

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
        if not isinstance(other, BundleVersionWithFileData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
