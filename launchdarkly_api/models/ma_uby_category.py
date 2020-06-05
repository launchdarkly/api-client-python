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

from launchdarkly_api.models.mau_metadata import MAUMetadata  # noqa: F401,E501
from launchdarkly_api.models.stream_by_sdk_links import StreamBySDKLinks  # noqa: F401,E501
from launchdarkly_api.models.stream_usage_series import StreamUsageSeries  # noqa: F401,E501


class MAUbyCategory(object):
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
        'links': 'StreamBySDKLinks',
        'metadata': 'list[MAUMetadata]',
        'series': 'list[StreamUsageSeries]'
    }

    attribute_map = {
        'links': '_links',
        'metadata': 'metadata',
        'series': 'series'
    }

    def __init__(self, links=None, metadata=None, series=None):  # noqa: E501
        """MAUbyCategory - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._metadata = None
        self._series = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata
        if series is not None:
            self.series = series

    @property
    def links(self):
        """Gets the links of this MAUbyCategory.  # noqa: E501


        :return: The links of this MAUbyCategory.  # noqa: E501
        :rtype: StreamBySDKLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MAUbyCategory.


        :param links: The links of this MAUbyCategory.  # noqa: E501
        :type: StreamBySDKLinks
        """

        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this MAUbyCategory.  # noqa: E501


        :return: The metadata of this MAUbyCategory.  # noqa: E501
        :rtype: list[MAUMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MAUbyCategory.


        :param metadata: The metadata of this MAUbyCategory.  # noqa: E501
        :type: list[MAUMetadata]
        """

        self._metadata = metadata

    @property
    def series(self):
        """Gets the series of this MAUbyCategory.  # noqa: E501


        :return: The series of this MAUbyCategory.  # noqa: E501
        :rtype: list[StreamUsageSeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this MAUbyCategory.


        :param series: The series of this MAUbyCategory.  # noqa: E501
        :type: list[StreamUsageSeries]
        """

        self._series = series

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
        if issubclass(MAUbyCategory, dict):
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
        if not isinstance(other, MAUbyCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
