import pytest

from myapp.models import Contact


@pytest.mark.django_db
def test_contact_list_view(client):
    url = '/'
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['object_list']
