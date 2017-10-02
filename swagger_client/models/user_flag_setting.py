# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API

    OpenAPI spec version: 2.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserFlagSetting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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

    def __init__(self, links=None, value=None, setting=None):
        """
        UserFlagSetting - a model defined in Swagger
        """

        self._links = None
        self._value = None
        self._setting = None

        if links is not None:
          self.links = links
        if value is not None:
          self.value = value
        if setting is not None:
          self.setting = setting

    @property
    def links(self):
        """
        Gets the links of this UserFlagSetting.

        :return: The links of this UserFlagSetting.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this UserFlagSetting.

        :param links: The links of this UserFlagSetting.
        :type: Links
        """

        self._links = links

    @property
    def value(self):
        """
        Gets the value of this UserFlagSetting.

        :return: The value of this UserFlagSetting.
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserFlagSetting.

        :param value: The value of this UserFlagSetting.
        :type: bool
        """

        self._value = value

    @property
    def setting(self):
        """
        Gets the setting of this UserFlagSetting.

        :return: The setting of this UserFlagSetting.
        :rtype: bool
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """
        Sets the setting of this UserFlagSetting.

        :param setting: The setting of this UserFlagSetting.
        :type: bool
        """

        self._setting = setting

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserFlagSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
