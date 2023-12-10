"""
When: I am on the homepage as visitor (not logged in)
Then: I should should see the peeps
"""
def test_get_peeps_as_visitor(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"