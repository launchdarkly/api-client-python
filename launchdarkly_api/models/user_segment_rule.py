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

from launchdarkly_api.models.clause import Clause  # noqa: F401,E501


class UserSegmentRule(object):
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
        'clauses': 'list[Clause]',
        'weight': 'int',
        'bucket_by': 'str'
    }

    attribute_map = {
        'clauses': 'clauses',
        'weight': 'weight',
        'bucket_by': 'bucketBy'
    }

    def __init__(self, clauses=None, weight=None, bucket_by=None):  # noqa: E501
        """UserSegmentRule - a model defined in Swagger"""  # noqa: E501

        self._clauses = None
        self._weight = None
        self._bucket_by = None
        self.discriminator = None

        if clauses is not None:
            self.clauses = clauses
        if weight is not None:
            self.weight = weight
        if bucket_by is not None:
            self.bucket_by = bucket_by

    @property
    def clauses(self):
        """Gets the clauses of this UserSegmentRule.  # noqa: E501


        :return: The clauses of this UserSegmentRule.  # noqa: E501
        :rtype: list[Clause]
        """
        return self._clauses

    @clauses.setter
    def clauses(self, clauses):
        """Sets the clauses of this UserSegmentRule.


        :param clauses: The clauses of this UserSegmentRule.  # noqa: E501
        :type: list[Clause]
        """

        self._clauses = clauses

    @property
    def weight(self):
        """Gets the weight of this UserSegmentRule.  # noqa: E501


        :return: The weight of this UserSegmentRule.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this UserSegmentRule.


        :param weight: The weight of this UserSegmentRule.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def bucket_by(self):
        """Gets the bucket_by of this UserSegmentRule.  # noqa: E501


        :return: The bucket_by of this UserSegmentRule.  # noqa: E501
        :rtype: str
        """
        return self._bucket_by

    @bucket_by.setter
    def bucket_by(self, bucket_by):
        """Sets the bucket_by of this UserSegmentRule.


        :param bucket_by: The bucket_by of this UserSegmentRule.  # noqa: E501
        :type: str
        """

        self._bucket_by = bucket_by

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
        if issubclass(UserSegmentRule, dict):
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
        if not isinstance(other, UserSegmentRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
