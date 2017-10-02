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


class FeatureFlag(object):
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
        'key': 'str',
        'name': 'str',
        'kind': 'str',
        'creation_date': 'float',
        'include_in_snippet': 'bool',
        'temporary': 'bool',
        'maintainer_id': 'str',
        'tags': 'list[str]',
        'variations': 'list[Variation]',
        'links': 'Links',
        'maintainer': 'Member',
        'environments': 'dict(str, FeatureFlagConfig)'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'kind': 'kind',
        'creation_date': 'creationDate',
        'include_in_snippet': 'includeInSnippet',
        'temporary': 'temporary',
        'maintainer_id': 'maintainerId',
        'tags': 'tags',
        'variations': 'variations',
        'links': '_links',
        'maintainer': '_maintainer',
        'environments': 'environments'
    }

    def __init__(self, key=None, name=None, kind=None, creation_date=None, include_in_snippet=None, temporary=None, maintainer_id=None, tags=None, variations=None, links=None, maintainer=None, environments=None):
        """
        FeatureFlag - a model defined in Swagger
        """

        self._key = None
        self._name = None
        self._kind = None
        self._creation_date = None
        self._include_in_snippet = None
        self._temporary = None
        self._maintainer_id = None
        self._tags = None
        self._variations = None
        self._links = None
        self._maintainer = None
        self._environments = None

        if key is not None:
          self.key = key
        if name is not None:
          self.name = name
        if kind is not None:
          self.kind = kind
        if creation_date is not None:
          self.creation_date = creation_date
        if include_in_snippet is not None:
          self.include_in_snippet = include_in_snippet
        if temporary is not None:
          self.temporary = temporary
        if maintainer_id is not None:
          self.maintainer_id = maintainer_id
        if tags is not None:
          self.tags = tags
        if variations is not None:
          self.variations = variations
        if links is not None:
          self.links = links
        if maintainer is not None:
          self.maintainer = maintainer
        if environments is not None:
          self.environments = environments

    @property
    def key(self):
        """
        Gets the key of this FeatureFlag.

        :return: The key of this FeatureFlag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FeatureFlag.

        :param key: The key of this FeatureFlag.
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this FeatureFlag.

        :return: The name of this FeatureFlag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FeatureFlag.

        :param name: The name of this FeatureFlag.
        :type: str
        """

        self._name = name

    @property
    def kind(self):
        """
        Gets the kind of this FeatureFlag.

        :return: The kind of this FeatureFlag.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this FeatureFlag.

        :param kind: The kind of this FeatureFlag.
        :type: str
        """

        self._kind = kind

    @property
    def creation_date(self):
        """
        Gets the creation_date of this FeatureFlag.

        :return: The creation_date of this FeatureFlag.
        :rtype: float
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this FeatureFlag.

        :param creation_date: The creation_date of this FeatureFlag.
        :type: float
        """

        self._creation_date = creation_date

    @property
    def include_in_snippet(self):
        """
        Gets the include_in_snippet of this FeatureFlag.

        :return: The include_in_snippet of this FeatureFlag.
        :rtype: bool
        """
        return self._include_in_snippet

    @include_in_snippet.setter
    def include_in_snippet(self, include_in_snippet):
        """
        Sets the include_in_snippet of this FeatureFlag.

        :param include_in_snippet: The include_in_snippet of this FeatureFlag.
        :type: bool
        """

        self._include_in_snippet = include_in_snippet

    @property
    def temporary(self):
        """
        Gets the temporary of this FeatureFlag.

        :return: The temporary of this FeatureFlag.
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """
        Sets the temporary of this FeatureFlag.

        :param temporary: The temporary of this FeatureFlag.
        :type: bool
        """

        self._temporary = temporary

    @property
    def maintainer_id(self):
        """
        Gets the maintainer_id of this FeatureFlag.

        :return: The maintainer_id of this FeatureFlag.
        :rtype: str
        """
        return self._maintainer_id

    @maintainer_id.setter
    def maintainer_id(self, maintainer_id):
        """
        Sets the maintainer_id of this FeatureFlag.

        :param maintainer_id: The maintainer_id of this FeatureFlag.
        :type: str
        """

        self._maintainer_id = maintainer_id

    @property
    def tags(self):
        """
        Gets the tags of this FeatureFlag.

        :return: The tags of this FeatureFlag.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FeatureFlag.

        :param tags: The tags of this FeatureFlag.
        :type: list[str]
        """

        self._tags = tags

    @property
    def variations(self):
        """
        Gets the variations of this FeatureFlag.

        :return: The variations of this FeatureFlag.
        :rtype: list[Variation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """
        Sets the variations of this FeatureFlag.

        :param variations: The variations of this FeatureFlag.
        :type: list[Variation]
        """

        self._variations = variations

    @property
    def links(self):
        """
        Gets the links of this FeatureFlag.

        :return: The links of this FeatureFlag.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this FeatureFlag.

        :param links: The links of this FeatureFlag.
        :type: Links
        """

        self._links = links

    @property
    def maintainer(self):
        """
        Gets the maintainer of this FeatureFlag.

        :return: The maintainer of this FeatureFlag.
        :rtype: Member
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """
        Sets the maintainer of this FeatureFlag.

        :param maintainer: The maintainer of this FeatureFlag.
        :type: Member
        """

        self._maintainer = maintainer

    @property
    def environments(self):
        """
        Gets the environments of this FeatureFlag.

        :return: The environments of this FeatureFlag.
        :rtype: dict(str, FeatureFlagConfig)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """
        Sets the environments of this FeatureFlag.

        :param environments: The environments of this FeatureFlag.
        :type: dict(str, FeatureFlagConfig)
        """

        self._environments = environments

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
        if not isinstance(other, FeatureFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
