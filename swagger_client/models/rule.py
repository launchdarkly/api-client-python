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


class Rule(object):
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
        'variation': 'int',
        'rollout': 'Rollout',
        'clauses': 'list[Clause]'
    }

    attribute_map = {
        'variation': 'variation',
        'rollout': 'rollout',
        'clauses': 'clauses'
    }

    def __init__(self, variation=None, rollout=None, clauses=None):
        """
        Rule - a model defined in Swagger
        """

        self._variation = None
        self._rollout = None
        self._clauses = None

        if variation is not None:
          self.variation = variation
        if rollout is not None:
          self.rollout = rollout
        if clauses is not None:
          self.clauses = clauses

    @property
    def variation(self):
        """
        Gets the variation of this Rule.

        :return: The variation of this Rule.
        :rtype: int
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """
        Sets the variation of this Rule.

        :param variation: The variation of this Rule.
        :type: int
        """

        self._variation = variation

    @property
    def rollout(self):
        """
        Gets the rollout of this Rule.

        :return: The rollout of this Rule.
        :rtype: Rollout
        """
        return self._rollout

    @rollout.setter
    def rollout(self, rollout):
        """
        Sets the rollout of this Rule.

        :param rollout: The rollout of this Rule.
        :type: Rollout
        """

        self._rollout = rollout

    @property
    def clauses(self):
        """
        Gets the clauses of this Rule.

        :return: The clauses of this Rule.
        :rtype: list[Clause]
        """
        return self._clauses

    @clauses.setter
    def clauses(self, clauses):
        """
        Sets the clauses of this Rule.

        :param clauses: The clauses of this Rule.
        :type: list[Clause]
        """

        self._clauses = clauses

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
