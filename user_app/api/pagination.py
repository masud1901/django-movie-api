from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
    last_page_strings = "last"


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2


class WatchListPaginationCursor(CursorPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
    last_page_strings = "last"
    ordering = "created"
