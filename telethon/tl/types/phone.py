"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types import TypePhoneCall, TypeUser



class PhoneCall(TLObject):
    CONSTRUCTOR_ID = 0xec82e140
    SUBCLASS_OF_ID = 0xd48afe4f

    def __init__(self, phone_call, users):
        """
        :param TypePhoneCall phone_call:
        :param List[TypeUser] users:

        Constructor for phone.PhoneCall: Instance of PhoneCall.
        """
        super().__init__()

        self.phone_call = phone_call  # type: TypePhoneCall
        self.users = users  # type: List[TypeUser]

    def to_dict(self):
        return {
            '_': 'PhoneCall',
            'phone_call': None if self.phone_call is None else self.phone_call.to_dict(),
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users]
        }

    def __bytes__(self):
        return b''.join((
            b'@\xe1\x82\xec',
            bytes(self.phone_call),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(bytes(x) for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_call = reader.tgread_object()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(phone_call=_phone_call, users=_users)

