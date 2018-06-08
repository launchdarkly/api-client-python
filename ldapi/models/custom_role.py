# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.2
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ldapi.models.custom_role_key_or_id import CustomRoleKeyOrId  # noqa: F401,E501
from ldapi.models.id import Id  # noqa: F401,E501
from ldapi.models.links import Links  # noqa: F401,E501
from ldapi.models.policy import Policy  # noqa: F401,E501


class CustomRole(object):
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
        'name': 'str',
        'key': 'CustomRoleKeyOrId',
        'description': 'str',
        'id': 'Id',
        'policy': 'list[Policy]'
    }

    attribute_map = {
        'links': '_links',
        'name': 'name',
        'key': 'key',
        'description': 'description',
        'id': '_id',
        'policy': 'policy'
    }

    def __init__(self, links=None, name=None, key=None, description=None, id=None, policy=None):  # noqa: E501
        """CustomRole - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._name = None
        self._key = None
        self._description = None
        self._id = None
        self._policy = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if policy is not None:
            self.policy = policy

    @property
    def links(self):
        """Gets the links of this CustomRole.  # noqa: E501


        :return: The links of this CustomRole.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CustomRole.


        :param links: The links of this CustomRole.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this CustomRole.  # noqa: E501

        Name of the custom role.  # noqa: E501

        :return: The name of this CustomRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomRole.

        Name of the custom role.  # noqa: E501

        :param name: The name of this CustomRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this CustomRole.  # noqa: E501


        :return: The key of this CustomRole.  # noqa: E501
        :rtype: CustomRoleKeyOrId
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CustomRole.


        :param key: The key of this CustomRole.  # noqa: E501
        :type: CustomRoleKeyOrId
        """

        self._key = key

    @property
    def description(self):
        """Gets the description of this CustomRole.  # noqa: E501

        Description of the custom role.  # noqa: E501

        :return: The description of this CustomRole.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomRole.

        Description of the custom role.  # noqa: E501

        :param description: The description of this CustomRole.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this CustomRole.  # noqa: E501


        :return: The id of this CustomRole.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomRole.


        :param id: The id of this CustomRole.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def policy(self):
        """Gets the policy of this CustomRole.  # noqa: E501


        :return: The policy of this CustomRole.  # noqa: E501
        :rtype: list[Policy]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CustomRole.


        :param policy: The policy of this CustomRole.  # noqa: E501
        :type: list[Policy]
        """

        self._policy = policy

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
