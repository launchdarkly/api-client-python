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


class MultiEnvironmentDependentFlag(object):
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
        'environments': 'list[DependentFlagEnvironment]',
        'links': 'DependentFlagsLinks',
        'site': 'Site'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'environments': 'environments',
        'links': '_links',
        'site': '_site'
    }

    def __init__(self, name=None, key=None, environments=None, links=None, site=None):  # noqa: E501
        """MultiEnvironmentDependentFlag - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._environments = None
        self._links = None
        self._site = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if environments is not None:
            self.environments = environments
        if links is not None:
            self.links = links
        if site is not None:
            self.site = site

    @property
    def name(self):
        """Gets the name of this MultiEnvironmentDependentFlag.  # noqa: E501


        :return: The name of this MultiEnvironmentDependentFlag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MultiEnvironmentDependentFlag.


        :param name: The name of this MultiEnvironmentDependentFlag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this MultiEnvironmentDependentFlag.  # noqa: E501


        :return: The key of this MultiEnvironmentDependentFlag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MultiEnvironmentDependentFlag.


        :param key: The key of this MultiEnvironmentDependentFlag.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def environments(self):
        """Gets the environments of this MultiEnvironmentDependentFlag.  # noqa: E501


        :return: The environments of this MultiEnvironmentDependentFlag.  # noqa: E501
        :rtype: list[DependentFlagEnvironment]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this MultiEnvironmentDependentFlag.


        :param environments: The environments of this MultiEnvironmentDependentFlag.  # noqa: E501
        :type: list[DependentFlagEnvironment]
        """

        self._environments = environments

    @property
    def links(self):
        """Gets the links of this MultiEnvironmentDependentFlag.  # noqa: E501


        :return: The links of this MultiEnvironmentDependentFlag.  # noqa: E501
        :rtype: DependentFlagsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MultiEnvironmentDependentFlag.


        :param links: The links of this MultiEnvironmentDependentFlag.  # noqa: E501
        :type: DependentFlagsLinks
        """

        self._links = links

    @property
    def site(self):
        """Gets the site of this MultiEnvironmentDependentFlag.  # noqa: E501


        :return: The site of this MultiEnvironmentDependentFlag.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this MultiEnvironmentDependentFlag.


        :param site: The site of this MultiEnvironmentDependentFlag.  # noqa: E501
        :type: Site
        """

        self._site = site

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
        if issubclass(MultiEnvironmentDependentFlag, dict):
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
        if not isinstance(other, MultiEnvironmentDependentFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
