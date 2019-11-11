# coding: utf-8

"""
    Simple FIDO API

    This is the FIDO API  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: ruhma@metrarc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PublicKeyCredentialRequestOptions(object):
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
        'rp_id': 'str',
        'challenge': 'Challenge',
        'allow_credentials': 'AllowCredentials',
        'user_verification': 'UserVerification',
        'timeout': 'Timeout',
        'extensions': 'object'
    }

    attribute_map = {
        'rp_id': 'rpId',
        'challenge': 'challenge',
        'allow_credentials': 'allowCredentials',
        'user_verification': 'userVerification',
        'timeout': 'timeout',
        'extensions': 'extensions'
    }

    def __init__(self, rp_id=None, challenge=None, allow_credentials=None, user_verification=None, timeout=None, extensions=None):  # noqa: E501
        """PublicKeyCredentialRequestOptions - a model defined in Swagger"""  # noqa: E501
        self._rp_id = None
        self._challenge = None
        self._allow_credentials = None
        self._user_verification = None
        self._timeout = None
        self._extensions = None
        self.discriminator = None
        self.rp_id = rp_id
        if challenge is not None:
            self.challenge = challenge
        self.allow_credentials = allow_credentials
        if user_verification is not None:
            self.user_verification = user_verification
        if timeout is not None:
            self.timeout = timeout
        if extensions is not None:
            self.extensions = extensions

    @property
    def rp_id(self):
        """Gets the rp_id of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The rp_id of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._rp_id

    @rp_id.setter
    def rp_id(self, rp_id):
        """Sets the rp_id of this PublicKeyCredentialRequestOptions.


        :param rp_id: The rp_id of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: str
        """
        if rp_id is None:
            raise ValueError("Invalid value for `rp_id`, must not be `None`")  # noqa: E501

        self._rp_id = rp_id

    @property
    def challenge(self):
        """Gets the challenge of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The challenge of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: Challenge
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this PublicKeyCredentialRequestOptions.


        :param challenge: The challenge of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: Challenge
        """

        self._challenge = challenge

    @property
    def allow_credentials(self):
        """Gets the allow_credentials of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The allow_credentials of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: AllowCredentials
        """
        return self._allow_credentials

    @allow_credentials.setter
    def allow_credentials(self, allow_credentials):
        """Sets the allow_credentials of this PublicKeyCredentialRequestOptions.


        :param allow_credentials: The allow_credentials of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: AllowCredentials
        """
        if allow_credentials is None:
            raise ValueError("Invalid value for `allow_credentials`, must not be `None`")  # noqa: E501

        self._allow_credentials = allow_credentials

    @property
    def user_verification(self):
        """Gets the user_verification of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The user_verification of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: UserVerification
        """
        return self._user_verification

    @user_verification.setter
    def user_verification(self, user_verification):
        """Sets the user_verification of this PublicKeyCredentialRequestOptions.


        :param user_verification: The user_verification of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: UserVerification
        """

        self._user_verification = user_verification

    @property
    def timeout(self):
        """Gets the timeout of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The timeout of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: Timeout
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this PublicKeyCredentialRequestOptions.


        :param timeout: The timeout of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: Timeout
        """

        self._timeout = timeout

    @property
    def extensions(self):
        """Gets the extensions of this PublicKeyCredentialRequestOptions.  # noqa: E501


        :return: The extensions of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :rtype: object
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this PublicKeyCredentialRequestOptions.


        :param extensions: The extensions of this PublicKeyCredentialRequestOptions.  # noqa: E501
        :type: object
        """

        self._extensions = extensions

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
        if issubclass(PublicKeyCredentialRequestOptions, dict):
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
        if not isinstance(other, PublicKeyCredentialRequestOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
