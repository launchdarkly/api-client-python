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


class FeatureFlagStatusAcrossEnvironments(object):
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
        'links': 'FeatureFlagStatusLinks',
        'key': 'str',
        'environments': 'dict(str, FeatureFlagStatusForQueriedEnvironment)'
    }

    attribute_map = {
        'links': '_links',
        'key': 'key',
        'environments': 'environments'
    }

    def __init__(self, links=None, key=None, environments=None):  # noqa: E501
        """FeatureFlagStatusAcrossEnvironments - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._key = None
        self._environments = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if key is not None:
            self.key = key
        if environments is not None:
            self.environments = environments

    @property
    def links(self):
        """Gets the links of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501


        :return: The links of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :rtype: FeatureFlagStatusLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureFlagStatusAcrossEnvironments.


        :param links: The links of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :type: FeatureFlagStatusLinks
        """

        self._links = links

    @property
    def key(self):
        """Gets the key of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501


        :return: The key of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FeatureFlagStatusAcrossEnvironments.


        :param key: The key of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def environments(self):
        """Gets the environments of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501


        :return: The environments of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :rtype: dict(str, FeatureFlagStatusForQueriedEnvironment)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this FeatureFlagStatusAcrossEnvironments.


        :param environments: The environments of this FeatureFlagStatusAcrossEnvironments.  # noqa: E501
        :type: dict(str, FeatureFlagStatusForQueriedEnvironment)
        """

        self._environments = environments

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
        if issubclass(FeatureFlagStatusAcrossEnvironments, dict):
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
        if not isinstance(other, FeatureFlagStatusAcrossEnvironments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
