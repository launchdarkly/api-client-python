# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.32
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.audit_log_entry_target import AuditLogEntryTarget  # noqa: F401,E501
from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.member import Member  # noqa: F401,E501


class AuditLogEntry(object):
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
        '_date': 'int',
        'kind': 'str',
        'name': 'str',
        'description': 'str',
        'short_description': 'str',
        'comment': 'str',
        'member': 'Member',
        'title_verb': 'str',
        'title': 'str',
        'target': 'AuditLogEntryTarget'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        '_date': 'date',
        'kind': 'kind',
        'name': 'name',
        'description': 'description',
        'short_description': 'shortDescription',
        'comment': 'comment',
        'member': 'member',
        'title_verb': 'titleVerb',
        'title': 'title',
        'target': 'target'
    }

    def __init__(self, links=None, id=None, _date=None, kind=None, name=None, description=None, short_description=None, comment=None, member=None, title_verb=None, title=None, target=None):  # noqa: E501
        """AuditLogEntry - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self.__date = None
        self._kind = None
        self._name = None
        self._description = None
        self._short_description = None
        self._comment = None
        self._member = None
        self._title_verb = None
        self._title = None
        self._target = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if _date is not None:
            self._date = _date
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if short_description is not None:
            self.short_description = short_description
        if comment is not None:
            self.comment = comment
        if member is not None:
            self.member = member
        if title_verb is not None:
            self.title_verb = title_verb
        if title is not None:
            self.title = title
        if target is not None:
            self.target = target

    @property
    def links(self):
        """Gets the links of this AuditLogEntry.  # noqa: E501


        :return: The links of this AuditLogEntry.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AuditLogEntry.


        :param links: The links of this AuditLogEntry.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this AuditLogEntry.  # noqa: E501


        :return: The id of this AuditLogEntry.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLogEntry.


        :param id: The id of this AuditLogEntry.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this AuditLogEntry.  # noqa: E501


        :return: The _date of this AuditLogEntry.  # noqa: E501
        :rtype: int
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AuditLogEntry.


        :param _date: The _date of this AuditLogEntry.  # noqa: E501
        :type: int
        """

        self.__date = _date

    @property
    def kind(self):
        """Gets the kind of this AuditLogEntry.  # noqa: E501


        :return: The kind of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AuditLogEntry.


        :param kind: The kind of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this AuditLogEntry.  # noqa: E501


        :return: The name of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditLogEntry.


        :param name: The name of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AuditLogEntry.  # noqa: E501


        :return: The description of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuditLogEntry.


        :param description: The description of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_description(self):
        """Gets the short_description of this AuditLogEntry.  # noqa: E501


        :return: The short_description of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this AuditLogEntry.


        :param short_description: The short_description of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def comment(self):
        """Gets the comment of this AuditLogEntry.  # noqa: E501


        :return: The comment of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuditLogEntry.


        :param comment: The comment of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def member(self):
        """Gets the member of this AuditLogEntry.  # noqa: E501


        :return: The member of this AuditLogEntry.  # noqa: E501
        :rtype: Member
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this AuditLogEntry.


        :param member: The member of this AuditLogEntry.  # noqa: E501
        :type: Member
        """

        self._member = member

    @property
    def title_verb(self):
        """Gets the title_verb of this AuditLogEntry.  # noqa: E501


        :return: The title_verb of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._title_verb

    @title_verb.setter
    def title_verb(self, title_verb):
        """Sets the title_verb of this AuditLogEntry.


        :param title_verb: The title_verb of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._title_verb = title_verb

    @property
    def title(self):
        """Gets the title of this AuditLogEntry.  # noqa: E501


        :return: The title of this AuditLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AuditLogEntry.


        :param title: The title of this AuditLogEntry.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def target(self):
        """Gets the target of this AuditLogEntry.  # noqa: E501


        :return: The target of this AuditLogEntry.  # noqa: E501
        :rtype: AuditLogEntryTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AuditLogEntry.


        :param target: The target of this AuditLogEntry.  # noqa: E501
        :type: AuditLogEntryTarget
        """

        self._target = target

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
        if issubclass(AuditLogEntry, dict):
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
        if not isinstance(other, AuditLogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
