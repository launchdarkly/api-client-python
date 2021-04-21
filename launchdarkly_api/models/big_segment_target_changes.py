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


class BigSegmentTargetChanges(object):
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
        'add': 'list[str]',
        'remove': 'list[str]'
    }

    attribute_map = {
        'add': 'add',
        'remove': 'remove'
    }

    def __init__(self, add=None, remove=None):  # noqa: E501
        """BigSegmentTargetChanges - a model defined in Swagger"""  # noqa: E501

        self._add = None
        self._remove = None
        self.discriminator = None

        if add is not None:
            self.add = add
        if remove is not None:
            self.remove = remove

    @property
    def add(self):
        """Gets the add of this BigSegmentTargetChanges.  # noqa: E501

        Users to add to this list of targets  # noqa: E501

        :return: The add of this BigSegmentTargetChanges.  # noqa: E501
        :rtype: list[str]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this BigSegmentTargetChanges.

        Users to add to this list of targets  # noqa: E501

        :param add: The add of this BigSegmentTargetChanges.  # noqa: E501
        :type: list[str]
        """

        self._add = add

    @property
    def remove(self):
        """Gets the remove of this BigSegmentTargetChanges.  # noqa: E501

        Users to remove from this list of targets  # noqa: E501

        :return: The remove of this BigSegmentTargetChanges.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """Sets the remove of this BigSegmentTargetChanges.

        Users to remove from this list of targets  # noqa: E501

        :param remove: The remove of this BigSegmentTargetChanges.  # noqa: E501
        :type: list[str]
        """

        self._remove = remove

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
        if issubclass(BigSegmentTargetChanges, dict):
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
        if not isinstance(other, BigSegmentTargetChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
