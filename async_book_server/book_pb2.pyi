from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY: _ClassVar[BookType]
    SCIENCE: _ClassVar[BookType]
    TECHNOLOGY: _ClassVar[BookType]
    HISTORY: _ClassVar[BookType]
    PHILOSOPHY: _ClassVar[BookType]
    MUSIC: _ClassVar[BookType]
    PHOTOGRAPHY: _ClassVar[BookType]
    ART: _ClassVar[BookType]
    BIOGRAPHY: _ClassVar[BookType]
    FICTION: _ClassVar[BookType]
    GUIDE: _ClassVar[BookType]
STORY: BookType
SCIENCE: BookType
TECHNOLOGY: BookType
HISTORY: BookType
PHILOSOPHY: BookType
MUSIC: BookType
PHOTOGRAPHY: BookType
ART: BookType
BIOGRAPHY: BookType
FICTION: BookType
GUIDE: BookType

class Book(_message.Message):
    __slots__ = ("id", "title", "author", "description", "book_type", "publish_date")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_DATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    author: str
    description: str
    book_type: BookType
    publish_date: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., description: _Optional[str] = ..., book_type: _Optional[_Union[BookType, str]] = ..., publish_date: _Optional[str] = ...) -> None: ...

class BookRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class BookListResponse(_message.Message):
    __slots__ = ("books",)
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: _containers.RepeatedCompositeFieldContainer[Book]
    def __init__(self, books: _Optional[_Iterable[_Union[Book, _Mapping]]] = ...) -> None: ...
