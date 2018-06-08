# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.2
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EnvironmentBody(object):
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
        'name': 'str',
        'key': 'str',
        'color': 'str',
        'default_ttl': 'float'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'color': 'color',
        'default_ttl': 'defaultTtl'
    }

    def __init__(self, name=None, key=None, color=None, default_ttl=None):  # noqa: E501
        """EnvironmentBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._color = None
        self._default_ttl = None
        self.discriminator = None

        self.name = name
        self.key = key
        self.color = color
        if default_ttl is not None:
            self.default_ttl = default_ttl

    @property
    def name(self):
        """Gets the name of this EnvironmentBody.  # noqa: E501

        The name of the new environment.  # noqa: E501

        :return: The name of this EnvironmentBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentBody.

        The name of the new environment.  # noqa: E501

        :param name: The name of this EnvironmentBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this EnvironmentBody.  # noqa: E501

        A project-unique key for the new environment.  # noqa: E501

        :return: The key of this EnvironmentBody.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this EnvironmentBody.

        A project-unique key for the new environment.  # noqa: E501

        :param key: The key of this EnvironmentBody.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def color(self):
        """Gets the color of this EnvironmentBody.  # noqa: E501

        A color swatch (as an RGB hex value with no leading '#', e.g. C8C8C8).  # noqa: E501

        :return: The color of this EnvironmentBody.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EnvironmentBody.

        A color swatch (as an RGB hex value with no leading '#', e.g. C8C8C8).  # noqa: E501

        :param color: The color of this EnvironmentBody.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def default_ttl(self):
        """Gets the default_ttl of this EnvironmentBody.  # noqa: E501

        The default TTL for the new environment.  # noqa: E501

        :return: The default_ttl of this EnvironmentBody.  # noqa: E501
        :rtype: float
        """
        return self._default_ttl

    @default_ttl.setter
    def default_ttl(self, default_ttl):
        """Sets the default_ttl of this EnvironmentBody.

        The default TTL for the new environment.  # noqa: E501

        :param default_ttl: The default_ttl of this EnvironmentBody.  # noqa: E501
        :type: float
        """

        self._default_ttl = default_ttl

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnvironmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
