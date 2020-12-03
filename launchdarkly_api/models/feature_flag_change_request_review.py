# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.2
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.feature_flag_change_request_review_status import FeatureFlagChangeRequestReviewStatus  # noqa: F401,E501
from launchdarkly_api.models.id import Id  # noqa: F401,E501


class FeatureFlagChangeRequestReview(object):
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
        'creation_date': 'int',
        'kind': 'FeatureFlagChangeRequestReviewStatus',
        'member_id': 'Id',
        'id': 'Id'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'kind': 'kind',
        'member_id': 'memberId',
        'id': '_id'
    }

    def __init__(self, creation_date=None, kind=None, member_id=None, id=None):  # noqa: E501
        """FeatureFlagChangeRequestReview - a model defined in Swagger"""  # noqa: E501

        self._creation_date = None
        self._kind = None
        self._member_id = None
        self._id = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if kind is not None:
            self.kind = kind
        if member_id is not None:
            self.member_id = member_id
        if id is not None:
            self.id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this FeatureFlagChangeRequestReview.  # noqa: E501

        A unix epoch time in milliseconds specifying the date the change request was reviewed  # noqa: E501

        :return: The creation_date of this FeatureFlagChangeRequestReview.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FeatureFlagChangeRequestReview.

        A unix epoch time in milliseconds specifying the date the change request was reviewed  # noqa: E501

        :param creation_date: The creation_date of this FeatureFlagChangeRequestReview.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def kind(self):
        """Gets the kind of this FeatureFlagChangeRequestReview.  # noqa: E501


        :return: The kind of this FeatureFlagChangeRequestReview.  # noqa: E501
        :rtype: FeatureFlagChangeRequestReviewStatus
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this FeatureFlagChangeRequestReview.


        :param kind: The kind of this FeatureFlagChangeRequestReview.  # noqa: E501
        :type: FeatureFlagChangeRequestReviewStatus
        """

        self._kind = kind

    @property
    def member_id(self):
        """Gets the member_id of this FeatureFlagChangeRequestReview.  # noqa: E501


        :return: The member_id of this FeatureFlagChangeRequestReview.  # noqa: E501
        :rtype: Id
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this FeatureFlagChangeRequestReview.


        :param member_id: The member_id of this FeatureFlagChangeRequestReview.  # noqa: E501
        :type: Id
        """

        self._member_id = member_id

    @property
    def id(self):
        """Gets the id of this FeatureFlagChangeRequestReview.  # noqa: E501


        :return: The id of this FeatureFlagChangeRequestReview.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeatureFlagChangeRequestReview.


        :param id: The id of this FeatureFlagChangeRequestReview.  # noqa: E501
        :type: Id
        """

        self._id = id

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
        if issubclass(FeatureFlagChangeRequestReview, dict):
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
        if not isinstance(other, FeatureFlagChangeRequestReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
