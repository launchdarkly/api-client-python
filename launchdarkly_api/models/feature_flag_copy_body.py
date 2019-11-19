# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.22
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.copy_actions import CopyActions  # noqa: F401,E501
from launchdarkly_api.models.feature_flag_copy_object import FeatureFlagCopyObject  # noqa: F401,E501


class FeatureFlagCopyBody(object):
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
        'source': 'FeatureFlagCopyObject',
        'target': 'FeatureFlagCopyObject',
        'comment': 'str',
        'included_actions': 'list[CopyActions]',
        'excluded_actions': 'list[CopyActions]'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target',
        'comment': 'comment',
        'included_actions': 'includedActions',
        'excluded_actions': 'excludedActions'
    }

    def __init__(self, source=None, target=None, comment=None, included_actions=None, excluded_actions=None):  # noqa: E501
        """FeatureFlagCopyBody - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._target = None
        self._comment = None
        self._included_actions = None
        self._excluded_actions = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if comment is not None:
            self.comment = comment
        if included_actions is not None:
            self.included_actions = included_actions
        if excluded_actions is not None:
            self.excluded_actions = excluded_actions

    @property
    def source(self):
        """Gets the source of this FeatureFlagCopyBody.  # noqa: E501


        :return: The source of this FeatureFlagCopyBody.  # noqa: E501
        :rtype: FeatureFlagCopyObject
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FeatureFlagCopyBody.


        :param source: The source of this FeatureFlagCopyBody.  # noqa: E501
        :type: FeatureFlagCopyObject
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this FeatureFlagCopyBody.  # noqa: E501


        :return: The target of this FeatureFlagCopyBody.  # noqa: E501
        :rtype: FeatureFlagCopyObject
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this FeatureFlagCopyBody.


        :param target: The target of this FeatureFlagCopyBody.  # noqa: E501
        :type: FeatureFlagCopyObject
        """

        self._target = target

    @property
    def comment(self):
        """Gets the comment of this FeatureFlagCopyBody.  # noqa: E501

        comment will be included in audit log item for change.  # noqa: E501

        :return: The comment of this FeatureFlagCopyBody.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this FeatureFlagCopyBody.

        comment will be included in audit log item for change.  # noqa: E501

        :param comment: The comment of this FeatureFlagCopyBody.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def included_actions(self):
        """Gets the included_actions of this FeatureFlagCopyBody.  # noqa: E501

        Define the parts of the flag configuration that will be copied.  # noqa: E501

        :return: The included_actions of this FeatureFlagCopyBody.  # noqa: E501
        :rtype: list[CopyActions]
        """
        return self._included_actions

    @included_actions.setter
    def included_actions(self, included_actions):
        """Sets the included_actions of this FeatureFlagCopyBody.

        Define the parts of the flag configuration that will be copied.  # noqa: E501

        :param included_actions: The included_actions of this FeatureFlagCopyBody.  # noqa: E501
        :type: list[CopyActions]
        """

        self._included_actions = included_actions

    @property
    def excluded_actions(self):
        """Gets the excluded_actions of this FeatureFlagCopyBody.  # noqa: E501

        Define the parts of the flag configuration that will not be copied.  # noqa: E501

        :return: The excluded_actions of this FeatureFlagCopyBody.  # noqa: E501
        :rtype: list[CopyActions]
        """
        return self._excluded_actions

    @excluded_actions.setter
    def excluded_actions(self, excluded_actions):
        """Sets the excluded_actions of this FeatureFlagCopyBody.

        Define the parts of the flag configuration that will not be copied.  # noqa: E501

        :param excluded_actions: The excluded_actions of this FeatureFlagCopyBody.  # noqa: E501
        :type: list[CopyActions]
        """

        self._excluded_actions = excluded_actions

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
        if issubclass(FeatureFlagCopyBody, dict):
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
        if not isinstance(other, FeatureFlagCopyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other