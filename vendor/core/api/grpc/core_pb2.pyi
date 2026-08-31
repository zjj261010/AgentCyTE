from core.api.grpc import services_pb2 as _services_pb2
from core.api.grpc import common_pb2 as _common_pb2
from core.api.grpc import emane_pb2 as _emane_pb2
from core.api.grpc import mobility_pb2 as _mobility_pb2
from core.api.grpc import wlan_pb2 as _wlan_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("services", "emane_models")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    EMANE_MODELS_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_services_pb2.Service]
    emane_models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, services: _Optional[_Iterable[_Union[_services_pb2.Service, _Mapping]]] = ..., emane_models: _Optional[_Iterable[str]] = ...) -> None: ...

class StartSessionRequest(_message.Message):
    __slots__ = ("session", "definition")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    definition: bool
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., definition: bool = ...) -> None: ...

class StartSessionResponse(_message.Message):
    __slots__ = ("result", "exceptions")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONS_FIELD_NUMBER: _ClassVar[int]
    result: bool
    exceptions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: bool = ..., exceptions: _Optional[_Iterable[str]] = ...) -> None: ...

class StopSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class StopSessionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class GetSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[SessionSummary]
    def __init__(self, sessions: _Optional[_Iterable[_Union[SessionSummary, _Mapping]]] = ...) -> None: ...

class CheckSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CheckSessionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class GetSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class SessionAlertRequest(_message.Message):
    __slots__ = ("session_id", "level", "source", "text", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    level: AlertLevel.Enum
    source: str
    text: str
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., level: _Optional[_Union[AlertLevel.Enum, str]] = ..., source: _Optional[str] = ..., text: _Optional[str] = ..., node_id: _Optional[int] = ...) -> None: ...

class SessionAlertResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class EventsRequest(_message.Message):
    __slots__ = ("session_id", "events")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    events: _containers.RepeatedScalarFieldContainer[EventType.Enum]
    def __init__(self, session_id: _Optional[int] = ..., events: _Optional[_Iterable[_Union[EventType.Enum, str]]] = ...) -> None: ...

class ThroughputsRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class ThroughputsEvent(_message.Message):
    __slots__ = ("session_id", "bridge_throughputs", "iface_throughputs")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_THROUGHPUTS_FIELD_NUMBER: _ClassVar[int]
    IFACE_THROUGHPUTS_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    bridge_throughputs: _containers.RepeatedCompositeFieldContainer[BridgeThroughput]
    iface_throughputs: _containers.RepeatedCompositeFieldContainer[InterfaceThroughput]
    def __init__(self, session_id: _Optional[int] = ..., bridge_throughputs: _Optional[_Iterable[_Union[BridgeThroughput, _Mapping]]] = ..., iface_throughputs: _Optional[_Iterable[_Union[InterfaceThroughput, _Mapping]]] = ...) -> None: ...

class CpuUsageRequest(_message.Message):
    __slots__ = ("delay",)
    DELAY_FIELD_NUMBER: _ClassVar[int]
    delay: int
    def __init__(self, delay: _Optional[int] = ...) -> None: ...

class CpuUsageEvent(_message.Message):
    __slots__ = ("usage",)
    USAGE_FIELD_NUMBER: _ClassVar[int]
    usage: float
    def __init__(self, usage: _Optional[float] = ...) -> None: ...

class InterfaceThroughput(_message.Message):
    __slots__ = ("node_id", "iface_id", "throughput")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    iface_id: int
    throughput: float
    def __init__(self, node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., throughput: _Optional[float] = ...) -> None: ...

