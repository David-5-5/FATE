# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nn-model-meta.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='nn-model-meta.proto',
    package='com.webank.ai.fate.core.mlmodel.buffer',
    syntax='proto3',
    serialized_options=_b('B\020NNModelMetaProto'),
    serialized_pb=_b('\n\x13nn-model-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\",\n\tEarlyStop\x12\x12\n\nearly_stop\x18\x01 \x01(\t\x12\x0b\n\x03\x65ps\x18\x02 \x01(\x01\",\n\tOptimizer\x12\x11\n\toptimizer\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x01(\t\"\xd8\x02\n\x0bHomoNNParam\x12\x18\n\x10secure_aggregate\x18\x01 \x01(\x08\x12\x1f\n\x17\x61ggregate_every_n_epoch\x18\x02 \x01(\x05\x12\x13\n\x0b\x63onfig_type\x18\x03 \x01(\t\x12\x11\n\tnn_define\x18\x04 \x03(\t\x12\x12\n\nbatch_size\x18\x05 \x01(\x05\x12\x10\n\x08max_iter\x18\x06 \x01(\x05\x12\x45\n\nearly_stop\x18\x07 \x01(\x0b\x32\x31.com.webank.ai.fate.core.mlmodel.buffer.EarlyStop\x12\x0f\n\x07metrics\x18\x08 \x03(\t\x12\x44\n\toptimizer\x18\t \x01(\x0b\x32\x31.com.webank.ai.fate.core.mlmodel.buffer.Optimizer\x12\x0c\n\x04loss\x18\n \x01(\t\x12\x14\n\x0c\x65ncode_label\x18\x0b \x01(\x08\"z\n\x0bNNModelMeta\x12\x16\n\x0e\x61ggregate_iter\x18\x01 \x01(\x05\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\x43\n\x06params\x18\x64 \x01(\x0b\x32\x33.com.webank.ai.fate.core.mlmodel.buffer.HomoNNParamB\x12\x42\x10NNModelMetaProtob\x06proto3')
)


_EARLYSTOP = _descriptor.Descriptor(
    name='EarlyStop',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.EarlyStop',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.EarlyStop.early_stop', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='eps', full_name='com.webank.ai.fate.core.mlmodel.buffer.EarlyStop.eps', index=1,
            number=2, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=63,
    serialized_end=107,
)


_OPTIMIZER = _descriptor.Descriptor(
    name='Optimizer',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer.optimizer', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='args', full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer.args', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=109,
    serialized_end=153,
)


_HOMONNPARAM = _descriptor.Descriptor(
    name='HomoNNParam',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='secure_aggregate', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.secure_aggregate', index=0,
            number=1, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='aggregate_every_n_epoch', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.aggregate_every_n_epoch', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='config_type', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.config_type', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='nn_define', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.nn_define', index=3,
            number=4, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='batch_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.batch_size', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='max_iter', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.max_iter', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.early_stop', index=6,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='metrics', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.metrics', index=7,
            number=8, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.optimizer', index=8,
            number=9, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='loss', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.loss', index=9,
            number=10, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='encode_label', full_name='com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam.encode_label', index=10,
            number=11, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=156,
    serialized_end=500,
)


_NNMODELMETA = _descriptor.Descriptor(
    name='NNModelMeta',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.NNModelMeta',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='aggregate_iter',
            full_name='com.webank.ai.fate.core.mlmodel.buffer.NNModelMeta.aggregate_iter',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='module',
            full_name='com.webank.ai.fate.core.mlmodel.buffer.NNModelMeta.module',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='params',
            full_name='com.webank.ai.fate.core.mlmodel.buffer.NNModelMeta.params',
            index=2,
            number=100,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=502,
    serialized_end=624,
)

_HOMONNPARAM.fields_by_name['early_stop'].message_type = _EARLYSTOP
_HOMONNPARAM.fields_by_name['optimizer'].message_type = _OPTIMIZER
_NNMODELMETA.fields_by_name['params'].message_type = _HOMONNPARAM
DESCRIPTOR.message_types_by_name['EarlyStop'] = _EARLYSTOP
DESCRIPTOR.message_types_by_name['Optimizer'] = _OPTIMIZER
DESCRIPTOR.message_types_by_name['HomoNNParam'] = _HOMONNPARAM
DESCRIPTOR.message_types_by_name['NNModelMeta'] = _NNMODELMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EarlyStop = _reflection.GeneratedProtocolMessageType('EarlyStop', (_message.Message,), {
    'DESCRIPTOR': _EARLYSTOP,
    '__module__': 'nn_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.EarlyStop)
})
_sym_db.RegisterMessage(EarlyStop)

Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), {
    'DESCRIPTOR': _OPTIMIZER,
    '__module__': 'nn_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Optimizer)
})
_sym_db.RegisterMessage(Optimizer)

HomoNNParam = _reflection.GeneratedProtocolMessageType('HomoNNParam', (_message.Message,), {
    'DESCRIPTOR': _HOMONNPARAM,
    '__module__': 'nn_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.HomoNNParam)
})
_sym_db.RegisterMessage(HomoNNParam)

NNModelMeta = _reflection.GeneratedProtocolMessageType('NNModelMeta', (_message.Message,), {
    'DESCRIPTOR': _NNMODELMETA,
    '__module__': 'nn_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.NNModelMeta)
})
_sym_db.RegisterMessage(NNModelMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
