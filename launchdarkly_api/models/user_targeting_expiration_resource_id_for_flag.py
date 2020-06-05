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


class UserTargetingExpirationResourceIdForFlag(object):
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
        'kind': 'str',
        'project_key': 'str',
        'environment_key': 'str',
        'flag_key': 'str',
        'key': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'project_key': 'projectKey',
        'environment_key': 'environmentKey',
        'flag_key': 'flagKey',
        'key': 'key'
    }

    def __init__(self, kind=None, project_key=None, environment_key=None, flag_key=None, key=None):  # noqa: E501
        """UserTargetingExpirationResourceIdForFlag - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._project_key = None
        self._environment_key = None
        self._flag_key = None
        self._key = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if project_key is not None:
            self.project_key = project_key
        if environment_key is not None:
            self.environment_key = environment_key
        if flag_key is not None:
            self.flag_key = flag_key
        if key is not None:
            self.key = key

    @property
    def kind(self):
        """Gets the kind of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501


        :return: The kind of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this UserTargetingExpirationResourceIdForFlag.


        :param kind: The kind of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def project_key(self):
        """Gets the project_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501


        :return: The project_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :rtype: str
        """
        return self._project_key

    @project_key.setter
    def project_key(self, project_key):
        """Sets the project_key of this UserTargetingExpirationResourceIdForFlag.


        :param project_key: The project_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :type: str
        """

        self._project_key = project_key

    @property
    def environment_key(self):
        """Gets the environment_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501


        :return: The environment_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :rtype: str
        """
        return self._environment_key

    @environment_key.setter
    def environment_key(self, environment_key):
        """Sets the environment_key of this UserTargetingExpirationResourceIdForFlag.


        :param environment_key: The environment_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :type: str
        """

        self._environment_key = environment_key

    @property
    def flag_key(self):
        """Gets the flag_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501


        :return: The flag_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :rtype: str
        """
        return self._flag_key

    @flag_key.setter
    def flag_key(self, flag_key):
        """Sets the flag_key of this UserTargetingExpirationResourceIdForFlag.


        :param flag_key: The flag_key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :type: str
        """

        self._flag_key = flag_key

    @property
    def key(self):
        """Gets the key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501


        :return: The key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserTargetingExpirationResourceIdForFlag.


        :param key: The key of this UserTargetingExpirationResourceIdForFlag.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(UserTargetingExpirationResourceIdForFlag, dict):
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
        if not isinstance(other, UserTargetingExpirationResourceIdForFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
