from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.api
def test_api_get_users():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(
            "https://jsonplaceholder.typicode.com/posts"
        )

        assert response.status == 200

        body = response.json()

        assert body[0]["id"] == 1