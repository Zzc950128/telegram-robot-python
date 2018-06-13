"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types.storage import TypeFileType
    from ...tl.types import TypeFileHash



class CdnFile(TLObject):
    CONSTRUCTOR_ID = 0xa99fca4f
    SUBCLASS_OF_ID = 0xf5ccf928

    def __init__(self, bytes):
        """
        :param bytes bytes:

        Constructor for upload.CdnFile: Instance of either CdnFileReuploadNeeded, CdnFile.
        """
        super().__init__()

        self.bytes = bytes  # type: bytes

    def to_dict(self):
        return {
            '_': 'CdnFile',
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'O\xca\x9f\xa9',
            TLObject.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bytes = reader.tgread_bytes()
        return cls(bytes=_bytes)


class CdnFileReuploadNeeded(TLObject):
    CONSTRUCTOR_ID = 0xeea8e46e
    SUBCLASS_OF_ID = 0xf5ccf928

    def __init__(self, request_token):
        """
        :param bytes request_token:

        Constructor for upload.CdnFile: Instance of either CdnFileReuploadNeeded, CdnFile.
        """
        super().__init__()

        self.request_token = request_token  # type: bytes

    def to_dict(self):
        return {
            '_': 'CdnFileReuploadNeeded',
            'request_token': self.request_token
        }

    def __bytes__(self):
        return b''.join((
            b'n\xe4\xa8\xee',
            TLObject.serialize_bytes(self.request_token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _request_token = reader.tgread_bytes()
        return cls(request_token=_request_token)


class File(TLObject):
    CONSTRUCTOR_ID = 0x96a18d5
    SUBCLASS_OF_ID = 0x6c9bd728

    def __init__(self, type, mtime, bytes):
        """
        :param TypeFileType type:
        :param int mtime:
        :param bytes bytes:

        Constructor for upload.File: Instance of either File, FileCdnRedirect.
        """
        super().__init__()

        self.type = type  # type: TypeFileType
        self.mtime = mtime  # type: int
        self.bytes = bytes  # type: bytes

    def to_dict(self):
        return {
            '_': 'File',
            'type': None if self.type is None else self.type.to_dict(),
            'mtime': self.mtime,
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'\xd5\x18j\t',
            bytes(self.type),
            struct.pack('<i', self.mtime),
            TLObject.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _type = reader.tgread_object()
        _mtime = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(type=_type, mtime=_mtime, bytes=_bytes)


class FileCdnRedirect(TLObject):
    CONSTRUCTOR_ID = 0xf18cda44
    SUBCLASS_OF_ID = 0x6c9bd728

    def __init__(self, dc_id, file_token, encryption_key, encryption_iv, file_hashes):
        """
        :param int dc_id:
        :param bytes file_token:
        :param bytes encryption_key:
        :param bytes encryption_iv:
        :param List[TypeFileHash] file_hashes:

        Constructor for upload.File: Instance of either File, FileCdnRedirect.
        """
        super().__init__()

        self.dc_id = dc_id  # type: int
        self.file_token = file_token  # type: bytes
        self.encryption_key = encryption_key  # type: bytes
        self.encryption_iv = encryption_iv  # type: bytes
        self.file_hashes = file_hashes  # type: List[TypeFileHash]

    def to_dict(self):
        return {
            '_': 'FileCdnRedirect',
            'dc_id': self.dc_id,
            'file_token': self.file_token,
            'encryption_key': self.encryption_key,
            'encryption_iv': self.encryption_iv,
            'file_hashes': [] if self.file_hashes is None else [None if x is None else x.to_dict() for x in self.file_hashes]
        }

    def __bytes__(self):
        return b''.join((
            b'D\xda\x8c\xf1',
            struct.pack('<i', self.dc_id),
            TLObject.serialize_bytes(self.file_token),
            TLObject.serialize_bytes(self.encryption_key),
            TLObject.serialize_bytes(self.encryption_iv),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.file_hashes)),b''.join(bytes(x) for x in self.file_hashes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _dc_id = reader.read_int()
        _file_token = reader.tgread_bytes()
        _encryption_key = reader.tgread_bytes()
        _encryption_iv = reader.tgread_bytes()
        reader.read_int()
        _file_hashes = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _file_hashes.append(_x)

        return cls(dc_id=_dc_id, file_token=_file_token, encryption_key=_encryption_key, encryption_iv=_encryption_iv, file_hashes=_file_hashes)


class WebFile(TLObject):
    CONSTRUCTOR_ID = 0x21e753bc
    SUBCLASS_OF_ID = 0x68f17f51

    def __init__(self, size, mime_type, file_type, mtime, bytes):
        """
        :param int size:
        :param str mime_type:
        :param TypeFileType file_type:
        :param int mtime:
        :param bytes bytes:

        Constructor for upload.WebFile: Instance of WebFile.
        """
        super().__init__()

        self.size = size  # type: int
        self.mime_type = mime_type  # type: str
        self.file_type = file_type  # type: TypeFileType
        self.mtime = mtime  # type: int
        self.bytes = bytes  # type: bytes

    def to_dict(self):
        return {
            '_': 'WebFile',
            'size': self.size,
            'mime_type': self.mime_type,
            'file_type': None if self.file_type is None else self.file_type.to_dict(),
            'mtime': self.mtime,
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'\xbcS\xe7!',
            struct.pack('<i', self.size),
            TLObject.serialize_bytes(self.mime_type),
            bytes(self.file_type),
            struct.pack('<i', self.mtime),
            TLObject.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _size = reader.read_int()
        _mime_type = reader.tgread_string()
        _file_type = reader.tgread_object()
        _mtime = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(size=_size, mime_type=_mime_type, file_type=_file_type, mtime=_mtime, bytes=_bytes)

