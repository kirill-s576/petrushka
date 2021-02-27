from pydantic import BaseModel
import datetime


class SolverTypeSerializer(BaseModel):
    id: int = None
    name: str = None

class SolverTypeCreateSerializer(BaseModel):
    name: str

class SolverTypeUpdateSerializer(BaseModel):
    name: str = None


class SolverSerializer(BaseModel):
    id: int = None
    solver_type: int = None
    name: str = None
    created_at: datetime.datetime = None

class SolverCreateSerializer(BaseModel):
    solver_type_id: int
    name: str
    created_at: datetime.datetime = datetime.datetime.now()

class SolverUpdateSerializer(BaseModel):
    solver_type_id: int = None
    name: str = None


class TestSerializer(BaseModel):
    id: int = None
    solver_type: int = None
    name: str = None

class TestCreateSerializer(BaseModel):
    solver_type_id: int
    name: str

class TestUpdateSerializer(BaseModel):
    solver_type_id: int = None
    name: str = None


class TestRunSerializer(BaseModel):
    id: int = None
    solver: int = None
    test: int = None
    started_at: datetime.datetime = None
    finished: bool = None
    result: bool = None
    log: str = None

class TestRunCreateSerializer(BaseModel):
    solver_id: int
    test_id: int
    started_at: datetime.datetime = datetime.datetime.now()
    finished: bool = False
    result: bool = False
    log: str = ""