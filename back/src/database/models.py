import peewee
from config import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD
)


pg_database = peewee.PostgresqlDatabase(
    DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

class SolverType(peewee.Model):
    """

    """
    name = peewee.CharField()

    class Meta:
        database = pg_database


class Solver(peewee.Model):
    """

    """
    solver_type = peewee.ForeignKeyField(SolverType, backref='solvers')
    name = peewee.CharField()
    created_at = peewee.DateTimeField()

    class Meta:
        database = pg_database


class Test(peewee.Model):
    """

    """
    solver_type = peewee.ForeignKeyField(SolverType, backref='tests')
    name = peewee.CharField()

    class Meta:
        database = pg_database


class TestRun(peewee.Model):
    """

    """
    solver = peewee.ForeignKeyField(Solver, backref='test_runs')
    test = peewee.ForeignKeyField(Test, backref='test_runs')
    started_at = peewee.DateTimeField()
    finished = peewee.BooleanField()
    result = peewee.BooleanField()
    log = peewee.TextField()

    class Meta:
        database = pg_database


def create_all_tables():
    pg_database.connect()
    pg_database.create_tables(
        [
            SolverType,
            Solver,
            Test,
            TestRun
        ]
    )
    pg_database.close()