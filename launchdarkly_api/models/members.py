# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.6.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.member import Member  # noqa: F401,E501


class Members(object):
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
        'links': 'Links',
        'items': 'list[Member]',
        'total_count': 'float'
    }

    attribute_map = {
        'links': '_links',
        'items': 'items',
        'total_count': 'totalCount'
    }

    def __init__(self, links=None, items=None, total_count=None):  # noqa: E501
        """Members - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._items = None
        self._total_count = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if items is not None:
            self.items = items
        if total_count is not None:
            self.total_count = total_count

    @property
    def links(self):
        """Gets the links of this Members.  # noqa: E501


        :return: The links of this Members.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Members.


        :param links: The links of this Members.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def items(self):
        """Gets the items of this Members.  # noqa: E501


        :return: The items of this Members.  # noqa: E501
        :rtype: list[Member]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Members.


        :param items: The items of this Members.  # noqa: E501
        :type: list[Member]
        """

        self._items = items

    @property
    def total_count(self):
        """Gets the total_count of this Members.  # noqa: E501


        :return: The total_count of this Members.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Members.


        :param total_count: The total_count of this Members.  # noqa: E501
        :type: float
        """

        self._total_count = total_count

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
        if issubclass(Members, dict):
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
        if not isinstance(other, Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
