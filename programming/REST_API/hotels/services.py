from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import permissions
from .types import *


class ReadOnlyOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'admin'


class PaginationHotels(PageNumberPagination):
    page_size = PAGE_SIZE
    max_page_size = MAX_PAGE_SIZE
    page_query_param = "offset"
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response(
            OrderedDict([
                ('hotels', data),
                ('count', self.page.paginator.count),
            ]))