# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.0.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.unbounded_segment_target_changes import UnboundedSegmentTargetChanges  # noqa: F401,E501


class UnboundedSegmentTargetsBody(object):
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
        'included': 'UnboundedSegmentTargetChanges',
        'excluded': 'UnboundedSegmentTargetChanges'
    }

    attribute_map = {
        'included': 'included',
        'excluded': 'excluded'
    }

    def __init__(self, included=None, excluded=None):  # noqa: E501
        """UnboundedSegmentTargetsBody - a model defined in Swagger"""  # noqa: E501

        self._included = None
        self._excluded = None
        self.discriminator = None

        if included is not None:
            self.included = included
        if excluded is not None:
            self.excluded = excluded

    @property
    def included(self):
        """Gets the included of this UnboundedSegmentTargetsBody.  # noqa: E501


        :return: The included of this UnboundedSegmentTargetsBody.  # noqa: E501
        :rtype: UnboundedSegmentTargetChanges
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this UnboundedSegmentTargetsBody.


        :param included: The included of this UnboundedSegmentTargetsBody.  # noqa: E501
        :type: UnboundedSegmentTargetChanges
        """

        self._included = included

    @property
    def excluded(self):
        """Gets the excluded of this UnboundedSegmentTargetsBody.  # noqa: E501


        :return: The excluded of this UnboundedSegmentTargetsBody.  # noqa: E501
        :rtype: UnboundedSegmentTargetChanges
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this UnboundedSegmentTargetsBody.


        :param excluded: The excluded of this UnboundedSegmentTargetsBody.  # noqa: E501
        :type: UnboundedSegmentTargetChanges
        """

        self._excluded = excluded

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
        if issubclass(UnboundedSegmentTargetsBody, dict):
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
        if not isinstance(other, UnboundedSegmentTargetsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
