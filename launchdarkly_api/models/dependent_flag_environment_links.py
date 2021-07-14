# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.3.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DependentFlagEnvironmentLinks(object):
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
        '_self': 'Link',
        'flag_link': 'Link'
    }

    attribute_map = {
        '_self': 'self',
        'flag_link': 'flagLink'
    }

    def __init__(self, _self=None, flag_link=None):  # noqa: E501
        """DependentFlagEnvironmentLinks - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._flag_link = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if flag_link is not None:
            self.flag_link = flag_link

    @property
    def _self(self):
        """Gets the _self of this DependentFlagEnvironmentLinks.  # noqa: E501


        :return: The _self of this DependentFlagEnvironmentLinks.  # noqa: E501
        :rtype: Link
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this DependentFlagEnvironmentLinks.


        :param _self: The _self of this DependentFlagEnvironmentLinks.  # noqa: E501
        :type: Link
        """

        self.__self = _self

    @property
    def flag_link(self):
        """Gets the flag_link of this DependentFlagEnvironmentLinks.  # noqa: E501


        :return: The flag_link of this DependentFlagEnvironmentLinks.  # noqa: E501
        :rtype: Link
        """
        return self._flag_link

    @flag_link.setter
    def flag_link(self, flag_link):
        """Sets the flag_link of this DependentFlagEnvironmentLinks.


        :param flag_link: The flag_link of this DependentFlagEnvironmentLinks.  # noqa: E501
        :type: Link
        """

        self._flag_link = flag_link

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
        if issubclass(DependentFlagEnvironmentLinks, dict):
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
        if not isinstance(other, DependentFlagEnvironmentLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
