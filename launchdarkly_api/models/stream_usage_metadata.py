# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.6.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StreamUsageMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sdk': 'str',
        'version': 'str',
        'source': 'str'
    }

    attribute_map = {
        'sdk': 'sdk',
        'version': 'version',
        'source': 'source'
    }

    def __init__(self, sdk=None, version=None, source=None):  # noqa: E501
        """StreamUsageMetadata - a model defined in Swagger"""  # noqa: E501

        self._sdk = None
        self._version = None
        self._source = None
        self.discriminator = None

        if sdk is not None:
            self.sdk = sdk
        if version is not None:
            self.version = version
        if source is not None:
            self.source = source

    @property
    def sdk(self):
        """Gets the sdk of this StreamUsageMetadata.  # noqa: E501

        The language of the sdk  # noqa: E501

        :return: The sdk of this StreamUsageMetadata.  # noqa: E501
        :rtype: str
        """
        return self._sdk

    @sdk.setter
    def sdk(self, sdk):
        """Sets the sdk of this StreamUsageMetadata.

        The language of the sdk  # noqa: E501

        :param sdk: The sdk of this StreamUsageMetadata.  # noqa: E501
        :type: str
        """

        self._sdk = sdk

    @property
    def version(self):
        """Gets the version of this StreamUsageMetadata.  # noqa: E501

        The version of the SDK  # noqa: E501

        :return: The version of this StreamUsageMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StreamUsageMetadata.

        The version of the SDK  # noqa: E501

        :param version: The version of this StreamUsageMetadata.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def source(self):
        """Gets the source of this StreamUsageMetadata.  # noqa: E501


        :return: The source of this StreamUsageMetadata.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this StreamUsageMetadata.


        :param source: The source of this StreamUsageMetadata.  # noqa: E501
        :type: str
        """

        self._source = source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(StreamUsageMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamUsageMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
