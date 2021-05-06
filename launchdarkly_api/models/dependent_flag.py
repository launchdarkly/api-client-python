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


class DependentFlag(object):
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
        'links': 'DependentFlagLinks',
        'site': 'Site'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'links': '_links',
        'site': '_site'
    }

    def __init__(self, name=None, key=None, links=None, site=None):  # noqa: E501
        """DependentFlag - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._links = None
        self._site = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if links is not None:
            self.links = links
        if site is not None:
            self.site = site

    @property
    def name(self):
        """Gets the name of this DependentFlag.  # noqa: E501


        :return: The name of this DependentFlag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DependentFlag.


        :param name: The name of this DependentFlag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this DependentFlag.  # noqa: E501


        :return: The key of this DependentFlag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DependentFlag.


        :param key: The key of this DependentFlag.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def links(self):
        """Gets the links of this DependentFlag.  # noqa: E501


        :return: The links of this DependentFlag.  # noqa: E501
        :rtype: DependentFlagLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DependentFlag.


        :param links: The links of this DependentFlag.  # noqa: E501
        :type: DependentFlagLinks
        """

        self._links = links

    @property
    def site(self):
        """Gets the site of this DependentFlag.  # noqa: E501


        :return: The site of this DependentFlag.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this DependentFlag.


        :param site: The site of this DependentFlag.  # noqa: E501
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
        if issubclass(DependentFlag, dict):
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
        if not isinstance(other, DependentFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other