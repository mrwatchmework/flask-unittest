
def test_db_load(client):
    rv = client.get('/items')
    assert rv.status_code == 200
