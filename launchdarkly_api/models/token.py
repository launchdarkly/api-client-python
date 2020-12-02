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

from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.member import Member  # noqa: F401,E501
from launchdarkly_api.models.statement import Statement  # noqa: F401,E501


class Token(object):
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
        'links': 'Links',
        'id': 'Id',
        'owner_id': 'Id',
        'member_id': 'Id',
        'member': 'Member',
        'creation_date': 'int',
        'last_modified': 'int',
        'last_used': 'int',
        'token': 'str',
        'name': 'str',
        'role': 'str',
        'custom_role_ids': 'list[str]',
        'inline_role': 'list[Statement]',
        'service_token': 'bool',
        'default_api_version': 'int'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'owner_id': 'ownerId',
        'member_id': 'memberId',
        'member': '_member',
        'creation_date': 'creationDate',
        'last_modified': 'lastModified',
        'last_used': 'lastUsed',
        'token': 'token',
        'name': 'name',
        'role': 'role',
        'custom_role_ids': 'customRoleIds',
        'inline_role': 'inlineRole',
        'service_token': 'serviceToken',
        'default_api_version': 'defaultApiVersion'
    }

    def __init__(self, links=None, id=None, owner_id=None, member_id=None, member=None, creation_date=None, last_modified=None, last_used=None, token=None, name=None, role=None, custom_role_ids=None, inline_role=None, service_token=None, default_api_version=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._owner_id = None
        self._member_id = None
        self._member = None
        self._creation_date = None
        self._last_modified = None
        self._last_used = None
        self._token = None
        self._name = None
        self._role = None
        self._custom_role_ids = None
        self._inline_role = None
        self._service_token = None
        self._default_api_version = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if member_id is not None:
            self.member_id = member_id
        if member is not None:
            self.member = member
        if creation_date is not None:
            self.creation_date = creation_date
        if last_modified is not None:
            self.last_modified = last_modified
        if last_used is not None:
            self.last_used = last_used
        if token is not None:
            self.token = token
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
    def links(self):
        """Gets the links of this Token.  # noqa: E501


        :return: The links of this Token.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Token.


        :param links: The links of this Token.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Token.  # noqa: E501


        :return: The id of this Token.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Token.


        :param id: The id of this Token.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this Token.  # noqa: E501


        :return: The owner_id of this Token.  # noqa: E501
        :rtype: Id
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Token.


        :param owner_id: The owner_id of this Token.  # noqa: E501
        :type: Id
        """

        self._owner_id = owner_id

    @property
    def member_id(self):
        """Gets the member_id of this Token.  # noqa: E501


        :return: The member_id of this Token.  # noqa: E501
        :rtype: Id
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this Token.


        :param member_id: The member_id of this Token.  # noqa: E501
        :type: Id
        """

        self._member_id = member_id

    @property
    def member(self):
        """Gets the member of this Token.  # noqa: E501


        :return: The member of this Token.  # noqa: E501
        :rtype: Member
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Token.


        :param member: The member of this Token.  # noqa: E501
        :type: Member
        """

        self._member = member

    @property
    def creation_date(self):
        """Gets the creation_date of this Token.  # noqa: E501

        A unix epoch time in milliseconds specifying the creation time of this access token.  # noqa: E501

        :return: The creation_date of this Token.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Token.

        A unix epoch time in milliseconds specifying the creation time of this access token.  # noqa: E501

        :param creation_date: The creation_date of this Token.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def last_modified(self):
        """Gets the last_modified of this Token.  # noqa: E501

        A unix epoch time in milliseconds specifying the last time this access token was modified.  # noqa: E501

        :return: The last_modified of this Token.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Token.

        A unix epoch time in milliseconds specifying the last time this access token was modified.  # noqa: E501

        :param last_modified: The last_modified of this Token.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def last_used(self):
        """Gets the last_used of this Token.  # noqa: E501

        A unix epoch time in milliseconds specifying the last time this access token was used to authorize access to the LaunchDarkly REST API.  # noqa: E501

        :return: The last_used of this Token.  # noqa: E501
        :rtype: int
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this Token.

        A unix epoch time in milliseconds specifying the last time this access token was used to authorize access to the LaunchDarkly REST API.  # noqa: E501

        :param last_used: The last_used of this Token.  # noqa: E501
        :type: int
        """

        self._last_used = last_used

    @property
    def token(self):
        """Gets the token of this Token.  # noqa: E501

        The last 4 digits of the unique secret key for this access token. If creating or resetting the token, this will be the full token secret.  # noqa: E501

        :return: The token of this Token.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Token.

        The last 4 digits of the unique secret key for this access token. If creating or resetting the token, this will be the full token secret.  # noqa: E501

        :param token: The token of this Token.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def name(self):
        """Gets the name of this Token.  # noqa: E501

        A human-friendly name for the access token  # noqa: E501

        :return: The name of this Token.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Token.

        A human-friendly name for the access token  # noqa: E501

        :param name: The name of this Token.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this Token.  # noqa: E501

        The name of a built-in role for the token  # noqa: E501

        :return: The role of this Token.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Token.

        The name of a built-in role for the token  # noqa: E501

        :param role: The role of this Token.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def custom_role_ids(self):
        """Gets the custom_role_ids of this Token.  # noqa: E501

        A list of custom role IDs to use as access limits for the access token  # noqa: E501

        :return: The custom_role_ids of this Token.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_role_ids

    @custom_role_ids.setter
    def custom_role_ids(self, custom_role_ids):
        """Sets the custom_role_ids of this Token.

        A list of custom role IDs to use as access limits for the access token  # noqa: E501

        :param custom_role_ids: The custom_role_ids of this Token.  # noqa: E501
        :type: list[str]
        """

        self._custom_role_ids = custom_role_ids

    @property
    def inline_role(self):
        """Gets the inline_role of this Token.  # noqa: E501


        :return: The inline_role of this Token.  # noqa: E501
        :rtype: list[Statement]
        """
        return self._inline_role

    @inline_role.setter
    def inline_role(self, inline_role):
        """Sets the inline_role of this Token.


        :param inline_role: The inline_role of this Token.  # noqa: E501
        :type: list[Statement]
        """

        self._inline_role = inline_role

    @property
    def service_token(self):
        """Gets the service_token of this Token.  # noqa: E501

        Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens  # noqa: E501

        :return: The service_token of this Token.  # noqa: E501
        :rtype: bool
        """
        return self._service_token

    @service_token.setter
    def service_token(self, service_token):
        """Sets the service_token of this Token.

        Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens  # noqa: E501

        :param service_token: The service_token of this Token.  # noqa: E501
        :type: bool
        """

        self._service_token = service_token

    @property
    def default_api_version(self):
        """Gets the default_api_version of this Token.  # noqa: E501

        The default API version for this token  # noqa: E501

        :return: The default_api_version of this Token.  # noqa: E501
        :rtype: int
        """
        return self._default_api_version

    @default_api_version.setter
    def default_api_version(self, default_api_version):
        """Sets the default_api_version of this Token.

        The default API version for this token  # noqa: E501

        :param default_api_version: The default_api_version of this Token.  # noqa: E501
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
        if issubclass(Token, dict):
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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
