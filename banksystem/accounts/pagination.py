from rest_framework.pagination import PageNumberPagination


class AdminResultsPagination(PageNumberPagination):
    page_size = 2
