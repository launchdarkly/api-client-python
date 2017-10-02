# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API

    OpenAPI spec version: 2.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Projects(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'key': 'str',
        'name': 'str',
        'items': 'list[Project]'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'key': 'key',
        'name': 'name',
        'items': 'items'
    }

    def __init__(self, links=None, id=None, key=None, name=None, items=None):
        """
        Projects - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._key = None
        self._name = None
        self._items = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if key is not None:
          self.key = key
        if name is not None:
          self.name = name
        if items is not None:
          self.items = items

    @property
    def links(self):
        """
        Gets the links of this Projects.

        :return: The links of this Projects.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Projects.

        :param links: The links of this Projects.
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Projects.

        :return: The id of this Projects.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Projects.

        :param id: The id of this Projects.
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """
        Gets the key of this Projects.

        :return: The key of this Projects.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Projects.

        :param key: The key of this Projects.
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this Projects.

        :return: The name of this Projects.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Projects.

        :param name: The name of this Projects.
        :type: str
        """

        self._name = name

    @property
    def items(self):
        """
        Gets the items of this Projects.

        :return: The items of this Projects.
        :rtype: list[Project]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this Projects.

        :param items: The items of this Projects.
        :type: list[Project]
        """

        self._items = items

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Projects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
