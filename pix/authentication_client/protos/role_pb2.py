# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/services/role/role.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/services/role/role.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61pp/services/role/role.proto\"\x0b\n\tRoleEmpty\"\x1b\n\rRoleIdRequest\x12\n\n\x02id\x18\x01 \x02(\t\">\n\x10RoleNotIdRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x63ode\x18\x02 \x02(\t\x12\x0e\n\x06scopes\x18\x03 \x03(\t\"E\n\x0bRoleRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x63ode\x18\x03 \x02(\t\x12\x0e\n\x06scopes\x18\x04 \x03(\t\"F\n\x10RoleTableRequest\x12\x0c\n\x04page\x18\x01 \x02(\x05\x12\x14\n\x08per_page\x18\x02 \x01(\x05:\x02\x31\x35\x12\x0e\n\x06search\x18\x03 \x01(\t\"*\n\x0cRoleResponse\x12\x1a\n\x04role\x18\x01 \x02(\x0b\x32\x0c.RoleRequest\"2\n\x14RoleMultipleResponse\x12\x1a\n\x04role\x18\x01 \x03(\x0b\x32\x0c.RoleRequest\"x\n\x11RoleTableResponse\x12\x1b\n\x05items\x18\x01 \x03(\x0b\x32\x0c.RoleRequest\x12\x0c\n\x04page\x18\x02 \x02(\x05\x12\x10\n\x08per_page\x18\x03 \x02(\x05\x12\x13\n\x0btotal_items\x18\x04 \x02(\x05\x12\x11\n\tnum_pages\x18\x05 \x02(\x05\x32\x84\x02\n\x04Role\x12.\n\x05table\x12\x11.RoleTableRequest\x1a\x12.RoleTableResponse\x12,\n\x07get_all\x12\n.RoleEmpty\x1a\x15.RoleMultipleResponse\x12$\n\x03get\x12\x0e.RoleIdRequest\x1a\r.RoleResponse\x12(\n\x04save\x12\x11.RoleNotIdRequest\x1a\r.RoleResponse\x12%\n\x06update\x12\x0c.RoleRequest\x1a\r.RoleResponse\x12\'\n\x06\x64\x65lete\x12\x0e.RoleIdRequest\x1a\r.RoleResponse'
)




_ROLEEMPTY = _descriptor.Descriptor(
  name='RoleEmpty',
  full_name='RoleEmpty',
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
  serialized_start=32,
  serialized_end=43,
)


_ROLEIDREQUEST = _descriptor.Descriptor(
  name='RoleIdRequest',
  full_name='RoleIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RoleIdRequest.id', index=0,
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
  serialized_start=45,
  serialized_end=72,
)


_ROLENOTIDREQUEST = _descriptor.Descriptor(
  name='RoleNotIdRequest',
  full_name='RoleNotIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RoleNotIdRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='RoleNotIdRequest.code', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='RoleNotIdRequest.scopes', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=74,
  serialized_end=136,
)


_ROLEREQUEST = _descriptor.Descriptor(
  name='RoleRequest',
  full_name='RoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RoleRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='RoleRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='RoleRequest.code', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='RoleRequest.scopes', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=138,
  serialized_end=207,
)


_ROLETABLEREQUEST = _descriptor.Descriptor(
  name='RoleTableRequest',
  full_name='RoleTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='RoleTableRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='RoleTableRequest.per_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='RoleTableRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=209,
  serialized_end=279,
)


_ROLERESPONSE = _descriptor.Descriptor(
  name='RoleResponse',
  full_name='RoleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='RoleResponse.role', index=0,
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
  serialized_start=281,
  serialized_end=323,
)


_ROLEMULTIPLERESPONSE = _descriptor.Descriptor(
  name='RoleMultipleResponse',
  full_name='RoleMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='RoleMultipleResponse.role', index=0,
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
  serialized_start=325,
  serialized_end=375,
)


_ROLETABLERESPONSE = _descriptor.Descriptor(
  name='RoleTableResponse',
  full_name='RoleTableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='RoleTableResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='RoleTableResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='RoleTableResponse.per_page', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_items', full_name='RoleTableResponse.total_items', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_pages', full_name='RoleTableResponse.num_pages', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=377,
  serialized_end=497,
)

