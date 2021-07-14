# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.3.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Clause(object):
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
        'attribute': 'str',
        'op': 'str',
        'values': 'list[object]',
        'negate': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'attribute': 'attribute',
        'op': 'op',
        'values': 'values',
        'negate': 'negate'
    }

    def __init__(self, id=None, attribute=None, op=None, values=None, negate=None):  # noqa: E501
        """Clause - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._attribute = None
        self._op = None
        self._values = None
        self._negate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if attribute is not None:
            self.attribute = attribute
        if op is not None:
            self.op = op
        if values is not None:
            self.values = values
        if negate is not None:
            self.negate = negate

    @property
    def id(self):
        """Gets the id of this Clause.  # noqa: E501


        :return: The id of this Clause.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Clause.


        :param id: The id of this Clause.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attribute(self):
        """Gets the attribute of this Clause.  # noqa: E501


        :return: The attribute of this Clause.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Clause.


        :param attribute: The attribute of this Clause.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def op(self):
        """Gets the op of this Clause.  # noqa: E501


        :return: The op of this Clause.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this Clause.


        :param op: The op of this Clause.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def values(self):
        """Gets the values of this Clause.  # noqa: E501


        :return: The values of this Clause.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Clause.


        :param values: The values of this Clause.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def negate(self):
        """Gets the negate of this Clause.  # noqa: E501


        :return: The negate of this Clause.  # noqa: E501
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        """Sets the negate of this Clause.


        :param negate: The negate of this Clause.  # noqa: E501
        :type: bool
        """

        self._negate = negate

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
        if issubclass(Clause, dict):
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
        if not isinstance(other, Clause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
