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

from launchdarkly_api.models.clause import Clause  # noqa: F401,E501
from launchdarkly_api.models.rollout import Rollout  # noqa: F401,E501


class Rule(object):
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
        'id': 'str',
        'variation': 'int',
        'track_events': 'bool',
        'rollout': 'Rollout',
        'clauses': 'list[Clause]',
        'description': 'str'
    }

    attribute_map = {
        'id': '_id',
        'variation': 'variation',
        'track_events': 'trackEvents',
        'rollout': 'rollout',
        'clauses': 'clauses',
        'description': 'description'
    }

    def __init__(self, id=None, variation=None, track_events=None, rollout=None, clauses=None, description=None):  # noqa: E501
        """Rule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._variation = None
        self._track_events = None
        self._rollout = None
        self._clauses = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if variation is not None:
            self.variation = variation
        if track_events is not None:
            self.track_events = track_events
        if rollout is not None:
            self.rollout = rollout
        if clauses is not None:
            self.clauses = clauses
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Rule.  # noqa: E501


        :return: The id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rule.


        :param id: The id of this Rule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def variation(self):
        """Gets the variation of this Rule.  # noqa: E501


        :return: The variation of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this Rule.


        :param variation: The variation of this Rule.  # noqa: E501
        :type: int
        """

        self._variation = variation

    @property
    def track_events(self):
        """Gets the track_events of this Rule.  # noqa: E501


        :return: The track_events of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._track_events

    @track_events.setter
    def track_events(self, track_events):
        """Sets the track_events of this Rule.


        :param track_events: The track_events of this Rule.  # noqa: E501
        :type: bool
        """

        self._track_events = track_events

    @property
    def rollout(self):
        """Gets the rollout of this Rule.  # noqa: E501


        :return: The rollout of this Rule.  # noqa: E501
        :rtype: Rollout
        """
        return self._rollout

    @rollout.setter
    def rollout(self, rollout):
        """Sets the rollout of this Rule.


        :param rollout: The rollout of this Rule.  # noqa: E501
        :type: Rollout
        """

        self._rollout = rollout

    @property
    def clauses(self):
        """Gets the clauses of this Rule.  # noqa: E501


        :return: The clauses of this Rule.  # noqa: E501
        :rtype: list[Clause]
        """
        return self._clauses

    @clauses.setter
    def clauses(self, clauses):
        """Sets the clauses of this Rule.


        :param clauses: The clauses of this Rule.  # noqa: E501
        :type: list[Clause]
        """

        self._clauses = clauses

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501


        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.


        :param description: The description of this Rule.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(Rule, dict):
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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
