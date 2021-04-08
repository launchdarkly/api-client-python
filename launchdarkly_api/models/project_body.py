# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.0.3
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProjectBody(object):
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
        'key': 'str',
        'include_in_snippet_by_default': 'bool',
        'tags': 'list[str]',
        'environments': 'list[EnvironmentPost]',
        'default_client_side_availability': 'ClientSideAvailability'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'include_in_snippet_by_default': 'includeInSnippetByDefault',
        'tags': 'tags',
        'environments': 'environments',
        'default_client_side_availability': 'defaultClientSideAvailability'
    }

    def __init__(self, name=None, key=None, include_in_snippet_by_default=None, tags=None, environments=None, default_client_side_availability=None):  # noqa: E501
        """ProjectBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._include_in_snippet_by_default = None
        self._tags = None
        self._environments = None
        self._default_client_side_availability = None
        self.discriminator = None

        self.name = name
        self.key = key
        if include_in_snippet_by_default is not None:
            self.include_in_snippet_by_default = include_in_snippet_by_default
        if tags is not None:
            self.tags = tags
        if environments is not None:
            self.environments = environments
        if default_client_side_availability is not None:
            self.default_client_side_availability = default_client_side_availability

    @property
    def name(self):
        """Gets the name of this ProjectBody.  # noqa: E501


        :return: The name of this ProjectBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectBody.


        :param name: The name of this ProjectBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this ProjectBody.  # noqa: E501


        :return: The key of this ProjectBody.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ProjectBody.


        :param key: The key of this ProjectBody.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def include_in_snippet_by_default(self):
        """Gets the include_in_snippet_by_default of this ProjectBody.  # noqa: E501


        :return: The include_in_snippet_by_default of this ProjectBody.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_snippet_by_default

    @include_in_snippet_by_default.setter
    def include_in_snippet_by_default(self, include_in_snippet_by_default):
        """Sets the include_in_snippet_by_default of this ProjectBody.


        :param include_in_snippet_by_default: The include_in_snippet_by_default of this ProjectBody.  # noqa: E501
        :type: bool
        """

        self._include_in_snippet_by_default = include_in_snippet_by_default

    @property
    def tags(self):
        """Gets the tags of this ProjectBody.  # noqa: E501


        :return: The tags of this ProjectBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProjectBody.


        :param tags: The tags of this ProjectBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def environments(self):
        """Gets the environments of this ProjectBody.  # noqa: E501


        :return: The environments of this ProjectBody.  # noqa: E501
        :rtype: list[EnvironmentPost]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this ProjectBody.


        :param environments: The environments of this ProjectBody.  # noqa: E501
        :type: list[EnvironmentPost]
        """

        self._environments = environments

    @property
    def default_client_side_availability(self):
        """Gets the default_client_side_availability of this ProjectBody.  # noqa: E501


        :return: The default_client_side_availability of this ProjectBody.  # noqa: E501
        :rtype: ClientSideAvailability
        """
        return self._default_client_side_availability

    @default_client_side_availability.setter
    def default_client_side_availability(self, default_client_side_availability):
        """Sets the default_client_side_availability of this ProjectBody.


        :param default_client_side_availability: The default_client_side_availability of this ProjectBody.  # noqa: E501
        :type: ClientSideAvailability
        """

        self._default_client_side_availability = default_client_side_availability

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
        if issubclass(ProjectBody, dict):
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
        if not isinstance(other, ProjectBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
