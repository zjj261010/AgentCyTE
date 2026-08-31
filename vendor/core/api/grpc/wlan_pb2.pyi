from core.api.grpc import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WlanConfig(_message.Message):
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

class GetWlanConfigRequest(_message.Message):
    __slots__ = ("session_id", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetWlanConfigResponse(_message.Message):
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

class SetWlanConfigRequest(_message.Message):
    __slots__ = ("session_id", "wlan_config")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WLAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    wlan_config: WlanConfig
    def __init__(self, session_id: _Optional[int] = ..., wlan_config: _Optional[_Union[WlanConfig, _Mapping]] = ...) -> None: ...

class SetWlanConfigResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class WlanLinkRequest(_message.Message):
    __slots__ = ("session_id", "wlan", "node1_id", "node2_id", "linked")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WLAN_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    wlan: int
    node1_id: int
    node2_id: int
    linked: bool
    def __init__(self, session_id: _Optional[int] = ..., wlan: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., linked: bool = ...) -> None: ...

class WlanLinkResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...
