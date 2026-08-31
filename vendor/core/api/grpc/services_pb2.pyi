from core.api.grpc import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAction(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START: _ClassVar[ServiceAction.Enum]
        STOP: _ClassVar[ServiceAction.Enum]
        RESTART: _ClassVar[ServiceAction.Enum]
        VALIDATE: _ClassVar[ServiceAction.Enum]
    START: ServiceAction.Enum
    STOP: ServiceAction.Enum
    RESTART: ServiceAction.Enum
    VALIDATE: ServiceAction.Enum
    def __init__(self) -> None: ...

class ServiceDefaults(_message.Message):
    __slots__ = ("model", "services")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    model: str
    services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ...) -> None: ...

class ServiceActionRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "service", "action")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    service: str
    action: ServiceAction.Enum
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., service: _Optional[str] = ..., action: _Optional[_Union[ServiceAction.Enum, str]] = ...) -> None: ...

class ServiceActionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class ServiceConfig(_message.Message):
    __slots__ = ("templates", "config")
    class TemplatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.ScalarMap[str, str]
    config: _containers.ScalarMap[str, str]
    def __init__(self, templates: _Optional[_Mapping[str, str]] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ServiceValidationMode(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKING: _ClassVar[ServiceValidationMode.Enum]
        NON_BLOCKING: _ClassVar[ServiceValidationMode.Enum]
        TIMER: _ClassVar[ServiceValidationMode.Enum]
    BLOCKING: ServiceValidationMode.Enum
    NON_BLOCKING: ServiceValidationMode.Enum
    TIMER: ServiceValidationMode.Enum
    def __init__(self) -> None: ...

class Service(_message.Message):
    __slots__ = ("group", "name", "executables", "dependencies", "directories", "files", "startup", "validate", "shutdown", "validation_mode", "validation_timer", "validation_period")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLES_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    STARTUP_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_MODE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_TIMER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    group: str
    name: str
    executables: _containers.RepeatedScalarFieldContainer[str]
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    directories: _containers.RepeatedScalarFieldContainer[str]
    files: _containers.RepeatedScalarFieldContainer[str]
    startup: _containers.RepeatedScalarFieldContainer[str]
    validate: _containers.RepeatedScalarFieldContainer[str]
    shutdown: _containers.RepeatedScalarFieldContainer[str]
    validation_mode: ServiceValidationMode.Enum
    validation_timer: int
    validation_period: float
    def __init__(self, group: _Optional[str] = ..., name: _Optional[str] = ..., executables: _Optional[_Iterable[str]] = ..., dependencies: _Optional[_Iterable[str]] = ..., directories: _Optional[_Iterable[str]] = ..., files: _Optional[_Iterable[str]] = ..., startup: _Optional[_Iterable[str]] = ..., validate: _Optional[_Iterable[str]] = ..., shutdown: _Optional[_Iterable[str]] = ..., validation_mode: _Optional[_Union[ServiceValidationMode.Enum, str]] = ..., validation_timer: _Optional[int] = ..., validation_period: _Optional[float] = ...) -> None: ...

class ConfigMode(_message.Message):
    __slots__ = ("name", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetServiceDefaultsRequest(_message.Message):
    __slots__ = ("name", "session_id", "node_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    session_id: int
    node_id: int
    def __init__(self, name: _Optional[str] = ..., session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetServiceDefaultsResponse(_message.Message):
    __slots__ = ("templates", "config", "modes")
    class TemplatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.ScalarMap[str, str]
    config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    modes: _containers.RepeatedCompositeFieldContainer[ConfigMode]
    def __init__(self, templates: _Optional[_Mapping[str, str]] = ..., config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ..., modes: _Optional[_Iterable[_Union[ConfigMode, _Mapping]]] = ...) -> None: ...

class GetNodeServiceRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "name")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    name: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetNodeServiceResponse(_message.Message):
    __slots__ = ("config",)
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _containers.ScalarMap[str, str]
    def __init__(self, config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetServiceRenderedRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "name")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    name: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetServiceRenderedResponse(_message.Message):
    __slots__ = ("rendered",)
    class RenderedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RENDERED_FIELD_NUMBER: _ClassVar[int]
    rendered: _containers.ScalarMap[str, str]
    def __init__(self, rendered: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateServiceRequest(_message.Message):
    __slots__ = ("service", "templates", "recreate")
    class TemplatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    RECREATE_FIELD_NUMBER: _ClassVar[int]
    service: Service
    templates: _containers.ScalarMap[str, str]
    recreate: bool
    def __init__(self, service: _Optional[_Union[Service, _Mapping]] = ..., templates: _Optional[_Mapping[str, str]] = ..., recreate: bool = ...) -> None: ...

class CreateServiceResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...
