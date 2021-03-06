# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/services/whitelist/whitelist.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/services/whitelist/whitelist.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&app/services/whitelist/whitelist.proto\"\x10\n\x0eWhitelistEmpty\" \n\x12WhitelistIdRequest\x12\n\n\x02id\x18\x01 \x02(\t\":\n\x15WhitelistNotIdRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\x10\n\x08\x63urrency\x18\x02 \x02(\t\"A\n\x10WhitelistRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\x12\x10\n\x08\x63urrency\x18\x03 \x02(\t\"9\n\x11WhitelistResponse\x12$\n\twhitelist\x18\x01 \x02(\x0b\x32\x11.WhitelistRequest\"A\n\x19WhitelistMultipleResponse\x12$\n\twhitelist\x18\x01 \x03(\x0b\x32\x11.WhitelistRequest2\xdb\x01\n\tWhitelist\x12\x36\n\x07get_all\x12\x0f.WhitelistEmpty\x1a\x1a.WhitelistMultipleResponse\x12\x32\n\x04save\x12\x16.WhitelistNotIdRequest\x1a\x12.WhitelistResponse\x12/\n\x06update\x12\x11.WhitelistRequest\x1a\x12.WhitelistResponse\x12\x31\n\x06\x64\x65lete\x12\x13.WhitelistIdRequest\x1a\x12.WhitelistResponse'
)




_WHITELISTEMPTY = _descriptor.Descriptor(
  name='WhitelistEmpty',
  full_name='WhitelistEmpty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=58,
)


_WHITELISTIDREQUEST = _descriptor.Descriptor(
  name='WhitelistIdRequest',
  full_name='WhitelistIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WhitelistIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=92,
)


_WHITELISTNOTIDREQUEST = _descriptor.Descriptor(
  name='WhitelistNotIdRequest',
  full_name='WhitelistNotIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='WhitelistNotIdRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='WhitelistNotIdRequest.currency', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=152,
)


_WHITELISTREQUEST = _descriptor.Descriptor(
  name='WhitelistRequest',
  full_name='WhitelistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WhitelistRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='WhitelistRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='WhitelistRequest.currency', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=219,
)


_WHITELISTRESPONSE = _descriptor.Descriptor(
  name='WhitelistResponse',
  full_name='WhitelistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='whitelist', full_name='WhitelistResponse.whitelist', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=278,
)


_WHITELISTMULTIPLERESPONSE = _descriptor.Descriptor(
  name='WhitelistMultipleResponse',
  full_name='WhitelistMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='whitelist', full_name='WhitelistMultipleResponse.whitelist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=345,
)

_WHITELISTRESPONSE.fields_by_name['whitelist'].message_type = _WHITELISTREQUEST
_WHITELISTMULTIPLERESPONSE.fields_by_name['whitelist'].message_type = _WHITELISTREQUEST
DESCRIPTOR.message_types_by_name['WhitelistEmpty'] = _WHITELISTEMPTY
DESCRIPTOR.message_types_by_name['WhitelistIdRequest'] = _WHITELISTIDREQUEST
DESCRIPTOR.message_types_by_name['WhitelistNotIdRequest'] = _WHITELISTNOTIDREQUEST
DESCRIPTOR.message_types_by_name['WhitelistRequest'] = _WHITELISTREQUEST
DESCRIPTOR.message_types_by_name['WhitelistResponse'] = _WHITELISTRESPONSE
DESCRIPTOR.message_types_by_name['WhitelistMultipleResponse'] = _WHITELISTMULTIPLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WhitelistEmpty = _reflection.GeneratedProtocolMessageType('WhitelistEmpty', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTEMPTY,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistEmpty)
  })
_sym_db.RegisterMessage(WhitelistEmpty)

WhitelistIdRequest = _reflection.GeneratedProtocolMessageType('WhitelistIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTIDREQUEST,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistIdRequest)
  })
_sym_db.RegisterMessage(WhitelistIdRequest)

WhitelistNotIdRequest = _reflection.GeneratedProtocolMessageType('WhitelistNotIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTNOTIDREQUEST,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistNotIdRequest)
  })
_sym_db.RegisterMessage(WhitelistNotIdRequest)

WhitelistRequest = _reflection.GeneratedProtocolMessageType('WhitelistRequest', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTREQUEST,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistRequest)
  })
_sym_db.RegisterMessage(WhitelistRequest)

WhitelistResponse = _reflection.GeneratedProtocolMessageType('WhitelistResponse', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTRESPONSE,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistResponse)
  })
_sym_db.RegisterMessage(WhitelistResponse)

WhitelistMultipleResponse = _reflection.GeneratedProtocolMessageType('WhitelistMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTMULTIPLERESPONSE,
  '__module__' : 'app.services.whitelist.whitelist_pb2'
  # @@protoc_insertion_point(class_scope:WhitelistMultipleResponse)
  })
_sym_db.RegisterMessage(WhitelistMultipleResponse)



_WHITELIST = _descriptor.ServiceDescriptor(
  name='Whitelist',
  full_name='Whitelist',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=348,
  serialized_end=567,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='Whitelist.get_all',
    index=0,
    containing_service=None,
    input_type=_WHITELISTEMPTY,
    output_type=_WHITELISTMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='save',
    full_name='Whitelist.save',
    index=1,
    containing_service=None,
    input_type=_WHITELISTNOTIDREQUEST,
    output_type=_WHITELISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='Whitelist.update',
    index=2,
    containing_service=None,
    input_type=_WHITELISTREQUEST,
    output_type=_WHITELISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='Whitelist.delete',
    index=3,
    containing_service=None,
    input_type=_WHITELISTIDREQUEST,
    output_type=_WHITELISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WHITELIST)

DESCRIPTOR.services_by_name['Whitelist'] = _WHITELIST

# @@protoc_insertion_point(module_scope)
