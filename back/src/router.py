from flask import Flask, request
from .views import (
    SolverViewSet,
    SolverTypeViewSet,
    TestViewSet,
    TestRunViewSet
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    """  """
    return "Welcome!"


@app.route('/solver_type', methods=['GET'])
def solver_type_list():
    """  """
    view_set = SolverTypeViewSet(request)
    page = request.args.get('page', 0)
    return view_set.list(page=page)

@app.route('/solver_type', methods=['POST'])
def solver_type_create():
    """  """
    view_set = SolverTypeViewSet(request)
    return view_set.create()

@app.route('/solver_type/<int:id>', methods=['GET'])
def solver_type_retrieve(id):
    """  """
    view_set = SolverTypeViewSet(request)
    return view_set.retrieve(id)

@app.route('/solver_type/<int:id>', methods=['POST'])
def solver_type_update(id):
    """  """
    view_set = SolverTypeViewSet(request)
    return view_set.update(id)


@app.route('/solver', methods=['GET'])
def solver_list():
    """  """
    view_set = SolverViewSet(request)
    page = request.args.get('page', 0)
    return view_set.list(page=page)

@app.route('/solver', methods=['POST'])
def solver_create():
    """  """
    view_set = SolverViewSet(request)
    return view_set.create()

@app.route('/solver/<int:id>', methods=['GET'])
def solver_retrieve(id):
    """  """
    view_set = SolverViewSet(request)
    return view_set.retrieve(id=id)

@app.route('/solver/<int:id>', methods=['POST'])
def solver_update(id):
    """  """
    view_set = SolverViewSet(request)
    return view_set.update(id=id)


@app.route('/test', methods=['GET'])
def test_list():
    """  """
    view_set = TestViewSet(request)
    page = request.args.get('page', 0)
    return view_set.list(page=page)

@app.route('/test', methods=['POST'])
def test_create():
    """  """
    view_set = TestViewSet(request)
    return view_set.create()

@app.route('/test/<int:id>', methods=['GET'])
def test_retrieve(id):
    """  """
    view_set = TestViewSet(request)
    return view_set.retrieve(id)

@app.route('/test/<int:id>', methods=['POST'])
def test_update(id):
    """  """
    view_set = TestViewSet(request)
    return view_set.update(id)