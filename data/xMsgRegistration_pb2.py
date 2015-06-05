# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xMsgRegistration.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xMsgRegistration.proto',
  package='',
  serialized_pb='\n\x16xMsgRegistration.proto\"\xfd\x01\n\x10xMsgRegistration\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\t:\tundefined\x12\x0c\n\x04host\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\x0f\x12\x0e\n\x06\x64omain\x18\x05 \x02(\t\x12\x1a\n\x07subject\x18\x06 \x01(\t:\tundefined\x12\x17\n\x04type\x18\x07 \x01(\t:\tundefined\x12.\n\townerType\x18\x08 \x01(\x0e\x32\x1b.xMsgRegistration.OwnerType\"*\n\tOwnerType\x12\r\n\tPUBLISHER\x10\x01\x12\x0e\n\nSUBSCRIBER\x10\x02\x42\tB\x05xMsgRH\x01')



_XMSGREGISTRATION_OWNERTYPE = _descriptor.EnumDescriptor(
  name='OwnerType',
  full_name='xMsgRegistration.OwnerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUBLISHER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBER', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=238,
  serialized_end=280,
)


_XMSGREGISTRATION = _descriptor.Descriptor(
  name='xMsgRegistration',
  full_name='xMsgRegistration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xMsgRegistration.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='xMsgRegistration.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("undefined", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='xMsgRegistration.host', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='xMsgRegistration.port', index=3,
      number=4, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='xMsgRegistration.domain', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='xMsgRegistration.subject', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("undefined", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='xMsgRegistration.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("undefined", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ownerType', full_name='xMsgRegistration.ownerType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _XMSGREGISTRATION_OWNERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=280,
)

_XMSGREGISTRATION.fields_by_name['ownerType'].enum_type = _XMSGREGISTRATION_OWNERTYPE
_XMSGREGISTRATION_OWNERTYPE.containing_type = _XMSGREGISTRATION;
DESCRIPTOR.message_types_by_name['xMsgRegistration'] = _XMSGREGISTRATION

class xMsgRegistration(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XMSGREGISTRATION

  # @@protoc_insertion_point(class_scope:xMsgRegistration)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'B\005xMsgRH\001')
# @@protoc_insertion_point(module_scope)
