# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.3.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PatchOperation(object):
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
        'op': 'str',
        'path': 'str',
        'value': 'object'
    }

    attribute_map = {
        'op': 'op',
        'path': 'path',
        'value': 'value'
    }

    def __init__(self, op=None, path=None, value=None):  # noqa: E501
        """PatchOperation - a model defined in Swagger"""  # noqa: E501

        self._op = None
        self._path = None
        self._value = None
        self.discriminator = None

        self.op = op
        self.path = path
        self.value = value

    @property
    def op(self):
        """Gets the op of this PatchOperation.  # noqa: E501


        :return: The op of this PatchOperation.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this PatchOperation.


        :param op: The op of this PatchOperation.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501

        self._op = op

    @property
    def path(self):
        """Gets the path of this PatchOperation.  # noqa: E501


        :return: The path of this PatchOperation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PatchOperation.


        :param path: The path of this PatchOperation.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def value(self):
        """Gets the value of this PatchOperation.  # noqa: E501


        :return: The value of this PatchOperation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PatchOperation.


        :param value: The value of this PatchOperation.  # noqa: E501
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
        if issubclass(PatchOperation, dict):
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
        if not isinstance(other, PatchOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
