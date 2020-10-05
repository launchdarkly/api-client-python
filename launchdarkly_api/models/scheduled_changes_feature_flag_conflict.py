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


class ScheduledChangesFeatureFlagConflict(object):
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
        'id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'id': '_id',
        'reason': 'reason'
    }

    def __init__(self, id=None, reason=None):  # noqa: E501
        """ScheduledChangesFeatureFlagConflict - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        """Gets the id of this ScheduledChangesFeatureFlagConflict.  # noqa: E501

        Feature flag scheduled change id this change will conflict with  # noqa: E501

        :return: The id of this ScheduledChangesFeatureFlagConflict.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledChangesFeatureFlagConflict.

        Feature flag scheduled change id this change will conflict with  # noqa: E501

        :param id: The id of this ScheduledChangesFeatureFlagConflict.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this ScheduledChangesFeatureFlagConflict.  # noqa: E501

        Feature flag scheduled change conflict reason  # noqa: E501

        :return: The reason of this ScheduledChangesFeatureFlagConflict.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ScheduledChangesFeatureFlagConflict.

        Feature flag scheduled change conflict reason  # noqa: E501

        :param reason: The reason of this ScheduledChangesFeatureFlagConflict.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(ScheduledChangesFeatureFlagConflict, dict):
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
        if not isinstance(other, ScheduledChangesFeatureFlagConflict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
