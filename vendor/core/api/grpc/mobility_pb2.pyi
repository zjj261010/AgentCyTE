from core.api.grpc import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MobilityAction(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START: _ClassVar[MobilityAction.Enum]
        PAUSE: _ClassVar[MobilityAction.Enum]
        STOP: _ClassVar[MobilityAction.Enum]
    START: MobilityAction.Enum
    PAUSE: MobilityAction.Enum
    STOP: MobilityAction.Enum
    def __init__(self) -> None: ...

class MobilityConfig(_message.Message):
    __slots__ = ("node_id", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    config: _containers.ScalarMap[str, str]
    def __init__(self, node_id: _Optional[int] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetMobilityConfigRequest(_message.Message):
    __slots__ = ("session_id", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetMobilityConfigResponse(_message.Message):
    __slots__ = ("config",)
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    def __init__(self, config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ...) -> None: ...

class SetMobilityConfigRequest(_message.Message):
    __slots__ = ("session_id", "mobility_config")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MOBILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    mobility_config: MobilityConfig
    def __init__(self, session_id: _Optional[int] = ..., mobility_config: _Optional[_Union[MobilityConfig, _Mapping]] = ...) -> None: ...

class SetMobilityConfigResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class MobilityActionRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "action")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    action: MobilityAction.Enum
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., action: _Optional[_Union[MobilityAction.Enum, str]] = ...) -> None: ...

class MobilityActionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...
