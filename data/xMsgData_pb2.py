# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xMsgData.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xMsgData.proto',
  package='',
  serialized_pb='\n\x0exMsgData.proto\"\xb8\t\n\x04\x44\x61ta\x12\x13\n\x0b\x64\x61taVersion\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x61taDescription\x18\x02 \x01(\t\x12\x12\n\ndataAuthor\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x61taAuthorState\x18\x04 \x01(\t\x12\x32\n\x14\x64\x61taGenerationStatus\x18\x05 \x01(\x0e\x32\x0e.Data.Severity:\x04INFO\x12\x10\n\x08VLSINT32\x18\x06 \x01(\x11\x12\x10\n\x08VLSINT64\x18\x07 \x01(\x12\x12\x10\n\x08\x46LSINT32\x18\x08 \x01(\x0f\x12\x10\n\x08\x46LSINT64\x18\t \x01(\x10\x12\r\n\x05\x46LOAT\x18\n \x01(\x02\x12\x0e\n\x06\x44OUBLE\x18\x0b \x01(\x01\x12\x0e\n\x06STRING\x18\x0c \x01(\t\x12\r\n\x05\x42YTES\x18\r \x01(\x0c\x12\x11\n\tVLSINT32A\x18\x0e \x03(\x11\x12\x11\n\tVLSINT64A\x18\x0f \x03(\x12\x12\x11\n\tFLSINT32A\x18\x10 \x03(\x0f\x12\x11\n\tFLSINT64A\x18\x11 \x03(\x10\x12\x0e\n\x06\x46LOATA\x18\x12 \x03(\x02\x12\x0f\n\x07\x44OUBLEA\x18\x13 \x03(\x01\x12\x0f\n\x07STRINGA\x18\x14 \x03(\t\x12\x0e\n\x06\x42YTESA\x18\x15 \x03(\x0c\x12\x1d\n\x08\x64\x61taType\x18\x16 \x01(\x0e\x32\x0b.Data.DType\x12\x11\n\tbyteOrder\x18\x17 \x01(\t\x12\x0e\n\x06sender\x18\x18 \x01(\t\x12\n\n\x02id\x18\x19 \x01(\x07\x12\x18\n\x10\x65xceptionMonitor\x18\x1a \x01(\x08\x12\x13\n\x0b\x64oneMonitor\x18\x1b \x01(\x08\x12\x13\n\x0b\x64\x61taMonitor\x18\x1c \x01(\x08\x12\x13\n\x0b\x63omposition\x18\x1d \x01(\t\x12\x15\n\rexecutionTime\x18\x1e \x01(\x10\x12#\n\x06\x61\x63tion\x18\x1f \x01(\x0e\x32\x13.Data.ControlAction\x12(\n\x08\x63ontrolR\x18  \x01(\x0e\x32\x16.Data.SubControlAction\"\x8a\x02\n\x05\x44Type\x12\x0e\n\nT_VLSINT32\x10\x01\x12\x0e\n\nT_VLSINT64\x10\x02\x12\x0e\n\nT_FLSINT32\x10\x03\x12\x0e\n\nT_FLSINT64\x10\x04\x12\x0b\n\x07T_FLOAT\x10\x05\x12\x0c\n\x08T_DOUBLE\x10\x06\x12\x0c\n\x08T_STRING\x10\x07\x12\x0b\n\x07T_BYTES\x10\x08\x12\x0f\n\x0bT_VLSINT32A\x10\t\x12\x0f\n\x0bT_VLSINT64A\x10\n\x12\x0f\n\x0bT_FLSINT32A\x10\x0b\x12\x0f\n\x0bT_FLSINT64A\x10\x0c\x12\x0c\n\x08T_FLOATA\x10\r\x12\r\n\tT_DOUBLEA\x10\x0e\x12\r\n\tT_STRINGA\x10\x0f\x12\x0c\n\x08T_BYTESA\x10\x10\x12\r\n\tT_PAYLOAD\x10\x11\"D\n\x06\x42\x41Type\x12\x0b\n\x07JOBJECT\x10\x01\x12\x0b\n\x07\x43OBJECT\x10\x02\x12\x0b\n\x07POBJECT\x10\x03\x12\n\n\x06NETCDF\x10\x04\x12\x07\n\x03HDF\x10\x05\"+\n\rControlAction\x12\x0b\n\x07\x45XECUTE\x10\x00\x12\r\n\tCONFIGURE\x10\x01\"\x1c\n\x10SubControlAction\x12\x08\n\x04SKIP\x10\x00\"b\n\x08Severity\x12\n\n\x06\x45RROR1\x10\x01\x12\n\n\x06\x45RROR2\x10\x02\x12\n\n\x06\x45RROR3\x10\x03\x12\x0c\n\x08WARNING1\x10\x04\x12\x0c\n\x08WARNING2\x10\x05\x12\x0c\n\x08WARNING3\x10\x06\x12\x08\n\x04INFO\x10\x07\"Q\n\x07Payload\x12\x1b\n\x04item\x18\x01 \x03(\x0b\x32\r.Payload.Item\x1a)\n\x04Item\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x04\x64\x61ta\x18\x02 \x02(\x0b\x32\x05.DataB\tB\x05xMsgDH\x01')



