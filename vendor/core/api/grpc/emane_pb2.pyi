from core.api.grpc import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEmaneModelConfigRequest(_message.Message):
    __slots__ = ("session_id", "node_id", "iface_id", "model")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node_id: int
    iface_id: int
    model: str
    def __init__(self, session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., model: _Optional[str] = ...) -> None: ...

class GetEmaneModelConfigResponse(_message.Message):
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

class SetEmaneModelConfigRequest(_message.Message):
    __slots__ = ("session_id", "emane_model_config")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EMANE_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    emane_model_config: EmaneModelConfig
    def __init__(self, session_id: _Optional[int] = ..., emane_model_config: _Optional[_Union[EmaneModelConfig, _Mapping]] = ...) -> None: ...

class SetEmaneModelConfigResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class GetEmaneModelConfig(_message.Message):
    __slots__ = ("node_id", "model", "iface_id", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    model: str
    iface_id: int
    config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    def __init__(self, node_id: _Optional[int] = ..., model: _Optional[str] = ..., iface_id: _Optional[int] = ..., config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ...) -> None: ...

class NodeEmaneConfig(_message.Message):
    __slots__ = ("iface_id", "model", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ConfigOption
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ConfigOption, _Mapping]] = ...) -> None: ...
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    iface_id: int
    model: str
    config: _containers.MessageMap[str, _common_pb2.ConfigOption]
    def __init__(self, iface_id: _Optional[int] = ..., model: _Optional[str] = ..., config: _Optional[_Mapping[str, _common_pb2.ConfigOption]] = ...) -> None: ...

