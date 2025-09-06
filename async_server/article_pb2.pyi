from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Article(_message.Message):
    __slots__ = ("id", "title", "content", "create_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    content: str
    create_time: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., create_time: _Optional[str] = ...) -> None: ...

class ArticleRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ArticleListResponse(_message.Message):
    __slots__ = ("articles",)
    ARTICLES_FIELD_NUMBER: _ClassVar[int]
    articles: _containers.RepeatedCompositeFieldContainer[Article]
    def __init__(self, articles: _Optional[_Iterable[_Union[Article, _Mapping]]] = ...) -> None: ...

class ArticleDetailRequest(_message.Message):
    __slots__ = ("pk",)
    PK_FIELD_NUMBER: _ClassVar[int]
    pk: int
    def __init__(self, pk: _Optional[int] = ...) -> None: ...
