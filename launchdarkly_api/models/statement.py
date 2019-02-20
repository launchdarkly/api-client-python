# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.14
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.actions import Actions  # noqa: F401,E501
from launchdarkly_api.models.resources import Resources  # noqa: F401,E501


class Statement(object):
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
        'resources': 'Resources',
        'notresources': 'Resources',
        'actions': 'Actions',
        'notactions': 'Actions',
        'effect': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'notresources': 'notresources',
        'actions': 'actions',
        'notactions': 'notactions',
        'effect': 'effect'
    }

    def __init__(self, resources=None, notresources=None, actions=None, notactions=None, effect=None):  # noqa: E501
        """Statement - a model defined in Swagger"""  # noqa: E501

        self._resources = None
        self._notresources = None
        self._actions = None
        self._notactions = None
        self._effect = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if notresources is not None:
            self.notresources = notresources
        if actions is not None:
            self.actions = actions
        if notactions is not None:
            self.notactions = notactions
        if effect is not None:
            self.effect = effect

    @property
    def resources(self):
        """Gets the resources of this Statement.  # noqa: E501


        :return: The resources of this Statement.  # noqa: E501
        :rtype: Resources
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Statement.


        :param resources: The resources of this Statement.  # noqa: E501
        :type: Resources
        """

        self._resources = resources

    @property
    def notresources(self):
        """Gets the notresources of this Statement.  # noqa: E501

        Targeted resource will be those resources NOT in this list. The \"resources`\" field must be empty to use this field.  # noqa: E501

        :return: The notresources of this Statement.  # noqa: E501
        :rtype: Resources
        """
        return self._notresources

    @notresources.setter
    def notresources(self, notresources):
        """Sets the notresources of this Statement.

        Targeted resource will be those resources NOT in this list. The \"resources`\" field must be empty to use this field.  # noqa: E501

        :param notresources: The notresources of this Statement.  # noqa: E501
        :type: Resources
        """

        self._notresources = notresources

    @property
    def actions(self):
        """Gets the actions of this Statement.  # noqa: E501


        :return: The actions of this Statement.  # noqa: E501
        :rtype: Actions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Statement.


        :param actions: The actions of this Statement.  # noqa: E501
        :type: Actions
        """

        self._actions = actions

    @property
    def notactions(self):
        """Gets the notactions of this Statement.  # noqa: E501

        Targeted actions will be those actions NOT in this list. The \"actions\" field must be empty to use this field.  # noqa: E501

        :return: The notactions of this Statement.  # noqa: E501
        :rtype: Actions
        """
        return self._notactions

    @notactions.setter
    def notactions(self, notactions):
        """Sets the notactions of this Statement.

        Targeted actions will be those actions NOT in this list. The \"actions\" field must be empty to use this field.  # noqa: E501

        :param notactions: The notactions of this Statement.  # noqa: E501
        :type: Actions
        """

        self._notactions = notactions

    @property
    def effect(self):
        """Gets the effect of this Statement.  # noqa: E501


        :return: The effect of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Statement.


        :param effect: The effect of this Statement.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "deny"]  # noqa: E501
        if effect not in allowed_values:
            raise ValueError(
                "Invalid value for `effect` ({0}), must be one of {1}"  # noqa: E501
                .format(effect, allowed_values)
            )

        self._effect = effect

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
        if issubclass(Statement, dict):
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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
