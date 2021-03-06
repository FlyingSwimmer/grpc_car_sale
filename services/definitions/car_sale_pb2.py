# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/definitions/car_sale.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/definitions/car_sale.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#services/definitions/car_sale.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb4\x01\n\rAdvertisement\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05owner\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61r_name\x18\x05 \x01(\t\x12\x11\n\tcar_model\x18\x06 \x01(\t\x12\x11\n\tmin_price\x18\x07 \x01(\x03\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"z\n\x05Offer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04user\x18\x02 \x01(\x05\x12\x15\n\radvertisement\x18\x03 \x01(\x05\x12\r\n\x05price\x18\x04 \x01(\x03\x12\x31\n\rcreation_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x10\n\x0e\x41\x64sListRequest\"/\n\x0f\x41\x64sListResponse\x12\x1c\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0e.Advertisement\"T\n\x0f\x41\x64\x64OfferRequest\x12\x1b\n\x02uc\x18\x01 \x01(\x0b\x32\x0f.UserCredential\x12\x15\n\radvertisement\x18\x02 \x01(\x05\x12\r\n\x05price\x18\x03 \x01(\x03\"(\n\x10\x41\x64\x64OfferResponse\x12\x14\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x06.Offer\"\xc0\x01\n\x17\x41\x64\x64\x41\x64vertisementRequest\x12\x1b\n\x02uc\x18\x01 \x01(\x0b\x32\x0f.UserCredential\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61r_name\x18\x04 \x01(\t\x12\x11\n\tcar_model\x18\x05 \x01(\t\x12\x11\n\tmin_price\x18\x06 \x01(\x03\x12,\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\x18\x41\x64\x64\x41\x64vertisementResponse\x12\x1c\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0e.Advertisement\"4\n\x0eUserCredential\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t2\xba\x01\n\x07\x43\x61rSale\x12\x31\n\nGetAdsList\x12\x0f.AdsListRequest\x1a\x10.AdsListResponse\"\x00\x12\x31\n\x08\x41\x64\x64Offer\x12\x10.AddOfferRequest\x1a\x11.AddOfferResponse\"\x00\x12I\n\x10\x41\x64\x64\x41\x64vertisement\x12\x18.AddAdvertisementRequest\x1a\x19.AddAdvertisementResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ADVERTISEMENT = _descriptor.Descriptor(
  name='Advertisement',
  full_name='Advertisement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Advertisement.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='Advertisement.owner', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='Advertisement.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='Advertisement.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='car_name', full_name='Advertisement.car_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='car_model', full_name='Advertisement.car_model', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_price', full_name='Advertisement.min_price', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='Advertisement.end_time', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=253,
)


_OFFER = _descriptor.Descriptor(
  name='Offer',
  full_name='Offer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Offer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='Offer.user', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertisement', full_name='Offer.advertisement', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='Offer.price', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='Offer.creation_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=377,
)


_ADSLISTREQUEST = _descriptor.Descriptor(
  name='AdsListRequest',
  full_name='AdsListRequest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=395,
)


_ADSLISTRESPONSE = _descriptor.Descriptor(
  name='AdsListResponse',
  full_name='AdsListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='AdsListResponse.data', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=444,
)


_ADDOFFERREQUEST = _descriptor.Descriptor(
  name='AddOfferRequest',
  full_name='AddOfferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uc', full_name='AddOfferRequest.uc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertisement', full_name='AddOfferRequest.advertisement', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='AddOfferRequest.price', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=530,
)


_ADDOFFERRESPONSE = _descriptor.Descriptor(
  name='AddOfferResponse',
  full_name='AddOfferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='AddOfferResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=572,
)


_ADDADVERTISEMENTREQUEST = _descriptor.Descriptor(
  name='AddAdvertisementRequest',
  full_name='AddAdvertisementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uc', full_name='AddAdvertisementRequest.uc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='AddAdvertisementRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='AddAdvertisementRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='car_name', full_name='AddAdvertisementRequest.car_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='car_model', full_name='AddAdvertisementRequest.car_model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_price', full_name='AddAdvertisementRequest.min_price', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='AddAdvertisementRequest.end_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=767,
)


_ADDADVERTISEMENTRESPONSE = _descriptor.Descriptor(
  name='AddAdvertisementResponse',
  full_name='AddAdvertisementResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='AddAdvertisementResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=825,
)


_USERCREDENTIAL = _descriptor.Descriptor(
  name='UserCredential',
  full_name='UserCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='UserCredential.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='UserCredential.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=879,
)

