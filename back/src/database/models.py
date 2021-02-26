from .objects import AbstractDatabaseModel
from pydantic import Field
import datetime


class SolverType(AbstractDatabaseModel):
    """

    """
    name: str = Field()


class Solver(AbstractDatabaseModel):
    """

    """
    solver_type: SolverType
    name: str
    created_at: datetime.datetime


class Test(AbstractDatabaseModel):
    """

    """
    solver_type: SolverType
    name: str


class TestRun(AbstractDatabaseModel):
    """

    """
    solver: Solver
    test: Test
    started_at: datetime.datetime
    finished: bool
    result: bool
    log: str
