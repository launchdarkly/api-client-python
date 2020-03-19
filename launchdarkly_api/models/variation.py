# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.32
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Variation(object):
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
        'description': 'str',
        'value': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, name=None, description=None, value=None):  # noqa: E501
        """Variation - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.value = value

    @property
    def name(self):
        """Gets the name of this Variation.  # noqa: E501


        :return: The name of this Variation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Variation.


        :param name: The name of this Variation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Variation.  # noqa: E501


        :return: The description of this Variation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Variation.


        :param description: The description of this Variation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this Variation.  # noqa: E501


        :return: The value of this Variation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Variation.


        :param value: The value of this Variation.  # noqa: E501
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(Variation, dict):
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
        if not isinstance(other, Variation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