_ADVERTISEMENT.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OFFER.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ADSLISTRESPONSE.fields_by_name['data'].message_type = _ADVERTISEMENT
_ADDOFFERREQUEST.fields_by_name['uc'].message_type = _USERCREDENTIAL
_ADDOFFERRESPONSE.fields_by_name['data'].message_type = _OFFER
_ADDADVERTISEMENTREQUEST.fields_by_name['uc'].message_type = _USERCREDENTIAL
_ADDADVERTISEMENTREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ADDADVERTISEMENTRESPONSE.fields_by_name['data'].message_type = _ADVERTISEMENT
DESCRIPTOR.message_types_by_name['Advertisement'] = _ADVERTISEMENT
DESCRIPTOR.message_types_by_name['Offer'] = _OFFER
DESCRIPTOR.message_types_by_name['AdsListRequest'] = _ADSLISTREQUEST
DESCRIPTOR.message_types_by_name['AdsListResponse'] = _ADSLISTRESPONSE
DESCRIPTOR.message_types_by_name['AddOfferRequest'] = _ADDOFFERREQUEST
DESCRIPTOR.message_types_by_name['AddOfferResponse'] = _ADDOFFERRESPONSE
DESCRIPTOR.message_types_by_name['AddAdvertisementRequest'] = _ADDADVERTISEMENTREQUEST
DESCRIPTOR.message_types_by_name['AddAdvertisementResponse'] = _ADDADVERTISEMENTRESPONSE
DESCRIPTOR.message_types_by_name['UserCredential'] = _USERCREDENTIAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Advertisement = _reflection.GeneratedProtocolMessageType('Advertisement', (_message.Message,), {
  'DESCRIPTOR' : _ADVERTISEMENT,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:Advertisement)
  })
_sym_db.RegisterMessage(Advertisement)

Offer = _reflection.GeneratedProtocolMessageType('Offer', (_message.Message,), {
  'DESCRIPTOR' : _OFFER,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:Offer)
  })
_sym_db.RegisterMessage(Offer)

AdsListRequest = _reflection.GeneratedProtocolMessageType('AdsListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADSLISTREQUEST,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AdsListRequest)
  })
_sym_db.RegisterMessage(AdsListRequest)

AdsListResponse = _reflection.GeneratedProtocolMessageType('AdsListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADSLISTRESPONSE,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AdsListResponse)
  })
_sym_db.RegisterMessage(AdsListResponse)

AddOfferRequest = _reflection.GeneratedProtocolMessageType('AddOfferRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDOFFERREQUEST,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AddOfferRequest)
  })
_sym_db.RegisterMessage(AddOfferRequest)

AddOfferResponse = _reflection.GeneratedProtocolMessageType('AddOfferResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDOFFERRESPONSE,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AddOfferResponse)
  })
_sym_db.RegisterMessage(AddOfferResponse)

AddAdvertisementRequest = _reflection.GeneratedProtocolMessageType('AddAdvertisementRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDADVERTISEMENTREQUEST,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AddAdvertisementRequest)
  })
_sym_db.RegisterMessage(AddAdvertisementRequest)

AddAdvertisementResponse = _reflection.GeneratedProtocolMessageType('AddAdvertisementResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDADVERTISEMENTRESPONSE,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:AddAdvertisementResponse)
  })
_sym_db.RegisterMessage(AddAdvertisementResponse)

UserCredential = _reflection.GeneratedProtocolMessageType('UserCredential', (_message.Message,), {
  'DESCRIPTOR' : _USERCREDENTIAL,
  '__module__' : 'services.definitions.car_sale_pb2'
  # @@protoc_insertion_point(class_scope:UserCredential)
  })
_sym_db.RegisterMessage(UserCredential)



_CARSALE = _descriptor.ServiceDescriptor(
  name='CarSale',
  full_name='CarSale',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=882,
  serialized_end=1068,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdsList',
    full_name='CarSale.GetAdsList',
    index=0,
    containing_service=None,
    input_type=_ADSLISTREQUEST,
    output_type=_ADSLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddOffer',
    full_name='CarSale.AddOffer',
    index=1,
    containing_service=None,
    input_type=_ADDOFFERREQUEST,
    output_type=_ADDOFFERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddAdvertisement',
    full_name='CarSale.AddAdvertisement',
    index=2,
    containing_service=None,
    input_type=_ADDADVERTISEMENTREQUEST,
    output_type=_ADDADVERTISEMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CARSALE)

DESCRIPTOR.services_by_name['CarSale'] = _CARSALE

# @@protoc_insertion_point(module_scope)
