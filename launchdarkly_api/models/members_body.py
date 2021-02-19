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

from launchdarkly_api.models.role import Role  # noqa: F401,E501
from launchdarkly_api.models.statement import Statement  # noqa: F401,E501


class MembersBody(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'role': 'Role',
        'custom_roles': 'list[str]',
        'inline_role': 'list[Statement]'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'role': 'role',
        'custom_roles': 'customRoles',
        'inline_role': 'inlineRole'
    }

    def __init__(self, email=None, first_name=None, last_name=None, role=None, custom_roles=None, inline_role=None):  # noqa: E501
        """MembersBody - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._role = None
        self._custom_roles = None
        self._inline_role = None
        self.discriminator = None

        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if role is not None:
            self.role = role
        if custom_roles is not None:
            self.custom_roles = custom_roles
        if inline_role is not None:
            self.inline_role = inline_role

    @property
    def email(self):
        """Gets the email of this MembersBody.  # noqa: E501


        :return: The email of this MembersBody.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MembersBody.


        :param email: The email of this MembersBody.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this MembersBody.  # noqa: E501


        :return: The first_name of this MembersBody.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MembersBody.


        :param first_name: The first_name of this MembersBody.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MembersBody.  # noqa: E501


        :return: The last_name of this MembersBody.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MembersBody.


        :param last_name: The last_name of this MembersBody.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def role(self):
        """Gets the role of this MembersBody.  # noqa: E501


        :return: The role of this MembersBody.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MembersBody.


        :param role: The role of this MembersBody.  # noqa: E501
        :type: Role
        """

        self._role = role

    @property
    def custom_roles(self):
        """Gets the custom_roles of this MembersBody.  # noqa: E501


        :return: The custom_roles of this MembersBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_roles

    @custom_roles.setter
    def custom_roles(self, custom_roles):
        """Sets the custom_roles of this MembersBody.


        :param custom_roles: The custom_roles of this MembersBody.  # noqa: E501
        :type: list[str]
        """

        self._custom_roles = custom_roles

    @property
    def inline_role(self):
        """Gets the inline_role of this MembersBody.  # noqa: E501


        :return: The inline_role of this MembersBody.  # noqa: E501
        :rtype: list[Statement]
        """
        return self._inline_role

    @inline_role.setter
    def inline_role(self, inline_role):
        """Sets the inline_role of this MembersBody.


        :param inline_role: The inline_role of this MembersBody.  # noqa: E501
        :type: list[Statement]
        """

        self._inline_role = inline_role

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
        if issubclass(MembersBody, dict):
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
        if not isinstance(other, MembersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
