from flask import Response
import json


class JsonResponse(Response):

    def __init__(self, data, **kwargs):
        super().__init__(json.dumps(data), content_type="application/json", **kwargs)