class BridgeThroughput(_message.Message):
    __slots__ = ("node_id", "throughput")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    throughput: float
    def __init__(self, node_id: _Optional[int] = ..., throughput: _Optional[float] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("session_event", "node_event", "link_event", "alert_event", "session_id", "source")
    SESSION_EVENT_FIELD_NUMBER: _ClassVar[int]
    NODE_EVENT_FIELD_NUMBER: _ClassVar[int]
    LINK_EVENT_FIELD_NUMBER: _ClassVar[int]
    ALERT_EVENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_event: SessionEvent
    node_event: NodeEvent
    link_event: LinkEvent
    alert_event: AlertEvent
    session_id: int
    source: str
    def __init__(self, session_event: _Optional[_Union[SessionEvent, _Mapping]] = ..., node_event: _Optional[_Union[NodeEvent, _Mapping]] = ..., link_event: _Optional[_Union[LinkEvent, _Mapping]] = ..., alert_event: _Optional[_Union[AlertEvent, _Mapping]] = ..., session_id: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...

class NodeEvent(_message.Message):
    __slots__ = ("node", "message_type")
    NODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    node: Node
    message_type: MessageType.Enum
    def __init__(self, node: _Optional[_Union[Node, _Mapping]] = ..., message_type: _Optional[_Union[MessageType.Enum, str]] = ...) -> None: ...

class LinkEvent(_message.Message):
    __slots__ = ("message_type", "link")
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    message_type: MessageType.Enum
    link: Link
    def __init__(self, message_type: _Optional[_Union[MessageType.Enum, str]] = ..., link: _Optional[_Union[Link, _Mapping]] = ...) -> None: ...

class SessionEvent(_message.Message):
    __slots__ = ("node_id", "event", "name", "data", "time")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    event: int
    name: str
    data: str
    time: float
    def __init__(self, node_id: _Optional[int] = ..., event: _Optional[int] = ..., name: _Optional[str] = ..., data: _Optional[str] = ..., time: _Optional[float] = ...) -> None: ...

class AlertEvent(_message.Message):
    __slots__ = ("node_id", "level", "source", "date", "text", "opaque")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    level: AlertLevel.Enum
    source: str
    date: str
    text: str
    opaque: str
    def __init__(self, node_id: _Optional[int] = ..., level: _Optional[_Union[AlertLevel.Enum, str]] = ..., source: _Optional[str] = ..., date: _Optional[str] = ..., text: _Optional[str] = ..., opaque: _Optional[str] = ...) -> None: ...

class AddNodeRequest(_message.Message):
    __slots__ = ("session_id", "node", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node: Node
    source: str
    def __init__(self, session_id: _Optional[int] = ..., node: _Optional[_Union[Node, _Mapping]] = ..., source: _Optional[str] = ...) -> None: ...

class AddNodeResponse(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class GetNodeRequest(_message.Message):
    __slots__ = ("session_id", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetNodeResponse(_message.Message):
    __slots__ = ("node", "ifaces", "links")
    NODE_FIELD_NUMBER: _ClassVar[int]
    IFACES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    node: Node
    ifaces: _containers.RepeatedCompositeFieldContainer[Interface]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    def __init__(self, node: _Optional[_Union[Node, _Mapping]] = ..., ifaces: _Optional[_Iterable[_Union[Interface, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ...) -> None: ...

class EditNodeRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "icon", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    icon: str
    source: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., icon: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class EditNodeResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class DeleteNodeRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    source: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...

class DeleteNodeResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class GetNodeTerminalRequest(_message.Message):
    __slots__ = ("session_id", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetNodeTerminalResponse(_message.Message):
    __slots__ = ("terminal",)
    TERMINAL_FIELD_NUMBER: _ClassVar[int]
    terminal: str
    def __init__(self, terminal: _Optional[str] = ...) -> None: ...

class MoveNodeRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "source", "position", "geo")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    source: str
    position: Position
    geo: Geo
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., source: _Optional[str] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., geo: _Optional[_Union[Geo, _Mapping]] = ...) -> None: ...

class MoveNodeResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class MoveNodesRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "source", "position", "geo")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    source: str
    position: Position
    geo: Geo
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., source: _Optional[str] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., geo: _Optional[_Union[Geo, _Mapping]] = ...) -> None: ...

class MoveNodesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NodeCommandRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "command", "wait", "shell")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    command: str
    wait: bool
    shell: bool
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., command: _Optional[str] = ..., wait: bool = ..., shell: bool = ...) -> None: ...

class NodeCommandResponse(_message.Message):
    __slots__ = ("output", "return_code")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    output: str
    return_code: int
    def __init__(self, output: _Optional[str] = ..., return_code: _Optional[int] = ...) -> None: ...

class AddLinkRequest(_message.Message):
    __slots__ = ("session_id", "link", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    link: Link
    source: str
    def __init__(self, session_id: _Optional[int] = ..., link: _Optional[_Union[Link, _Mapping]] = ..., source: _Optional[str] = ...) -> None: ...

class AddLinkResponse(_message.Message):
    __slots__ = ("result", "iface1", "iface2")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    IFACE1_FIELD_NUMBER: _ClassVar[int]
    IFACE2_FIELD_NUMBER: _ClassVar[int]
    result: bool
    iface1: Interface
    iface2: Interface
    def __init__(self, result: bool = ..., iface1: _Optional[_Union[Interface, _Mapping]] = ..., iface2: _Optional[_Union[Interface, _Mapping]] = ...) -> None: ...

class EditLinkRequest(_message.Message):
    __slots__ = ("session_id", "node1_id", "node2_id", "iface1_id", "iface2_id", "options", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node1_id: int
    node2_id: int
    iface1_id: int
    iface2_id: int
    options: LinkOptions
    source: str
    def __init__(self, session_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., iface1_id: _Optional[int] = ..., iface2_id: _Optional[int] = ..., options: _Optional[_Union[LinkOptions, _Mapping]] = ..., source: _Optional[str] = ...) -> None: ...

class EditLinkResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class DeleteLinkRequest(_message.Message):
    __slots__ = ("session_id", "node1_id", "node2_id", "iface1_id", "iface2_id", "source")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node1_id: int
    node2_id: int
    iface1_id: int
    iface2_id: int
    source: str
    def __init__(self, session_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., iface1_id: _Optional[int] = ..., iface2_id: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...

class DeleteLinkResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class SaveXmlRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class SaveXmlResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class OpenXmlRequest(_message.Message):
    __slots__ = ("data", "start", "file")
    DATA_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    data: str
    start: bool
    file: str
    def __init__(self, data: _Optional[str] = ..., start: bool = ..., file: _Optional[str] = ...) -> None: ...

class OpenXmlResponse(_message.Message):
    __slots__ = ("result", "session_id")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    result: bool
    session_id: int
    def __init__(self, result: bool = ..., session_id: _Optional[int] = ...) -> None: ...

class GetInterfacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInterfacesResponse(_message.Message):
    __slots__ = ("ifaces",)
    IFACES_FIELD_NUMBER: _ClassVar[int]
    ifaces: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ifaces: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteScriptRequest(_message.Message):
    __slots__ = ("script", "args")
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    script: str
    args: str
    def __init__(self, script: _Optional[str] = ..., args: _Optional[str] = ...) -> None: ...

class ExecuteScriptResponse(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class EventType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SESSION: _ClassVar[EventType.Enum]
        NODE: _ClassVar[EventType.Enum]
        LINK: _ClassVar[EventType.Enum]
        EXCEPTION: _ClassVar[EventType.Enum]
        FILE: _ClassVar[EventType.Enum]
    SESSION: EventType.Enum
    NODE: EventType.Enum
    LINK: EventType.Enum
    EXCEPTION: EventType.Enum
    FILE: EventType.Enum
    def __init__(self) -> None: ...

class MessageType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[MessageType.Enum]
        ADD: _ClassVar[MessageType.Enum]
        DELETE: _ClassVar[MessageType.Enum]
        CRI: _ClassVar[MessageType.Enum]
        LOCAL: _ClassVar[MessageType.Enum]
        STRING: _ClassVar[MessageType.Enum]
        TEXT: _ClassVar[MessageType.Enum]
        TTY: _ClassVar[MessageType.Enum]
    NONE: MessageType.Enum
    ADD: MessageType.Enum
    DELETE: MessageType.Enum
    CRI: MessageType.Enum
    LOCAL: MessageType.Enum
    STRING: MessageType.Enum
    TEXT: MessageType.Enum
    TTY: MessageType.Enum
    def __init__(self) -> None: ...

class LinkType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIRELESS: _ClassVar[LinkType.Enum]
        WIRED: _ClassVar[LinkType.Enum]
    WIRELESS: LinkType.Enum
    WIRED: LinkType.Enum
    def __init__(self) -> None: ...

class SessionState(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SessionState.Enum]
        DEFINITION: _ClassVar[SessionState.Enum]
        CONFIGURATION: _ClassVar[SessionState.Enum]
        INSTANTIATION: _ClassVar[SessionState.Enum]
        RUNTIME: _ClassVar[SessionState.Enum]
        DATACOLLECT: _ClassVar[SessionState.Enum]
        SHUTDOWN: _ClassVar[SessionState.Enum]
    NONE: SessionState.Enum
    DEFINITION: SessionState.Enum
    CONFIGURATION: SessionState.Enum
    INSTANTIATION: SessionState.Enum
    RUNTIME: SessionState.Enum
    DATACOLLECT: SessionState.Enum
    SHUTDOWN: SessionState.Enum
    def __init__(self) -> None: ...

class NodeType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[NodeType.Enum]
        PHYSICAL: _ClassVar[NodeType.Enum]
        SWITCH: _ClassVar[NodeType.Enum]
        HUB: _ClassVar[NodeType.Enum]
        WIRELESS_LAN: _ClassVar[NodeType.Enum]
        RJ45: _ClassVar[NodeType.Enum]
        TUNNEL: _ClassVar[NodeType.Enum]
        EMANE: _ClassVar[NodeType.Enum]
        TAP_BRIDGE: _ClassVar[NodeType.Enum]
        DOCKER: _ClassVar[NodeType.Enum]
        WIRELESS: _ClassVar[NodeType.Enum]
        PODMAN: _ClassVar[NodeType.Enum]
    DEFAULT: NodeType.Enum
    PHYSICAL: NodeType.Enum
    SWITCH: NodeType.Enum
    HUB: NodeType.Enum
    WIRELESS_LAN: NodeType.Enum
    RJ45: NodeType.Enum
    TUNNEL: NodeType.Enum
    EMANE: NodeType.Enum
    TAP_BRIDGE: NodeType.Enum
    DOCKER: NodeType.Enum
    WIRELESS: NodeType.Enum
    PODMAN: NodeType.Enum
    def __init__(self) -> None: ...

class ConfigOptionType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ConfigOptionType.Enum]
        UINT8: _ClassVar[ConfigOptionType.Enum]
        UINT16: _ClassVar[ConfigOptionType.Enum]
        UINT32: _ClassVar[ConfigOptionType.Enum]
        UINT64: _ClassVar[ConfigOptionType.Enum]
        INT8: _ClassVar[ConfigOptionType.Enum]
        INT16: _ClassVar[ConfigOptionType.Enum]
        INT32: _ClassVar[ConfigOptionType.Enum]
        INT64: _ClassVar[ConfigOptionType.Enum]
        FLOAT: _ClassVar[ConfigOptionType.Enum]
        STRING: _ClassVar[ConfigOptionType.Enum]
        BOOL: _ClassVar[ConfigOptionType.Enum]
    NONE: ConfigOptionType.Enum
    UINT8: ConfigOptionType.Enum
    UINT16: ConfigOptionType.Enum
    UINT32: ConfigOptionType.Enum
    UINT64: ConfigOptionType.Enum
    INT8: ConfigOptionType.Enum
    INT16: ConfigOptionType.Enum
    INT32: ConfigOptionType.Enum
    INT64: ConfigOptionType.Enum
    FLOAT: ConfigOptionType.Enum
    STRING: ConfigOptionType.Enum
    BOOL: ConfigOptionType.Enum
    def __init__(self) -> None: ...

class AlertLevel(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[AlertLevel.Enum]
        FATAL: _ClassVar[AlertLevel.Enum]
        ERROR: _ClassVar[AlertLevel.Enum]
        WARNING: _ClassVar[AlertLevel.Enum]
        NOTICE: _ClassVar[AlertLevel.Enum]
    DEFAULT: AlertLevel.Enum
    FATAL: AlertLevel.Enum
    ERROR: AlertLevel.Enum
    WARNING: AlertLevel.Enum
    NOTICE: AlertLevel.Enum
    def __init__(self) -> None: ...

class Hook(_message.Message):
    __slots__ = ("state", "file", "data")
    STATE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    state: SessionState.Enum
    file: str
    data: str
    def __init__(self, state: _Optional[_Union[SessionState.Enum, str]] = ..., file: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "state", "nodes", "links", "dir", "user", "default_services", "location", "hooks", "metadata", "file", "options", "servers")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SERVICES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: SessionState.Enum
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    dir: str
    user: str
    default_services: _containers.RepeatedCompositeFieldContainer[_services_pb2.ServiceDefaults]
    location: SessionLocation
    hooks: _containers.RepeatedCompositeFieldContainer[Hook]
    metadata: _containers.ScalarMap[str, str]
    file: str
    options: _containers.MessageMap[str, _common_pb2.ConfigOption]
    servers: _containers.RepeatedCompositeFieldContainer[Server]
    def __init__(self, id: _Optional[int] = ..., state: _Optional[_Union[SessionState.Enum, str]] = ..., nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ..., dir: _Optional[str] = ..., user: _Optional[str] = ..., default_services: _Optional[_Iterable[_Union[_services_pb2.ServiceDefaults, _Mapping]]] = ..., location: _Optional[_Union[SessionLocation, _Mapping]] = ..., hooks: _Optional[_Iterable[_Union[Hook, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., file: _Optional[str] = ..., options: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ..., servers: _Optional[_Iterable[_Union[Server, _Mapping]]] = ...) -> None: ...

class SessionSummary(_message.Message):
    __slots__ = ("id", "state", "nodes", "file", "dir")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: SessionState.Enum
    nodes: int
    file: str
    dir: str
    def __init__(self, id: _Optional[int] = ..., state: _Optional[_Union[SessionState.Enum, str]] = ..., nodes: _Optional[int] = ..., file: _Optional[str] = ..., dir: _Optional[str] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("id", "name", "type", "model", "position", "emane", "icon", "image", "server", "services", "geo", "dir", "channel", "canvas", "wlan_config", "mobility_config", "service_configs", "emane_configs", "wireless_config", "compose", "compose_name")
    class WlanConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    class MobilityConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    class ServiceConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _services_pb2.ServiceConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_services_pb2.ServiceConfig, _Mapping]] = ...) -> None: ...
    class WirelessConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    EMANE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    WLAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MOBILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    EMANE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPOSE_FIELD_NUMBER: _ClassVar[int]
    COMPOSE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: NodeType.Enum
    model: str
    position: Position
    emane: str
    icon: str
    image: str
    server: str
    services: _containers.RepeatedScalarFieldContainer[str]
    geo: Geo
    dir: str
    channel: str
    canvas: int
    wlan_config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    mobility_config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    service_configs: _containers.MessageMap[str, _services_pb2.ServiceConfig]
    emane_configs: _containers.RepeatedCompositeFieldContainer[_emane_pb2.NodeEmaneConfig]
    wireless_config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    compose: str
    compose_name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[NodeType.Enum, str]] = ..., model: _Optional[str] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., emane: _Optional[str] = ..., icon: _Optional[str] = ..., image: _Optional[str] = ..., server: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ..., geo: _Optional[_Union[Geo, _Mapping]] = ..., dir: _Optional[str] = ..., channel: _Optional[str] = ..., canvas: _Optional[int] = ..., wlan_config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ..., mobility_config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ..., service_configs: _Optional[_Mapping[str, _services_pb2.ServiceConfig]] = ..., emane_configs: _Optional[_Iterable[_Union[_emane_pb2.NodeEmaneConfig, _Mapping]]] = ..., wireless_config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ..., compose: _Optional[str] = ..., compose_name: _Optional[str] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("node1_id", "node2_id", "type", "iface1", "iface2", "options", "network_id", "label", "color")
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IFACE1_FIELD_NUMBER: _ClassVar[int]
    IFACE2_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    node1_id: int
    node2_id: int
    type: LinkType.Enum
    iface1: Interface
    iface2: Interface
    options: LinkOptions
    network_id: int
    label: str
    color: str
    def __init__(self, node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., type: _Optional[_Union[LinkType.Enum, str]] = ..., iface1: _Optional[_Union[Interface, _Mapping]] = ..., iface2: _Optional[_Union[Interface, _Mapping]] = ..., options: _Optional[_Union[LinkOptions, _Mapping]] = ..., network_id: _Optional[int] = ..., label: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class LinkOptions(_message.Message):
    __slots__ = ("jitter", "key", "mburst", "mer", "loss", "bandwidth", "burst", "delay", "dup", "unidirectional", "buffer")
    JITTER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MBURST_FIELD_NUMBER: _ClassVar[int]
    MER_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    BURST_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    DUP_FIELD_NUMBER: _ClassVar[int]
    UNIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    jitter: int
    key: int
    mburst: int
    mer: int
    loss: float
    bandwidth: int
    burst: int
    delay: int
    dup: int
    unidirectional: bool
    buffer: int
    def __init__(self, jitter: _Optional[int] = ..., key: _Optional[int] = ..., mburst: _Optional[int] = ..., mer: _Optional[int] = ..., loss: _Optional[float] = ..., bandwidth: _Optional[int] = ..., burst: _Optional[int] = ..., delay: _Optional[int] = ..., dup: _Optional[int] = ..., unidirectional: bool = ..., buffer: _Optional[int] = ...) -> None: ...

class Interface(_message.Message):
    __slots__ = ("id", "name", "mac", "ip4", "ip4_mask", "ip6", "ip6_mask", "net_id", "flow_id", "mtu", "node_id", "net2_id", "nem_id", "nem_port")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    IP4_FIELD_NUMBER: _ClassVar[int]
    IP4_MASK_FIELD_NUMBER: _ClassVar[int]
    IP6_FIELD_NUMBER: _ClassVar[int]
    IP6_MASK_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NET2_ID_FIELD_NUMBER: _ClassVar[int]
    NEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEM_PORT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    mac: str
    ip4: str
    ip4_mask: int
    ip6: str
    ip6_mask: int
    net_id: int
    flow_id: int
    mtu: int
    node_id: int
    net2_id: int
    nem_id: int
    nem_port: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., mac: _Optional[str] = ..., ip4: _Optional[str] = ..., ip4_mask: _Optional[int] = ..., ip6: _Optional[str] = ..., ip6_mask: _Optional[int] = ..., net_id: _Optional[int] = ..., flow_id: _Optional[int] = ..., mtu: _Optional[int] = ..., node_id: _Optional[int] = ..., net2_id: _Optional[int] = ..., nem_id: _Optional[int] = ..., nem_port: _Optional[int] = ...) -> None: ...

class SessionLocation(_message.Message):
    __slots__ = ("x", "y", "z", "lat", "lon", "alt", "scale")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    lat: float
    lon: float
    alt: float
    scale: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., lat: _Optional[float] = ..., lon: _Optional[float] = ..., alt: _Optional[float] = ..., scale: _Optional[float] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Geo(_message.Message):
    __slots__ = ("lat", "lon", "alt")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    alt: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ..., alt: _Optional[float] = ...) -> None: ...

class Server(_message.Message):
    __slots__ = ("name", "host")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    name: str
    host: str
    def __init__(self, name: _Optional[str] = ..., host: _Optional[str] = ...) -> None: ...

class LinkedRequest(_message.Message):
    __slots__ = ("session_id", "node1_id", "node2_id", "iface1_id", "iface2_id", "linked")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node1_id: int
    node2_id: int
    iface1_id: int
    iface2_id: int
    linked: bool
    def __init__(self, session_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., iface1_id: _Optional[int] = ..., iface2_id: _Optional[int] = ..., linked: bool = ...) -> None: ...

class LinkedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WirelessLinkedRequest(_message.Message):
    __slots__ = ("session_id", "wireless_id", "node1_id", "node2_id", "linked")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    wireless_id: int
    node1_id: int
    node2_id: int
    linked: bool
    def __init__(self, session_id: _Optional[int] = ..., wireless_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., linked: bool = ...) -> None: ...

class WirelessLinkedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WirelessConfigRequest(_message.Message):
    __slots__ = ("session_id", "wireless_id", "node1_id", "node2_id", "options1", "options2")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS1_FIELD_NUMBER: _ClassVar[int]
    OPTIONS2_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    wireless_id: int
    node1_id: int
    node2_id: int
    options1: LinkOptions
    options2: LinkOptions
    def __init__(self, session_id: _Optional[int] = ..., wireless_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., options1: _Optional[_Union[LinkOptions, _Mapping]] = ..., options2: _Optional[_Union[LinkOptions, _Mapping]] = ...) -> None: ...

class WirelessConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWirelessConfigRequest(_message.Message):
    __slots__ = ("session_id", "node_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetWirelessConfigResponse(_message.Message):
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
