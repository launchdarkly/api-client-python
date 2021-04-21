# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.1.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DependentFlagsLinks(object):
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
        'parent': 'Link',
        '_self': 'Link'
    }

    attribute_map = {
        'parent': 'parent',
        '_self': 'self'
    }

    def __init__(self, parent=None, _self=None):  # noqa: E501
        """DependentFlagsLinks - a model defined in Swagger"""  # noqa: E501

        self._parent = None
        self.__self = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if _self is not None:
            self._self = _self

    @property
    def parent(self):
        """Gets the parent of this DependentFlagsLinks.  # noqa: E501


        :return: The parent of this DependentFlagsLinks.  # noqa: E501
        :rtype: Link
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DependentFlagsLinks.


        :param parent: The parent of this DependentFlagsLinks.  # noqa: E501
        :type: Link
        """

        self._parent = parent

    @property
    def _self(self):
        """Gets the _self of this DependentFlagsLinks.  # noqa: E501


        :return: The _self of this DependentFlagsLinks.  # noqa: E501
        :rtype: Link
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this DependentFlagsLinks.


        :param _self: The _self of this DependentFlagsLinks.  # noqa: E501
        :type: Link
        """

        self.__self = _self

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
        if issubclass(DependentFlagsLinks, dict):
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
        if not isinstance(other, DependentFlagsLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
