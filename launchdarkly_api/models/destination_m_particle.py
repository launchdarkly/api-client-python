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


class DestinationMParticle(object):
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
        'api_key': 'str',
        'secret': 'str',
        'user_identity': 'str',
        'environment': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'secret': 'secret',
        'user_identity': 'userIdentity',
        'environment': 'environment'
    }

    def __init__(self, api_key=None, secret=None, user_identity=None, environment=None):  # noqa: E501
        """DestinationMParticle - a model defined in Swagger"""  # noqa: E501

        self._api_key = None
        self._secret = None
        self._user_identity = None
        self._environment = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if secret is not None:
            self.secret = secret
        if user_identity is not None:
            self.user_identity = user_identity
        if environment is not None:
            self.environment = environment

    @property
    def api_key(self):
        """Gets the api_key of this DestinationMParticle.  # noqa: E501


        :return: The api_key of this DestinationMParticle.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this DestinationMParticle.


        :param api_key: The api_key of this DestinationMParticle.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def secret(self):
        """Gets the secret of this DestinationMParticle.  # noqa: E501


        :return: The secret of this DestinationMParticle.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DestinationMParticle.


        :param secret: The secret of this DestinationMParticle.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def user_identity(self):
        """Gets the user_identity of this DestinationMParticle.  # noqa: E501


        :return: The user_identity of this DestinationMParticle.  # noqa: E501
        :rtype: str
        """
        return self._user_identity

    @user_identity.setter
    def user_identity(self, user_identity):
        """Sets the user_identity of this DestinationMParticle.


        :param user_identity: The user_identity of this DestinationMParticle.  # noqa: E501
        :type: str
        """

        self._user_identity = user_identity

    @property
    def environment(self):
        """Gets the environment of this DestinationMParticle.  # noqa: E501


        :return: The environment of this DestinationMParticle.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this DestinationMParticle.


        :param environment: The environment of this DestinationMParticle.  # noqa: E501
        :type: str
        """

        self._environment = environment

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
        if issubclass(DestinationMParticle, dict):
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
        if not isinstance(other, DestinationMParticle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
