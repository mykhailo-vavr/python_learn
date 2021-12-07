from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class PaginationHotels(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_query_param = "offset"
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response(
            OrderedDict([
                ('hotels', data),
                ('count', self.page.paginator.count),
            ]))