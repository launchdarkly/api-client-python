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


class UserSegmentBody(object):
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
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, key=None, description=None, tags=None):  # noqa: E501
        """UserSegmentBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.key = key
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this UserSegmentBody.  # noqa: E501

        A human-friendly name for the user segment.  # noqa: E501

        :return: The name of this UserSegmentBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserSegmentBody.

        A human-friendly name for the user segment.  # noqa: E501

        :param name: The name of this UserSegmentBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this UserSegmentBody.  # noqa: E501

        A unique key that will be used to reference the user segment in feature flags.  # noqa: E501

        :return: The key of this UserSegmentBody.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserSegmentBody.

        A unique key that will be used to reference the user segment in feature flags.  # noqa: E501

        :param key: The key of this UserSegmentBody.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def description(self):
        """Gets the description of this UserSegmentBody.  # noqa: E501

        A description for the user segment.  # noqa: E501

        :return: The description of this UserSegmentBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserSegmentBody.

        A description for the user segment.  # noqa: E501

        :param description: The description of this UserSegmentBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UserSegmentBody.  # noqa: E501

        Tags for the user segment.  # noqa: E501

        :return: The tags of this UserSegmentBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UserSegmentBody.

        Tags for the user segment.  # noqa: E501

        :param tags: The tags of this UserSegmentBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(UserSegmentBody, dict):
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
        if not isinstance(other, UserSegmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
