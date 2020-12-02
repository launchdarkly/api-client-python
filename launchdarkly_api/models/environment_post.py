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


class EnvironmentPost(object):
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
        'color': 'str',
        'default_ttl': 'float',
        'secure_mode': 'bool',
        'default_track_events': 'bool',
        'tags': 'list[str]',
        'require_comments': 'bool',
        'confirm_changes': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'color': 'color',
        'default_ttl': 'defaultTtl',
        'secure_mode': 'secureMode',
        'default_track_events': 'defaultTrackEvents',
        'tags': 'tags',
        'require_comments': 'requireComments',
        'confirm_changes': 'confirmChanges'
    }

    def __init__(self, name=None, key=None, color=None, default_ttl=None, secure_mode=None, default_track_events=None, tags=None, require_comments=None, confirm_changes=None):  # noqa: E501
        """EnvironmentPost - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._color = None
        self._default_ttl = None
        self._secure_mode = None
        self._default_track_events = None
        self._tags = None
        self._require_comments = None
        self._confirm_changes = None
        self.discriminator = None

        self.name = name
        self.key = key
        self.color = color
        if default_ttl is not None:
            self.default_ttl = default_ttl
        if secure_mode is not None:
            self.secure_mode = secure_mode
        if default_track_events is not None:
            self.default_track_events = default_track_events
        if tags is not None:
            self.tags = tags
        if require_comments is not None:
            self.require_comments = require_comments
        if confirm_changes is not None:
            self.confirm_changes = confirm_changes

    @property
    def name(self):
        """Gets the name of this EnvironmentPost.  # noqa: E501

        The name of the new environment.  # noqa: E501

        :return: The name of this EnvironmentPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentPost.

        The name of the new environment.  # noqa: E501

        :param name: The name of this EnvironmentPost.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this EnvironmentPost.  # noqa: E501

        A project-unique key for the new environment.  # noqa: E501

        :return: The key of this EnvironmentPost.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this EnvironmentPost.

        A project-unique key for the new environment.  # noqa: E501

        :param key: The key of this EnvironmentPost.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def color(self):
        """Gets the color of this EnvironmentPost.  # noqa: E501

        A color swatch (as an RGB hex value with no leading '#', e.g. C8C8C8).  # noqa: E501

        :return: The color of this EnvironmentPost.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EnvironmentPost.

        A color swatch (as an RGB hex value with no leading '#', e.g. C8C8C8).  # noqa: E501

        :param color: The color of this EnvironmentPost.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def default_ttl(self):
        """Gets the default_ttl of this EnvironmentPost.  # noqa: E501

        The default TTL for the new environment.  # noqa: E501

        :return: The default_ttl of this EnvironmentPost.  # noqa: E501
        :rtype: float
        """
        return self._default_ttl

    @default_ttl.setter
    def default_ttl(self, default_ttl):
        """Sets the default_ttl of this EnvironmentPost.

        The default TTL for the new environment.  # noqa: E501

        :param default_ttl: The default_ttl of this EnvironmentPost.  # noqa: E501
        :type: float
        """

        self._default_ttl = default_ttl

    @property
    def secure_mode(self):
        """Gets the secure_mode of this EnvironmentPost.  # noqa: E501

        Determines whether the environment is in secure mode.  # noqa: E501

        :return: The secure_mode of this EnvironmentPost.  # noqa: E501
        :rtype: bool
        """
        return self._secure_mode

    @secure_mode.setter
    def secure_mode(self, secure_mode):
        """Sets the secure_mode of this EnvironmentPost.

        Determines whether the environment is in secure mode.  # noqa: E501

        :param secure_mode: The secure_mode of this EnvironmentPost.  # noqa: E501
        :type: bool
        """

        self._secure_mode = secure_mode

    @property
    def default_track_events(self):
        """Gets the default_track_events of this EnvironmentPost.  # noqa: E501

        Set to true to send detailed event information for newly created flags.  # noqa: E501

        :return: The default_track_events of this EnvironmentPost.  # noqa: E501
        :rtype: bool
        """
        return self._default_track_events

    @default_track_events.setter
    def default_track_events(self, default_track_events):
        """Sets the default_track_events of this EnvironmentPost.

        Set to true to send detailed event information for newly created flags.  # noqa: E501

        :param default_track_events: The default_track_events of this EnvironmentPost.  # noqa: E501
        :type: bool
        """

        self._default_track_events = default_track_events

    @property
    def tags(self):
        """Gets the tags of this EnvironmentPost.  # noqa: E501

        An array of tags for this environment.  # noqa: E501

        :return: The tags of this EnvironmentPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EnvironmentPost.

        An array of tags for this environment.  # noqa: E501

        :param tags: The tags of this EnvironmentPost.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def require_comments(self):
        """Gets the require_comments of this EnvironmentPost.  # noqa: E501

        Determines if this environment requires comments for flag and segment changes.  # noqa: E501

        :return: The require_comments of this EnvironmentPost.  # noqa: E501
        :rtype: bool
        """
        return self._require_comments

    @require_comments.setter
    def require_comments(self, require_comments):
        """Sets the require_comments of this EnvironmentPost.

        Determines if this environment requires comments for flag and segment changes.  # noqa: E501

        :param require_comments: The require_comments of this EnvironmentPost.  # noqa: E501
        :type: bool
        """

        self._require_comments = require_comments

    @property
    def confirm_changes(self):
        """Gets the confirm_changes of this EnvironmentPost.  # noqa: E501

        Determines if this environment requires confirmation for flag and segment changes.  # noqa: E501

        :return: The confirm_changes of this EnvironmentPost.  # noqa: E501
        :rtype: bool
        """
        return self._confirm_changes

    @confirm_changes.setter
    def confirm_changes(self, confirm_changes):
        """Sets the confirm_changes of this EnvironmentPost.

        Determines if this environment requires confirmation for flag and segment changes.  # noqa: E501

        :param confirm_changes: The confirm_changes of this EnvironmentPost.  # noqa: E501
        :type: bool
        """

        self._confirm_changes = confirm_changes

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
        if issubclass(EnvironmentPost, dict):
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
        if not isinstance(other, EnvironmentPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
