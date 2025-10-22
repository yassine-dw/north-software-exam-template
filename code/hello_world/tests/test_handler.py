import pytest

from hello_world.handler import lambda_handler

def test_lambda_handler_returns_hello_world():
    event = {}
    context = None
    response = lambda_handler(event, context)
    assert isinstance(response, dict)
    assert response.get("statusCode") == 200
    assert response.get("body") == "Hello, World!"