_DATA_DTYPE = _descriptor.EnumDescriptor(
  name='DType',
  full_name='Data.DType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='T_VLSINT32', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_VLSINT64', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLSINT32', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLSINT64', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLOAT', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_DOUBLE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_STRING', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_BYTES', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_VLSINT32A', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_VLSINT64A', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLSINT32A', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLSINT64A', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_FLOATA', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_DOUBLEA', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_STRINGA', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_BYTESA', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T_PAYLOAD', index=16, number=17,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=716,
  serialized_end=982,
)

_DATA_BATYPE = _descriptor.EnumDescriptor(
  name='BAType',
  full_name='Data.BAType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOBJECT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COBJECT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POBJECT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETCDF', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDF', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=984,
  serialized_end=1052,
)

_DATA_CONTROLACTION = _descriptor.EnumDescriptor(
  name='ControlAction',
  full_name='Data.ControlAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXECUTE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIGURE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1054,
  serialized_end=1097,
)

_DATA_SUBCONTROLACTION = _descriptor.EnumDescriptor(
  name='SubControlAction',
  full_name='Data.SubControlAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SKIP', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1099,
  serialized_end=1127,
)

_DATA_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='Data.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR1', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR2', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR3', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING1', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING2', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING3', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1129,
  serialized_end=1227,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataVersion', full_name='Data.dataVersion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataDescription', full_name='Data.dataDescription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataAuthor', full_name='Data.dataAuthor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataAuthorState', full_name='Data.dataAuthorState', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataGenerationStatus', full_name='Data.dataGenerationStatus', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VLSINT32', full_name='Data.VLSINT32', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VLSINT64', full_name='Data.VLSINT64', index=6,
      number=7, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLSINT32', full_name='Data.FLSINT32', index=7,
      number=8, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLSINT64', full_name='Data.FLSINT64', index=8,
      number=9, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLOAT', full_name='Data.FLOAT', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DOUBLE', full_name='Data.DOUBLE', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='STRING', full_name='Data.STRING', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BYTES', full_name='Data.BYTES', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VLSINT32A', full_name='Data.VLSINT32A', index=13,
      number=14, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VLSINT64A', full_name='Data.VLSINT64A', index=14,
      number=15, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLSINT32A', full_name='Data.FLSINT32A', index=15,
      number=16, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLSINT64A', full_name='Data.FLSINT64A', index=16,
      number=17, type=16, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FLOATA', full_name='Data.FLOATA', index=17,
      number=18, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DOUBLEA', full_name='Data.DOUBLEA', index=18,
      number=19, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='STRINGA', full_name='Data.STRINGA', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BYTESA', full_name='Data.BYTESA', index=20,
      number=21, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='Data.dataType', index=21,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='byteOrder', full_name='Data.byteOrder', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='Data.sender', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Data.id', index=24,
      number=25, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exceptionMonitor', full_name='Data.exceptionMonitor', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doneMonitor', full_name='Data.doneMonitor', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataMonitor', full_name='Data.dataMonitor', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='composition', full_name='Data.composition', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='executionTime', full_name='Data.executionTime', index=29,
      number=30, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Data.action', index=30,
      number=31, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controlR', full_name='Data.controlR', index=31,
      number=32, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATA_DTYPE,
    _DATA_BATYPE,
    _DATA_CONTROLACTION,
    _DATA_SUBCONTROLACTION,
    _DATA_SEVERITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=1227,
)


_PAYLOAD_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Payload.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Payload.Item.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Payload.Item.data', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1269,
  serialized_end=1310,
)

_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='Payload.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PAYLOAD_ITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1229,
  serialized_end=1310,
)

_DATA.fields_by_name['dataGenerationStatus'].enum_type = _DATA_SEVERITY
_DATA.fields_by_name['dataType'].enum_type = _DATA_DTYPE
_DATA.fields_by_name['action'].enum_type = _DATA_CONTROLACTION
_DATA.fields_by_name['controlR'].enum_type = _DATA_SUBCONTROLACTION
_DATA_DTYPE.containing_type = _DATA;
_DATA_BATYPE.containing_type = _DATA;
_DATA_CONTROLACTION.containing_type = _DATA;
_DATA_SUBCONTROLACTION.containing_type = _DATA;
_DATA_SEVERITY.containing_type = _DATA;
_PAYLOAD_ITEM.fields_by_name['data'].message_type = _DATA
_PAYLOAD_ITEM.containing_type = _PAYLOAD;
_PAYLOAD.fields_by_name['item'].message_type = _PAYLOAD_ITEM
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD

class Data(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATA

  # @@protoc_insertion_point(class_scope:Data)

class Payload(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Item(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PAYLOAD_ITEM

    # @@protoc_insertion_point(class_scope:Payload.Item)
  DESCRIPTOR = _PAYLOAD

  # @@protoc_insertion_point(class_scope:Payload)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'B\005xMsgDH\001')
# @@protoc_insertion_point(module_scope)