_ROLERESPONSE.fields_by_name['role'].message_type = _ROLEREQUEST
_ROLEMULTIPLERESPONSE.fields_by_name['role'].message_type = _ROLEREQUEST
_ROLETABLERESPONSE.fields_by_name['items'].message_type = _ROLEREQUEST
DESCRIPTOR.message_types_by_name['RoleEmpty'] = _ROLEEMPTY
DESCRIPTOR.message_types_by_name['RoleIdRequest'] = _ROLEIDREQUEST
DESCRIPTOR.message_types_by_name['RoleNotIdRequest'] = _ROLENOTIDREQUEST
DESCRIPTOR.message_types_by_name['RoleRequest'] = _ROLEREQUEST
DESCRIPTOR.message_types_by_name['RoleTableRequest'] = _ROLETABLEREQUEST
DESCRIPTOR.message_types_by_name['RoleResponse'] = _ROLERESPONSE
DESCRIPTOR.message_types_by_name['RoleMultipleResponse'] = _ROLEMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['RoleTableResponse'] = _ROLETABLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleEmpty = _reflection.GeneratedProtocolMessageType('RoleEmpty', (_message.Message,), {
  'DESCRIPTOR' : _ROLEEMPTY,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleEmpty)
  })
_sym_db.RegisterMessage(RoleEmpty)

RoleIdRequest = _reflection.GeneratedProtocolMessageType('RoleIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEIDREQUEST,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleIdRequest)
  })
_sym_db.RegisterMessage(RoleIdRequest)

RoleNotIdRequest = _reflection.GeneratedProtocolMessageType('RoleNotIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLENOTIDREQUEST,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleNotIdRequest)
  })
_sym_db.RegisterMessage(RoleNotIdRequest)

RoleRequest = _reflection.GeneratedProtocolMessageType('RoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEREQUEST,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleRequest)
  })
_sym_db.RegisterMessage(RoleRequest)

RoleTableRequest = _reflection.GeneratedProtocolMessageType('RoleTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLETABLEREQUEST,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleTableRequest)
  })
_sym_db.RegisterMessage(RoleTableRequest)

RoleResponse = _reflection.GeneratedProtocolMessageType('RoleResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLERESPONSE,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleResponse)
  })
_sym_db.RegisterMessage(RoleResponse)

RoleMultipleResponse = _reflection.GeneratedProtocolMessageType('RoleMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEMULTIPLERESPONSE,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleMultipleResponse)
  })
_sym_db.RegisterMessage(RoleMultipleResponse)

RoleTableResponse = _reflection.GeneratedProtocolMessageType('RoleTableResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLETABLERESPONSE,
  '__module__' : 'app.services.role.role_pb2'
  # @@protoc_insertion_point(class_scope:RoleTableResponse)
  })
_sym_db.RegisterMessage(RoleTableResponse)



_ROLE = _descriptor.ServiceDescriptor(
  name='Role',
  full_name='Role',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=500,
  serialized_end=760,
  methods=[
  _descriptor.MethodDescriptor(
    name='table',
    full_name='Role.table',
    index=0,
    containing_service=None,
    input_type=_ROLETABLEREQUEST,
    output_type=_ROLETABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='Role.get_all',
    index=1,
    containing_service=None,
    input_type=_ROLEEMPTY,
    output_type=_ROLEMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='Role.get',
    index=2,
    containing_service=None,
    input_type=_ROLEIDREQUEST,
    output_type=_ROLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='save',
    full_name='Role.save',
    index=3,
    containing_service=None,
    input_type=_ROLENOTIDREQUEST,
    output_type=_ROLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='Role.update',
    index=4,
    containing_service=None,
    input_type=_ROLEREQUEST,
    output_type=_ROLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='Role.delete',
    index=5,
    containing_service=None,
    input_type=_ROLEIDREQUEST,
    output_type=_ROLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLE)

DESCRIPTOR.services_by_name['Role'] = _ROLE

# @@protoc_insertion_point(module_scope)