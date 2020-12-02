# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.feature_flag_change_request_review import FeatureFlagChangeRequestReview  # noqa: F401,E501
from launchdarkly_api.models.feature_flag_change_request_review_status import FeatureFlagChangeRequestReviewStatus  # noqa: F401,E501
from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.semantic_patch_instruction import SemanticPatchInstruction  # noqa: F401,E501


class FeatureFlagChangeRequest(object):
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
        'id': 'Id',
        'version': 'int',
        'creation_date': 'int',
        'requestor_id': 'str',
        'review_status': 'FeatureFlagChangeRequestReviewStatus',
        'status': 'str',
        'applied_by_member_id': 'str',
        'applied_date': 'int',
        'current_reviews_by_member_id': 'FeatureFlagChangeRequestReview',
        'all_reviews': 'list[FeatureFlagChangeRequestReview]',
        'notify_member_ids': 'list[str]',
        'instructions': 'SemanticPatchInstruction'
    }

    attribute_map = {
        'id': '_id',
        'version': '_version',
        'creation_date': 'creationDate',
        'requestor_id': 'requestorId',
        'review_status': 'reviewStatus',
        'status': 'status',
        'applied_by_member_id': 'appliedByMemberID',
        'applied_date': 'appliedDate',
        'current_reviews_by_member_id': 'currentReviewsByMemberId',
        'all_reviews': 'allReviews',
        'notify_member_ids': 'notifyMemberIds',
        'instructions': 'instructions'
    }

    def __init__(self, id=None, version=None, creation_date=None, requestor_id=None, review_status=None, status=None, applied_by_member_id=None, applied_date=None, current_reviews_by_member_id=None, all_reviews=None, notify_member_ids=None, instructions=None):  # noqa: E501
        """FeatureFlagChangeRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._version = None
        self._creation_date = None
        self._requestor_id = None
        self._review_status = None
        self._status = None
        self._applied_by_member_id = None
        self._applied_date = None
        self._current_reviews_by_member_id = None
        self._all_reviews = None
        self._notify_member_ids = None
        self._instructions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if creation_date is not None:
            self.creation_date = creation_date
        if requestor_id is not None:
            self.requestor_id = requestor_id
        if review_status is not None:
            self.review_status = review_status
        if status is not None:
            self.status = status
        if applied_by_member_id is not None:
            self.applied_by_member_id = applied_by_member_id
        if applied_date is not None:
            self.applied_date = applied_date
        if current_reviews_by_member_id is not None:
            self.current_reviews_by_member_id = current_reviews_by_member_id
        if all_reviews is not None:
            self.all_reviews = all_reviews
        if notify_member_ids is not None:
            self.notify_member_ids = notify_member_ids
        if instructions is not None:
            self.instructions = instructions

    @property
    def id(self):
        """Gets the id of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The id of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeatureFlagChangeRequest.


        :param id: The id of this FeatureFlagChangeRequest.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The version of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeatureFlagChangeRequest.


        :param version: The version of this FeatureFlagChangeRequest.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def creation_date(self):
        """Gets the creation_date of this FeatureFlagChangeRequest.  # noqa: E501

        A unix epoch time in milliseconds specifying the date the change request was requested  # noqa: E501

        :return: The creation_date of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FeatureFlagChangeRequest.

        A unix epoch time in milliseconds specifying the date the change request was requested  # noqa: E501

        :param creation_date: The creation_date of this FeatureFlagChangeRequest.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def requestor_id(self):
        """Gets the requestor_id of this FeatureFlagChangeRequest.  # noqa: E501

        The id of the member that requested the change  # noqa: E501

        :return: The requestor_id of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """Sets the requestor_id of this FeatureFlagChangeRequest.

        The id of the member that requested the change  # noqa: E501

        :param requestor_id: The requestor_id of this FeatureFlagChangeRequest.  # noqa: E501
        :type: str
        """

        self._requestor_id = requestor_id

    @property
    def review_status(self):
        """Gets the review_status of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The review_status of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: FeatureFlagChangeRequestReviewStatus
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this FeatureFlagChangeRequest.


        :param review_status: The review_status of this FeatureFlagChangeRequest.  # noqa: E501
        :type: FeatureFlagChangeRequestReviewStatus
        """

        self._review_status = review_status

    @property
    def status(self):
        """Gets the status of this FeatureFlagChangeRequest.  # noqa: E501

        | Name     | Description | | --------:| ----------- | | pending  | the feature flag change request has not been applied yet | | completed| the feature flag change request has been applied successfully | | failed   | the feature flag change request has been applied but the changes were not applied successfully |   # noqa: E501

        :return: The status of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FeatureFlagChangeRequest.

        | Name     | Description | | --------:| ----------- | | pending  | the feature flag change request has not been applied yet | | completed| the feature flag change request has been applied successfully | | failed   | the feature flag change request has been applied but the changes were not applied successfully |   # noqa: E501

        :param status: The status of this FeatureFlagChangeRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "completed", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def applied_by_member_id(self):
        """Gets the applied_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501

        The id of the member that applied the change request  # noqa: E501

        :return: The applied_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._applied_by_member_id

    @applied_by_member_id.setter
    def applied_by_member_id(self, applied_by_member_id):
        """Sets the applied_by_member_id of this FeatureFlagChangeRequest.

        The id of the member that applied the change request  # noqa: E501

        :param applied_by_member_id: The applied_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501
        :type: str
        """

        self._applied_by_member_id = applied_by_member_id

    @property
    def applied_date(self):
        """Gets the applied_date of this FeatureFlagChangeRequest.  # noqa: E501

        A unix epoch time in milliseconds specifying the date the change request was applied  # noqa: E501

        :return: The applied_date of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: int
        """
        return self._applied_date

    @applied_date.setter
    def applied_date(self, applied_date):
        """Sets the applied_date of this FeatureFlagChangeRequest.

        A unix epoch time in milliseconds specifying the date the change request was applied  # noqa: E501

        :param applied_date: The applied_date of this FeatureFlagChangeRequest.  # noqa: E501
        :type: int
        """

        self._applied_date = applied_date

    @property
    def current_reviews_by_member_id(self):
        """Gets the current_reviews_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The current_reviews_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: FeatureFlagChangeRequestReview
        """
        return self._current_reviews_by_member_id

    @current_reviews_by_member_id.setter
    def current_reviews_by_member_id(self, current_reviews_by_member_id):
        """Sets the current_reviews_by_member_id of this FeatureFlagChangeRequest.


        :param current_reviews_by_member_id: The current_reviews_by_member_id of this FeatureFlagChangeRequest.  # noqa: E501
        :type: FeatureFlagChangeRequestReview
        """

        self._current_reviews_by_member_id = current_reviews_by_member_id

    @property
    def all_reviews(self):
        """Gets the all_reviews of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The all_reviews of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: list[FeatureFlagChangeRequestReview]
        """
        return self._all_reviews

    @all_reviews.setter
    def all_reviews(self, all_reviews):
        """Sets the all_reviews of this FeatureFlagChangeRequest.


        :param all_reviews: The all_reviews of this FeatureFlagChangeRequest.  # noqa: E501
        :type: list[FeatureFlagChangeRequestReview]
        """

        self._all_reviews = all_reviews

    @property
    def notify_member_ids(self):
        """Gets the notify_member_ids of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The notify_member_ids of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_member_ids

    @notify_member_ids.setter
    def notify_member_ids(self, notify_member_ids):
        """Sets the notify_member_ids of this FeatureFlagChangeRequest.


        :param notify_member_ids: The notify_member_ids of this FeatureFlagChangeRequest.  # noqa: E501
        :type: list[str]
        """

        self._notify_member_ids = notify_member_ids

    @property
    def instructions(self):
        """Gets the instructions of this FeatureFlagChangeRequest.  # noqa: E501


        :return: The instructions of this FeatureFlagChangeRequest.  # noqa: E501
        :rtype: SemanticPatchInstruction
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this FeatureFlagChangeRequest.


        :param instructions: The instructions of this FeatureFlagChangeRequest.  # noqa: E501
        :type: SemanticPatchInstruction
        """

        self._instructions = instructions

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
        if issubclass(FeatureFlagChangeRequest, dict):
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
        if not isinstance(other, FeatureFlagChangeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