class GetEmaneEventChannelRequest(_message.Message):
    __slots__ = ("session_id", "nem_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NEM_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    nem_id: int
    def __init__(self, session_id: _Optional[int] = ..., nem_id: _Optional[int] = ...) -> None: ...

class GetEmaneEventChannelResponse(_message.Message):
    __slots__ = ("group", "port", "device")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    group: str
    port: int
    device: str
    def __init__(self, group: _Optional[str] = ..., port: _Optional[int] = ..., device: _Optional[str] = ...) -> None: ...

class EmaneLinkRequest(_message.Message):
    __slots__ = ("session_id", "nem1", "nem2", "linked")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NEM1_FIELD_NUMBER: _ClassVar[int]
    NEM2_FIELD_NUMBER: _ClassVar[int]
    LINKED_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    nem1: int
    nem2: int
    linked: bool
    def __init__(self, session_id: _Optional[int] = ..., nem1: _Optional[int] = ..., nem2: _Optional[int] = ..., linked: bool = ...) -> None: ...

class EmaneLinkResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class EmaneModelConfig(_message.Message):
    __slots__ = ("node_id", "iface_id", "model", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    iface_id: int
    model: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., model: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EmanePathlossesRequest(_message.Message):
    __slots__ = ("session_id", "node1_id", "rx1", "iface1_id", "node2_id", "rx2", "iface2_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    RX1_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    RX2_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    node1_id: int
    rx1: float
    iface1_id: int
    node2_id: int
    rx2: float
    iface2_id: int
    def __init__(self, session_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., rx1: _Optional[float] = ..., iface1_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., rx2: _Optional[float] = ..., iface2_id: _Optional[int] = ...) -> None: ...

class EmanePathlossesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocationEvent(_message.Message):
    __slots__ = ("nem_id", "node_id", "iface_id", "lon", "lat", "alt", "azimuth", "elevation", "magnitude", "roll", "pitch", "yaw")
    NEM_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    nem_id: int
    node_id: int
    iface_id: int
    lon: float
    lat: float
    alt: float
    azimuth: float
    elevation: float
    magnitude: float
    roll: float
    pitch: float
    yaw: float
    def __init__(self, nem_id: _Optional[int] = ..., node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., lon: _Optional[float] = ..., lat: _Optional[float] = ..., alt: _Optional[float] = ..., azimuth: _Optional[float] = ..., elevation: _Optional[float] = ..., magnitude: _Optional[float] = ..., roll: _Optional[float] = ..., pitch: _Optional[float] = ..., yaw: _Optional[float] = ...) -> None: ...

class CommEffectEvent(_message.Message):
    __slots__ = ("nem1_id", "node1_id", "iface1_id", "nem2_id", "node2_id", "iface2_id", "delay", "jitter", "loss", "dup", "unicast", "broadcast")
    NEM1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    NEM2_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    JITTER_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    DUP_FIELD_NUMBER: _ClassVar[int]
    UNICAST_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    nem1_id: int
    node1_id: int
    iface1_id: int
    nem2_id: int
    node2_id: int
    iface2_id: int
    delay: int
    jitter: int
    loss: float
    dup: int
    unicast: int
    broadcast: int
    def __init__(self, nem1_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., iface1_id: _Optional[int] = ..., nem2_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., iface2_id: _Optional[int] = ..., delay: _Optional[int] = ..., jitter: _Optional[int] = ..., loss: _Optional[float] = ..., dup: _Optional[int] = ..., unicast: _Optional[int] = ..., broadcast: _Optional[int] = ...) -> None: ...

class PathlossEvent(_message.Message):
    __slots__ = ("nem1_id", "node1_id", "iface1_id", "nem2_id", "node2_id", "iface2_id", "forward1", "reverse1", "forward2", "reverse2")
    NEM1_ID_FIELD_NUMBER: _ClassVar[int]
    NODE1_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE1_ID_FIELD_NUMBER: _ClassVar[int]
    NEM2_ID_FIELD_NUMBER: _ClassVar[int]
    NODE2_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE2_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARD1_FIELD_NUMBER: _ClassVar[int]
    REVERSE1_FIELD_NUMBER: _ClassVar[int]
    FORWARD2_FIELD_NUMBER: _ClassVar[int]
    REVERSE2_FIELD_NUMBER: _ClassVar[int]
    nem1_id: int
    node1_id: int
    iface1_id: int
    nem2_id: int
    node2_id: int
    iface2_id: int
    forward1: float
    reverse1: float
    forward2: float
    reverse2: float
    def __init__(self, nem1_id: _Optional[int] = ..., node1_id: _Optional[int] = ..., iface1_id: _Optional[int] = ..., nem2_id: _Optional[int] = ..., node2_id: _Optional[int] = ..., iface2_id: _Optional[int] = ..., forward1: _Optional[float] = ..., reverse1: _Optional[float] = ..., forward2: _Optional[float] = ..., reverse2: _Optional[float] = ...) -> None: ...

class AntennaProfileEvent(_message.Message):
    __slots__ = ("nem_id", "node_id", "iface_id", "profile", "azimuth", "elevation")
    NEM_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    nem_id: int
    node_id: int
    iface_id: int
    profile: int
    azimuth: float
    elevation: float
    def __init__(self, nem_id: _Optional[int] = ..., node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., profile: _Optional[int] = ..., azimuth: _Optional[float] = ..., elevation: _Optional[float] = ...) -> None: ...

class FadingSelectionEvent(_message.Message):
    __slots__ = ("nem_id", "node_id", "iface_id", "model")
    NEM_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IFACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    nem_id: int
    node_id: int
    iface_id: int
    model: str
    def __init__(self, nem_id: _Optional[int] = ..., node_id: _Optional[int] = ..., iface_id: _Optional[int] = ..., model: _Optional[str] = ...) -> None: ...

class EmaneEventsRequest(_message.Message):
    __slots__ = ("session_id", "location", "comm_effect", "pathloss", "antenna", "fading")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMM_EFFECT_FIELD_NUMBER: _ClassVar[int]
    PATHLOSS_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_FIELD_NUMBER: _ClassVar[int]
    FADING_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    location: LocationEvent
    comm_effect: CommEffectEvent
    pathloss: PathlossEvent
    antenna: AntennaProfileEvent
    fading: FadingSelectionEvent
    def __init__(self, session_id: _Optional[int] = ..., location: _Optional[_Union[LocationEvent, _Mapping]] = ..., comm_effect: _Optional[_Union[CommEffectEvent, _Mapping]] = ..., pathloss: _Optional[_Union[PathlossEvent, _Mapping]] = ..., antenna: _Optional[_Union[AntennaProfileEvent, _Mapping]] = ..., fading: _Optional[_Union[FadingSelectionEvent, _Mapping]] = ...) -> None: ...

class EmaneEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
