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
    name = peewee.CharField(max_length=1024)

    class Meta:
        database = pg_database


class Solver(peewee.Model):
    """

    """
    solver_type = peewee.ForeignKeyField(SolverType, backref='solvers')
    name = peewee.CharField(max_length=1024)
    created_at = peewee.DateTimeField()

    class Meta:
        database = pg_database


class Test(peewee.Model):
    """

    """
    solver_type = peewee.ForeignKeyField(SolverType, backref='tests')
    name = peewee.CharField(max_length=1024)

    class Meta:
        database = pg_database

fmt = '%d-%m-%Y %H:%M:%S'

class TestRun(peewee.Model):
    """

    """
    solver = peewee.ForeignKeyField(Solver, backref='test_runs')
    test = peewee.ForeignKeyField(Test, backref='test_runs')
    started_at = peewee.DateTimeField(formats=[fmt])
    finished_at = peewee.DateTimeField(formats=[fmt], null=True)
    finished = peewee.BooleanField(default=False)
    result = peewee.BooleanField(default=False)
    log = peewee.TextField(null=True)

    class Meta:
        database = pg_database

    @property
    def total_seconds(self):
        if self.finished_at:
            delta = (self.finished_at - self.started_at).total_seconds()
            return delta
        else:
            return 0

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