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

from launchdarkly_api.models.flag_list_item import FlagListItem  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.user_segment_rule import UserSegmentRule  # noqa: F401,E501


class UserSegment(object):
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
        'key': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'creation_date': 'int',
        'included': 'list[str]',
        'excluded': 'list[str]',
        'rules': 'list[UserSegmentRule]',
        'unbounded': 'bool',
        'version': 'int',
        'links': 'Links',
        'flags': 'list[FlagListItem]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'creation_date': 'creationDate',
        'included': 'included',
        'excluded': 'excluded',
        'rules': 'rules',
        'unbounded': 'unbounded',
        'version': 'version',
        'links': '_links',
        'flags': '_flags'
    }

    def __init__(self, key=None, name=None, description=None, tags=None, creation_date=None, included=None, excluded=None, rules=None, unbounded=None, version=None, links=None, flags=None):  # noqa: E501
        """UserSegment - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._name = None
        self._description = None
        self._tags = None
        self._creation_date = None
        self._included = None
        self._excluded = None
        self._rules = None
        self._unbounded = None
        self._version = None
        self._links = None
        self._flags = None
        self.discriminator = None

        self.key = key
        self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        self.creation_date = creation_date
        if included is not None:
            self.included = included
        if excluded is not None:
            self.excluded = excluded
        if rules is not None:
            self.rules = rules
        if unbounded is not None:
            self.unbounded = unbounded
        if version is not None:
            self.version = version
        if links is not None:
            self.links = links
        if flags is not None:
            self.flags = flags

    @property
    def key(self):
        """Gets the key of this UserSegment.  # noqa: E501

        Unique identifier for the user segment.  # noqa: E501

        :return: The key of this UserSegment.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserSegment.

        Unique identifier for the user segment.  # noqa: E501

        :param key: The key of this UserSegment.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this UserSegment.  # noqa: E501

        Name of the user segment.  # noqa: E501

        :return: The name of this UserSegment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserSegment.

        Name of the user segment.  # noqa: E501

        :param name: The name of this UserSegment.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UserSegment.  # noqa: E501

        Description of the user segment.  # noqa: E501

        :return: The description of this UserSegment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserSegment.

        Description of the user segment.  # noqa: E501

        :param description: The description of this UserSegment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UserSegment.  # noqa: E501

        An array of tags for this user segment.  # noqa: E501

        :return: The tags of this UserSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UserSegment.

        An array of tags for this user segment.  # noqa: E501

        :param tags: The tags of this UserSegment.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def creation_date(self):
        """Gets the creation_date of this UserSegment.  # noqa: E501

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :return: The creation_date of this UserSegment.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserSegment.

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :param creation_date: The creation_date of this UserSegment.  # noqa: E501
        :type: int
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def included(self):
        """Gets the included of this UserSegment.  # noqa: E501

        An array of user keys that are included in this segment.  # noqa: E501

        :return: The included of this UserSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this UserSegment.

        An array of user keys that are included in this segment.  # noqa: E501

        :param included: The included of this UserSegment.  # noqa: E501
        :type: list[str]
        """

        self._included = included

    @property
    def excluded(self):
        """Gets the excluded of this UserSegment.  # noqa: E501

        An array of user keys that should not be included in this segment, unless they are also listed in \"included\".  # noqa: E501

        :return: The excluded of this UserSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this UserSegment.

        An array of user keys that should not be included in this segment, unless they are also listed in \"included\".  # noqa: E501

        :param excluded: The excluded of this UserSegment.  # noqa: E501
        :type: list[str]
        """

        self._excluded = excluded

    @property
    def rules(self):
        """Gets the rules of this UserSegment.  # noqa: E501

        An array of rules that can cause a user to be included in this segment.  # noqa: E501

        :return: The rules of this UserSegment.  # noqa: E501
        :rtype: list[UserSegmentRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UserSegment.

        An array of rules that can cause a user to be included in this segment.  # noqa: E501

        :param rules: The rules of this UserSegment.  # noqa: E501
        :type: list[UserSegmentRule]
        """

        self._rules = rules

    @property
    def unbounded(self):
        """Gets the unbounded of this UserSegment.  # noqa: E501

        Controls whether this segment can support unlimited numbers of users. Requires the beta API and additional setup. Include/exclude lists in this payload are not used in unbounded segments.  # noqa: E501

        :return: The unbounded of this UserSegment.  # noqa: E501
        :rtype: bool
        """
        return self._unbounded

    @unbounded.setter
    def unbounded(self, unbounded):
        """Sets the unbounded of this UserSegment.

        Controls whether this segment can support unlimited numbers of users. Requires the beta API and additional setup. Include/exclude lists in this payload are not used in unbounded segments.  # noqa: E501

        :param unbounded: The unbounded of this UserSegment.  # noqa: E501
        :type: bool
        """

        self._unbounded = unbounded

    @property
    def version(self):
        """Gets the version of this UserSegment.  # noqa: E501


        :return: The version of this UserSegment.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserSegment.


        :param version: The version of this UserSegment.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this UserSegment.  # noqa: E501


        :return: The links of this UserSegment.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserSegment.


        :param links: The links of this UserSegment.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def flags(self):
        """Gets the flags of this UserSegment.  # noqa: E501


        :return: The flags of this UserSegment.  # noqa: E501
        :rtype: list[FlagListItem]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this UserSegment.


        :param flags: The flags of this UserSegment.  # noqa: E501
        :type: list[FlagListItem]
        """

        self._flags = flags

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
        if issubclass(UserSegment, dict):
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
        if not isinstance(other, UserSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
