# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EnvironmentApprovalSettings(object):
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
        'service_kind': 'str',
        'required': 'bool',
        'can_review_own_request': 'bool',
        'min_num_approvals': 'int',
        'can_apply_declined_changes': 'bool'
    }

    attribute_map = {
        'service_kind': 'serviceKind',
        'required': 'required',
        'can_review_own_request': 'canReviewOwnRequest',
        'min_num_approvals': 'minNumApprovals',
        'can_apply_declined_changes': 'canApplyDeclinedChanges'
    }

    def __init__(self, service_kind=None, required=None, can_review_own_request=None, min_num_approvals=None, can_apply_declined_changes=None):  # noqa: E501
        """EnvironmentApprovalSettings - a model defined in Swagger"""  # noqa: E501

        self._service_kind = None
        self._required = None
        self._can_review_own_request = None
        self._min_num_approvals = None
        self._can_apply_declined_changes = None
        self.discriminator = None

        if service_kind is not None:
            self.service_kind = service_kind
        if required is not None:
            self.required = required
        if can_review_own_request is not None:
            self.can_review_own_request = can_review_own_request
        if min_num_approvals is not None:
            self.min_num_approvals = min_num_approvals
        if can_apply_declined_changes is not None:
            self.can_apply_declined_changes = can_apply_declined_changes

    @property
    def service_kind(self):
        """Gets the service_kind of this EnvironmentApprovalSettings.  # noqa: E501

        The approvals system used.  # noqa: E501

        :return: The service_kind of this EnvironmentApprovalSettings.  # noqa: E501
        :rtype: str
        """
        return self._service_kind

    @service_kind.setter
    def service_kind(self, service_kind):
        """Sets the service_kind of this EnvironmentApprovalSettings.

        The approvals system used.  # noqa: E501

        :param service_kind: The service_kind of this EnvironmentApprovalSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["launchdarkly", "service-now"]  # noqa: E501
        if service_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `service_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(service_kind, allowed_values)
            )

        self._service_kind = service_kind

    @property
    def required(self):
        """Gets the required of this EnvironmentApprovalSettings.  # noqa: E501

        Whether any changes to flags in this environment will require approval.  # noqa: E501

        :return: The required of this EnvironmentApprovalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this EnvironmentApprovalSettings.

        Whether any changes to flags in this environment will require approval.  # noqa: E501

        :param required: The required of this EnvironmentApprovalSettings.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def can_review_own_request(self):
        """Gets the can_review_own_request of this EnvironmentApprovalSettings.  # noqa: E501

        Whether requesters can approve or decline their own request. They may always comment.  # noqa: E501

        :return: The can_review_own_request of this EnvironmentApprovalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._can_review_own_request

    @can_review_own_request.setter
    def can_review_own_request(self, can_review_own_request):
        """Sets the can_review_own_request of this EnvironmentApprovalSettings.

        Whether requesters can approve or decline their own request. They may always comment.  # noqa: E501

        :param can_review_own_request: The can_review_own_request of this EnvironmentApprovalSettings.  # noqa: E501
        :type: bool
        """

        self._can_review_own_request = can_review_own_request

    @property
    def min_num_approvals(self):
        """Gets the min_num_approvals of this EnvironmentApprovalSettings.  # noqa: E501

        The number of approvals required before an approval request can be applied.  # noqa: E501

        :return: The min_num_approvals of this EnvironmentApprovalSettings.  # noqa: E501
        :rtype: int
        """
        return self._min_num_approvals

    @min_num_approvals.setter
    def min_num_approvals(self, min_num_approvals):
        """Sets the min_num_approvals of this EnvironmentApprovalSettings.

        The number of approvals required before an approval request can be applied.  # noqa: E501

        :param min_num_approvals: The min_num_approvals of this EnvironmentApprovalSettings.  # noqa: E501
        :type: int
        """

        self._min_num_approvals = min_num_approvals

    @property
    def can_apply_declined_changes(self):
        """Gets the can_apply_declined_changes of this EnvironmentApprovalSettings.  # noqa: E501

        Whether changes can be applied as long as minNumApprovals is met, regardless of if any reviewers have declined a request.  # noqa: E501

        :return: The can_apply_declined_changes of this EnvironmentApprovalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_declined_changes

    @can_apply_declined_changes.setter
    def can_apply_declined_changes(self, can_apply_declined_changes):
        """Sets the can_apply_declined_changes of this EnvironmentApprovalSettings.

        Whether changes can be applied as long as minNumApprovals is met, regardless of if any reviewers have declined a request.  # noqa: E501

        :param can_apply_declined_changes: The can_apply_declined_changes of this EnvironmentApprovalSettings.  # noqa: E501
        :type: bool
        """

        self._can_apply_declined_changes = can_apply_declined_changes

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
        if issubclass(EnvironmentApprovalSettings, dict):
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
        if not isinstance(other, EnvironmentApprovalSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
