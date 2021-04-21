# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.1.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Destination(object):
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
        'id': 'str',
        'name': 'str',
        'kind': 'str',
        'config': 'object',
        'on': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'name': 'name',
        'kind': 'kind',
        'config': 'config',
        'on': 'on',
        'version': 'version'
    }

    def __init__(self, links=None, id=None, name=None, kind=None, config=None, on=None, version=None):  # noqa: E501
        """Destination - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._name = None
        self._kind = None
        self._config = None
        self._on = None
        self._version = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if config is not None:
            self.config = config
        if on is not None:
            self.on = on
        if version is not None:
            self.version = version

    @property
    def links(self):
        """Gets the links of this Destination.  # noqa: E501


        :return: The links of this Destination.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Destination.


        :param links: The links of this Destination.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Destination.  # noqa: E501

        Unique destination ID.  # noqa: E501

        :return: The id of this Destination.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Destination.

        Unique destination ID.  # noqa: E501

        :param id: The id of this Destination.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Destination.  # noqa: E501

        The destination name  # noqa: E501

        :return: The name of this Destination.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Destination.

        The destination name  # noqa: E501

        :param name: The name of this Destination.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def kind(self):
        """Gets the kind of this Destination.  # noqa: E501

        Destination type (\"google-pubsub\", \"kinesis\", \"mparticle\", or \"segment\")  # noqa: E501

        :return: The kind of this Destination.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Destination.

        Destination type (\"google-pubsub\", \"kinesis\", \"mparticle\", or \"segment\")  # noqa: E501

        :param kind: The kind of this Destination.  # noqa: E501
        :type: str
        """
        allowed_values = ["google-pubsub", "kinesis", "mparticle", "segment"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def config(self):
        """Gets the config of this Destination.  # noqa: E501

        destination-specific configuration.  # noqa: E501

        :return: The config of this Destination.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Destination.

        destination-specific configuration.  # noqa: E501

        :param config: The config of this Destination.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def on(self):
        """Gets the on of this Destination.  # noqa: E501

        Whether the data export destination is on or not.  # noqa: E501

        :return: The on of this Destination.  # noqa: E501
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """Sets the on of this Destination.

        Whether the data export destination is on or not.  # noqa: E501

        :param on: The on of this Destination.  # noqa: E501
        :type: bool
        """

        self._on = on

    @property
    def version(self):
        """Gets the version of this Destination.  # noqa: E501


        :return: The version of this Destination.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Destination.


        :param version: The version of this Destination.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(Destination, dict):
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
        if not isinstance(other, Destination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
