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


class AuthenticatorAttestationResponse(object):
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
        'id': 'CredentialId',
        'raw_id': 'CredentialId',
        'type': 'str',
        'client_data_json': 'ClientDataJSON',
        'attestation_object': 'AttestationObject'
    }

    attribute_map = {
        'id': 'id',
        'raw_id': 'rawId',
        'type': 'type',
        'client_data_json': 'clientDataJSON',
        'attestation_object': 'attestationObject'
    }

    def __init__(self, id=None, raw_id=None, type=None, client_data_json=None, attestation_object=None):  # noqa: E501
        """AuthenticatorAttestationResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._raw_id = None
        self._type = None
        self._client_data_json = None
        self._attestation_object = None
        self.discriminator = None
        self.id = id
        if raw_id is not None:
            self.raw_id = raw_id
        self.type = type
        self.client_data_json = client_data_json
        self.attestation_object = attestation_object

    @property
    def id(self):
        """Gets the id of this AuthenticatorAttestationResponse.  # noqa: E501


        :return: The id of this AuthenticatorAttestationResponse.  # noqa: E501
        :rtype: CredentialId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthenticatorAttestationResponse.


        :param id: The id of this AuthenticatorAttestationResponse.  # noqa: E501
        :type: CredentialId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def raw_id(self):
        """Gets the raw_id of this AuthenticatorAttestationResponse.  # noqa: E501


        :return: The raw_id of this AuthenticatorAttestationResponse.  # noqa: E501
        :rtype: CredentialId
        """
        return self._raw_id

    @raw_id.setter
    def raw_id(self, raw_id):
        """Sets the raw_id of this AuthenticatorAttestationResponse.


        :param raw_id: The raw_id of this AuthenticatorAttestationResponse.  # noqa: E501
        :type: CredentialId
        """

        self._raw_id = raw_id

    @property
    def type(self):
        """Gets the type of this AuthenticatorAttestationResponse.  # noqa: E501


        :return: The type of this AuthenticatorAttestationResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthenticatorAttestationResponse.


        :param type: The type of this AuthenticatorAttestationResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def client_data_json(self):
        """Gets the client_data_json of this AuthenticatorAttestationResponse.  # noqa: E501


        :return: The client_data_json of this AuthenticatorAttestationResponse.  # noqa: E501
        :rtype: ClientDataJSON
        """
        return self._client_data_json

    @client_data_json.setter
    def client_data_json(self, client_data_json):
        """Sets the client_data_json of this AuthenticatorAttestationResponse.


        :param client_data_json: The client_data_json of this AuthenticatorAttestationResponse.  # noqa: E501
        :type: ClientDataJSON
        """
        if client_data_json is None:
            raise ValueError("Invalid value for `client_data_json`, must not be `None`")  # noqa: E501

        self._client_data_json = client_data_json

    @property
    def attestation_object(self):
        """Gets the attestation_object of this AuthenticatorAttestationResponse.  # noqa: E501


        :return: The attestation_object of this AuthenticatorAttestationResponse.  # noqa: E501
        :rtype: AttestationObject
        """
        return self._attestation_object

    @attestation_object.setter
    def attestation_object(self, attestation_object):
        """Sets the attestation_object of this AuthenticatorAttestationResponse.


        :param attestation_object: The attestation_object of this AuthenticatorAttestationResponse.  # noqa: E501
        :type: AttestationObject
        """
        if attestation_object is None:
            raise ValueError("Invalid value for `attestation_object`, must not be `None`")  # noqa: E501

        self._attestation_object = attestation_object

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
        if issubclass(AuthenticatorAttestationResponse, dict):
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
        if not isinstance(other, AuthenticatorAttestationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
