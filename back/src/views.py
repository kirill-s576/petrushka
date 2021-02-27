from abc import ABC, abstractmethod
from .lib.response import JsonResponse
from config import OBJECTS_PER_PAGE
from flask import request


class BaseViewSet(ABC):

    def __init__(self, request: request):
        self.request = request

    PAGE_SIZE = OBJECTS_PER_PAGE

    @abstractmethod
    def list(self, page:int=0) -> JsonResponse:
        pass

    @abstractmethod
    def retrieve(self, id:int) -> JsonResponse:
        pass

    @abstractmethod
    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    @abstractmethod
    def create(self) -> JsonResponse:
        pass

    @abstractmethod
    def delete(self, id:int) -> JsonResponse:
        pass


class SolverTypeViewSet(BaseViewSet):

    def list(self, page:int=0):
        return JsonResponse({"qqq": "qqq"})

    def retrieve(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def create(self) -> JsonResponse:
        return JsonResponse({})

    def delete(self, id:int) -> JsonResponse:
        return JsonResponse({})


class SolverViewSet(BaseViewSet):

    def list(self, page: int = 0):
        return JsonResponse({})

    def retrieve(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def create(self) -> JsonResponse:
        return JsonResponse({})

    def delete(self, id:int) -> JsonResponse:
        return JsonResponse({})


class TestViewSet(BaseViewSet):

    def list(self, page: int = 0):
        return JsonResponse({})

    def retrieve(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def create(self) -> JsonResponse:
        return JsonResponse({})

    def delete(self, id:int) -> JsonResponse:
        return JsonResponse({})


class TestRunViewSet(BaseViewSet):

    def list(self, page: int = 0):
        return JsonResponse({})

    def retrieve(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def create(self) -> JsonResponse:
        return JsonResponse({})

    def delete(self, id:int) -> JsonResponse:
        return JsonResponse({})