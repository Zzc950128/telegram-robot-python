"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types import TypePrivacyRule, TypeWebAuthorization, TypeBool, TypeUser, TypeAuthorization



class Authorizations(TLObject):
    CONSTRUCTOR_ID = 0x1250abde
    SUBCLASS_OF_ID = 0xbf5e0ff

    def __init__(self, authorizations):
        """
        :param List[TypeAuthorization] authorizations:

        Constructor for account.Authorizations: Instance of Authorizations.
        """
        super().__init__()

        self.authorizations = authorizations  # type: List[TypeAuthorization]

    def to_dict(self):
        return {
            '_': 'Authorizations',
            'authorizations': [] if self.authorizations is None else [None if x is None else x.to_dict() for x in self.authorizations]
        }

    def __bytes__(self):
        return b''.join((
            b'\xde\xabP\x12',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.authorizations)),b''.join(bytes(x) for x in self.authorizations),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _authorizations = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _authorizations.append(_x)

        return cls(authorizations=_authorizations)


class NoPassword(TLObject):
    CONSTRUCTOR_ID = 0x96dabc18
    SUBCLASS_OF_ID = 0x53a211a3

    def __init__(self, new_salt, email_unconfirmed_pattern):
        """
        :param bytes new_salt:
        :param str email_unconfirmed_pattern:

        Constructor for account.Password: Instance of either NoPassword, Password.
        """
        super().__init__()

        self.new_salt = new_salt  # type: bytes
        self.email_unconfirmed_pattern = email_unconfirmed_pattern  # type: str

    def to_dict(self):
        return {
            '_': 'NoPassword',
            'new_salt': self.new_salt,
            'email_unconfirmed_pattern': self.email_unconfirmed_pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\x18\xbc\xda\x96',
            TLObject.serialize_bytes(self.new_salt),
            TLObject.serialize_bytes(self.email_unconfirmed_pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _new_salt = reader.tgread_bytes()
        _email_unconfirmed_pattern = reader.tgread_string()
        return cls(new_salt=_new_salt, email_unconfirmed_pattern=_email_unconfirmed_pattern)


class Password(TLObject):
    CONSTRUCTOR_ID = 0x7c18141c
    SUBCLASS_OF_ID = 0x53a211a3

    def __init__(self, current_salt, new_salt, hint, has_recovery, email_unconfirmed_pattern):
        """
        :param bytes current_salt:
        :param bytes new_salt:
        :param str hint:
        :param TypeBool has_recovery:
        :param str email_unconfirmed_pattern:

        Constructor for account.Password: Instance of either NoPassword, Password.
        """
        super().__init__()

        self.current_salt = current_salt  # type: bytes
        self.new_salt = new_salt  # type: bytes
        self.hint = hint  # type: str
        self.has_recovery = has_recovery  # type: TypeBool
        self.email_unconfirmed_pattern = email_unconfirmed_pattern  # type: str

    def to_dict(self):
        return {
            '_': 'Password',
            'current_salt': self.current_salt,
            'new_salt': self.new_salt,
            'hint': self.hint,
            'has_recovery': self.has_recovery,
            'email_unconfirmed_pattern': self.email_unconfirmed_pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\x1c\x14\x18|',
            TLObject.serialize_bytes(self.current_salt),
            TLObject.serialize_bytes(self.new_salt),
            TLObject.serialize_bytes(self.hint),
            b'\xb5ur\x99' if self.has_recovery else b'7\x97y\xbc',
            TLObject.serialize_bytes(self.email_unconfirmed_pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _current_salt = reader.tgread_bytes()
        _new_salt = reader.tgread_bytes()
        _hint = reader.tgread_string()
        _has_recovery = reader.tgread_bool()
        _email_unconfirmed_pattern = reader.tgread_string()
        return cls(current_salt=_current_salt, new_salt=_new_salt, hint=_hint, has_recovery=_has_recovery, email_unconfirmed_pattern=_email_unconfirmed_pattern)


class PasswordInputSettings(TLObject):
    CONSTRUCTOR_ID = 0x86916deb
    SUBCLASS_OF_ID = 0xc426ca6

    def __init__(self, new_salt=None, new_password_hash=None, hint=None, email=None):
        """
        :param Optional[bytes] new_salt:
        :param Optional[bytes] new_password_hash:
        :param Optional[str] hint:
        :param Optional[str] email:

        Constructor for account.PasswordInputSettings: Instance of PasswordInputSettings.
        """
        super().__init__()

        self.new_salt = new_salt  # type: Optional[bytes]
        self.new_password_hash = new_password_hash  # type: Optional[bytes]
        self.hint = hint  # type: Optional[str]
        self.email = email  # type: Optional[str]

    def to_dict(self):
        return {
            '_': 'PasswordInputSettings',
            'new_salt': self.new_salt,
            'new_password_hash': self.new_password_hash,
            'hint': self.hint,
            'email': self.email
        }

    def __bytes__(self):
        assert ((self.new_salt or self.new_salt is not None) and (self.new_password_hash or self.new_password_hash is not None) and (self.hint or self.hint is not None)) or ((self.new_salt is None or self.new_salt is False) and (self.new_password_hash is None or self.new_password_hash is False) and (self.hint is None or self.hint is False)), 'new_salt, new_password_hash, hint parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\xebm\x91\x86',
            struct.pack('<I', (0 if self.new_salt is None or self.new_salt is False else 1) | (0 if self.new_password_hash is None or self.new_password_hash is False else 1) | (0 if self.hint is None or self.hint is False else 1) | (0 if self.email is None or self.email is False else 2)),
            b'' if self.new_salt is None or self.new_salt is False else (TLObject.serialize_bytes(self.new_salt)),
            b'' if self.new_password_hash is None or self.new_password_hash is False else (TLObject.serialize_bytes(self.new_password_hash)),
            b'' if self.hint is None or self.hint is False else (TLObject.serialize_bytes(self.hint)),
            b'' if self.email is None or self.email is False else (TLObject.serialize_bytes(self.email)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _new_salt = reader.tgread_bytes()
        else:
            _new_salt = None
        if flags & 1:
            _new_password_hash = reader.tgread_bytes()
        else:
            _new_password_hash = None
        if flags & 1:
            _hint = reader.tgread_string()
        else:
            _hint = None
        if flags & 2:
            _email = reader.tgread_string()
        else:
            _email = None
        return cls(new_salt=_new_salt, new_password_hash=_new_password_hash, hint=_hint, email=_email)


class PasswordSettings(TLObject):
    CONSTRUCTOR_ID = 0xb7b72ab3
    SUBCLASS_OF_ID = 0xd23fb078

    def __init__(self, email):
        """
        :param str email:

        Constructor for account.PasswordSettings: Instance of PasswordSettings.
        """
        super().__init__()

        self.email = email  # type: str

    def to_dict(self):
        return {
            '_': 'PasswordSettings',
            'email': self.email
        }

    def __bytes__(self):
        return b''.join((
            b'\xb3*\xb7\xb7',
            TLObject.serialize_bytes(self.email),
        ))

    @classmethod
    def from_reader(cls, reader):
        _email = reader.tgread_string()
        return cls(email=_email)


class PrivacyRules(TLObject):
    CONSTRUCTOR_ID = 0x554abb6f
    SUBCLASS_OF_ID = 0xb55aba82

    def __init__(self, rules, users):
        """
        :param List[TypePrivacyRule] rules:
        :param List[TypeUser] users:

        Constructor for account.PrivacyRules: Instance of PrivacyRules.
        """
        super().__init__()

        self.rules = rules  # type: List[TypePrivacyRule]
        self.users = users  # type: List[TypeUser]

    def to_dict(self):
        return {
            '_': 'PrivacyRules',
            'rules': [] if self.rules is None else [None if x is None else x.to_dict() for x in self.rules],
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users]
        }

    def __bytes__(self):
        return b''.join((
            b'o\xbbJU',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.rules)),b''.join(bytes(x) for x in self.rules),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(bytes(x) for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _rules = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _rules.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(rules=_rules, users=_users)


class TmpPassword(TLObject):
    CONSTRUCTOR_ID = 0xdb64fd34
    SUBCLASS_OF_ID = 0xb064992d

    def __init__(self, tmp_password, valid_until):
        """
        :param bytes tmp_password:
        :param int valid_until:

        Constructor for account.TmpPassword: Instance of TmpPassword.
        """
        super().__init__()

        self.tmp_password = tmp_password  # type: bytes
        self.valid_until = valid_until  # type: int

    def to_dict(self):
        return {
            '_': 'TmpPassword',
            'tmp_password': self.tmp_password,
            'valid_until': self.valid_until
        }

    def __bytes__(self):
        return b''.join((
            b'4\xfdd\xdb',
            TLObject.serialize_bytes(self.tmp_password),
            struct.pack('<i', self.valid_until),
        ))

    @classmethod
    def from_reader(cls, reader):
        _tmp_password = reader.tgread_bytes()
        _valid_until = reader.read_int()
        return cls(tmp_password=_tmp_password, valid_until=_valid_until)


class WebAuthorizations(TLObject):
    CONSTRUCTOR_ID = 0xed56c9fc
    SUBCLASS_OF_ID = 0x9a365b32

    def __init__(self, authorizations, users):
        """
        :param List[TypeWebAuthorization] authorizations:
        :param List[TypeUser] users:

        Constructor for account.WebAuthorizations: Instance of WebAuthorizations.
        """
        super().__init__()

        self.authorizations = authorizations  # type: List[TypeWebAuthorization]
        self.users = users  # type: List[TypeUser]

    def to_dict(self):
        return {
            '_': 'WebAuthorizations',
            'authorizations': [] if self.authorizations is None else [None if x is None else x.to_dict() for x in self.authorizations],
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users]
        }

    def __bytes__(self):
        return b''.join((
            b'\xfc\xc9V\xed',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.authorizations)),b''.join(bytes(x) for x in self.authorizations),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(bytes(x) for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _authorizations = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _authorizations.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(authorizations=_authorizations, users=_users)

