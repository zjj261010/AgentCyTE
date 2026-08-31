from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigOption(_message.Message):
    __slots__ = ("label", "name", "value", "type", "select", "group", "regex")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REGEX_FIELD_NUMBER: _ClassVar[int]
    label: str
    name: str
    value: str
    type: int
    select: _containers.RepeatedScalarFieldContainer[str]
    group: str
    regex: str
    def __init__(self, label: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[int] = ..., select: _Optional[_Iterable[str]] = ..., group: _Optional[str] = ..., regex: _Optional[str] = ...) -> None: ...

class MappedConfig(_message.Message):
    __slots__ = ("config",)
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConfigOption, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _containers.MessageMap[str, ConfigOption]
    def __init__(self, config: _Optional[_Mapping[str, ConfigOption]] = ...) -> None: ...
