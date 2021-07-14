# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.3.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TokenBody(object):
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
        'role': 'str',
        'custom_role_ids': 'list[str]',
        'inline_role': 'list[Statement]',
        'service_token': 'bool',
        'default_api_version': 'int'
    }

    attribute_map = {
        'name': 'name',
        'role': 'role',
        'custom_role_ids': 'customRoleIds',
        'inline_role': 'inlineRole',
        'service_token': 'serviceToken',
        'default_api_version': 'defaultApiVersion'
    }

    def __init__(self, name=None, role=None, custom_role_ids=None, inline_role=None, service_token=None, default_api_version=None):  # noqa: E501
        """TokenBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._role = None
        self._custom_role_ids = None
        self._inline_role = None
        self._service_token = None
        self._default_api_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if custom_role_ids is not None:
            self.custom_role_ids = custom_role_ids
        if inline_role is not None:
            self.inline_role = inline_role
        if service_token is not None:
            self.service_token = service_token
        if default_api_version is not None:
            self.default_api_version = default_api_version

    @property
    def name(self):
        """Gets the name of this TokenBody.  # noqa: E501

        A human-friendly name for the access token  # noqa: E501

        :return: The name of this TokenBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenBody.

        A human-friendly name for the access token  # noqa: E501

        :param name: The name of this TokenBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this TokenBody.  # noqa: E501

        The name of a built-in role for the token  # noqa: E501

        :return: The role of this TokenBody.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TokenBody.

        The name of a built-in role for the token  # noqa: E501

        :param role: The role of this TokenBody.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def custom_role_ids(self):
        """Gets the custom_role_ids of this TokenBody.  # noqa: E501

        A list of custom role IDs to use as access limits for the access token  # noqa: E501

        :return: The custom_role_ids of this TokenBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_role_ids

    @custom_role_ids.setter
    def custom_role_ids(self, custom_role_ids):
        """Sets the custom_role_ids of this TokenBody.

        A list of custom role IDs to use as access limits for the access token  # noqa: E501

        :param custom_role_ids: The custom_role_ids of this TokenBody.  # noqa: E501
        :type: list[str]
        """

        self._custom_role_ids = custom_role_ids

    @property
    def inline_role(self):
        """Gets the inline_role of this TokenBody.  # noqa: E501


        :return: The inline_role of this TokenBody.  # noqa: E501
        :rtype: list[Statement]
        """
        return self._inline_role

    @inline_role.setter
    def inline_role(self, inline_role):
        """Sets the inline_role of this TokenBody.


        :param inline_role: The inline_role of this TokenBody.  # noqa: E501
        :type: list[Statement]
        """

        self._inline_role = inline_role

    @property
    def service_token(self):
        """Gets the service_token of this TokenBody.  # noqa: E501

        Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens  # noqa: E501

        :return: The service_token of this TokenBody.  # noqa: E501
        :rtype: bool
        """
        return self._service_token

    @service_token.setter
    def service_token(self, service_token):
        """Sets the service_token of this TokenBody.

        Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens  # noqa: E501

        :param service_token: The service_token of this TokenBody.  # noqa: E501
        :type: bool
        """

        self._service_token = service_token

    @property
    def default_api_version(self):
        """Gets the default_api_version of this TokenBody.  # noqa: E501

        The default API version for this token  # noqa: E501

        :return: The default_api_version of this TokenBody.  # noqa: E501
        :rtype: int
        """
        return self._default_api_version

    @default_api_version.setter
    def default_api_version(self, default_api_version):
        """Sets the default_api_version of this TokenBody.

        The default API version for this token  # noqa: E501

        :param default_api_version: The default_api_version of this TokenBody.  # noqa: E501
        :type: int
        """

        self._default_api_version = default_api_version

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
        if issubclass(TokenBody, dict):
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
        if not isinstance(other, TokenBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
