from abc import ABC, abstractmethod
from .lib.response import JsonResponse
from config import OBJECTS_PER_PAGE
from flask import request
from .serializers import (
    SolverSerializer,
    SolverCreateSerializer,
    SolverUpdateSerializer,
    SolverTypeSerializer,
    SolverTypeCreateSerializer,
    SolverTypeUpdateSerializer,
    TestSerializer,
    TestCreateSerializer,
    TestUpdateSerializer,
    TestRunSerializer,
    TestRunCreateSerializer
)
from .database.models import (
    pg_database,
    Solver,
    SolverType,
    Test,
    TestRun
)
import json


class BaseViewSet(ABC):

    def __init__(self, request: request):
        self.request = request
        self.request_data = json.loads(request.data.decode("utf-8"))

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
        models = SolverType.select().offset(page*self.PAGE_SIZE).limit(page*self.PAGE_SIZE+self.PAGE_SIZE)
        total_count = SolverType.select().count()
        output_list = []
        for model in models:
            serializer = SolverTypeSerializer(**model.__data__)
            output_list.append(serializer.dict())
        return JsonResponse({
            "total": total_count,
            "page": page,
            "objects": output_list
        })

    def retrieve(self, id:int) -> JsonResponse:
        model = SolverType.get(id=id)
        serializer = SolverTypeSerializer(**model.__data__)
        return JsonResponse(serializer.dict())

    def update(self, id:int) -> JsonResponse:
        model = SolverType.get(id=id)
        serializer = SolverTypeUpdateSerializer(**self.request_data)
        for key, value in serializer.dict().items():
            setattr(model, key, value)
        model.save()
        updated_model_serializer = SolverTypeSerializer(**model.__data__)
        return JsonResponse(updated_model_serializer.dict())

    def create(self) -> JsonResponse:
        serializer = SolverTypeCreateSerializer(**self.request_data)
        model = SolverType.create(**serializer.dict())
        created_model_serializer = SolverTypeSerializer(**model.__data__)
        return JsonResponse(created_model_serializer.dict())

    def delete(self, id:int) -> JsonResponse:
        return JsonResponse({})


class SolverViewSet(BaseViewSet):

    def list(self, page: int = 0):
        return JsonResponse({})

    def retrieve(self, id:int) -> JsonResponse:
        model = Solver.get(id=id)
        serializer = SolverSerializer(**model.__data__)
        serializer.created_at = serializer.created_at.strftime("%d-%m-%Y %H:%M:%S")
        return JsonResponse(serializer.dict())

    def update(self, id:int) -> JsonResponse:
        return JsonResponse({})

    def create(self) -> JsonResponse:
        serializer = SolverCreateSerializer(**self.request_data)
        model = Solver.create(**serializer.dict())
        created_model_serializer = SolverSerializer(**model.__data__)
        created_model_serializer.created_at = created_model_serializer.created_at.strftime("%d-%m-%Y %H:%M:%S")
        return JsonResponse(created_model_serializer.dict())

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