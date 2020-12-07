# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.10.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.links import Links  # noqa: F401,E501


class UserFlagSetting(object):
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
        'links': 'Links',
        'value': 'bool',
        'setting': 'bool'
    }

    attribute_map = {
        'links': '_links',
        'value': '_value',
        'setting': 'setting'
    }

    def __init__(self, links=None, value=None, setting=None):  # noqa: E501
        """UserFlagSetting - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._value = None
        self._setting = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if value is not None:
            self.value = value
        if setting is not None:
            self.setting = setting

    @property
    def links(self):
        """Gets the links of this UserFlagSetting.  # noqa: E501


        :return: The links of this UserFlagSetting.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserFlagSetting.


        :param links: The links of this UserFlagSetting.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def value(self):
        """Gets the value of this UserFlagSetting.  # noqa: E501

        The most important attribute in the response. The _value is the current setting for the user. For a boolean feature toggle, this will be true, false, or null if there is no defined fallthrough value.  # noqa: E501

        :return: The value of this UserFlagSetting.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UserFlagSetting.

        The most important attribute in the response. The _value is the current setting for the user. For a boolean feature toggle, this will be true, false, or null if there is no defined fallthrough value.  # noqa: E501

        :param value: The value of this UserFlagSetting.  # noqa: E501
        :type: bool
        """

        self._value = value

    @property
    def setting(self):
        """Gets the setting of this UserFlagSetting.  # noqa: E501

        The setting attribute indicates whether you've explicitly targeted this user to receive a particular variation. For example, if you have explicitly turned off a feature toggle for a user, setting will be false. A setting of null means that you haven't assigned that user to a specific variation.  # noqa: E501

        :return: The setting of this UserFlagSetting.  # noqa: E501
        :rtype: bool
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """Sets the setting of this UserFlagSetting.

        The setting attribute indicates whether you've explicitly targeted this user to receive a particular variation. For example, if you have explicitly turned off a feature toggle for a user, setting will be false. A setting of null means that you haven't assigned that user to a specific variation.  # noqa: E501

        :param setting: The setting of this UserFlagSetting.  # noqa: E501
        :type: bool
        """

        self._setting = setting

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
        if issubclass(UserFlagSetting, dict):
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
        if not isinstance(other, UserFlagSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
