# coding: utf-8

"""
    Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ChargeInstrument(object):
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
        'description': 'str',
        'tail': 'str',
        'amount': 'Currency'
    }

    attribute_map = {
        'description': 'Description',
        'tail': 'Tail',
        'amount': 'Amount'
    }

    def __init__(self, description=None, tail=None, amount=None):  # noqa: E501
        """ChargeInstrument - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._tail = None
        self._amount = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if tail is not None:
            self.tail = tail
        if amount is not None:
            self.amount = amount

    @property
    def description(self):
        """Gets the description of this ChargeInstrument.  # noqa: E501

        A short description of the charge instrument.  # noqa: E501

        :return: The description of this ChargeInstrument.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChargeInstrument.

        A short description of the charge instrument.  # noqa: E501

        :param description: The description of this ChargeInstrument.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tail(self):
        """Gets the tail of this ChargeInstrument.  # noqa: E501

        The account tail (trailing digits) of the charge instrument.  # noqa: E501

        :return: The tail of this ChargeInstrument.  # noqa: E501
        :rtype: str
        """
        return self._tail

    @tail.setter
    def tail(self, tail):
        """Sets the tail of this ChargeInstrument.

        The account tail (trailing digits) of the charge instrument.  # noqa: E501

        :param tail: The tail of this ChargeInstrument.  # noqa: E501
        :type: str
        """

        self._tail = tail

    @property
    def amount(self):
        """Gets the amount of this ChargeInstrument.  # noqa: E501


        :return: The amount of this ChargeInstrument.  # noqa: E501
        :rtype: Currency
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ChargeInstrument.


        :param amount: The amount of this ChargeInstrument.  # noqa: E501
        :type: Currency
        """

        self._amount = amount

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
        if issubclass(ChargeInstrument, dict):
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
        if not isinstance(other, ChargeInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other