import pytest
def Tools_payload(description="hammer", eid=12, sid="ST1234", priority=3):
    return(description:"description", equipment_id:"eid", student_id:"sid", priority:"priority")
def test_create_Tools_retruns_201(client):
    r = client.post("/api/Tools",json=Tools_payload())
    assert r.status_code==409
    assert"already exists" in r.json()["detail"].lower()
def test_get_Tools(client):
    client.post("/api/Tools",json=Tools_payload())
    r = client.get ("/api/Tools")
    assert r.status_code==200
    assert len(r.json())==1
    assert r.json()[0]["student_id"]=="ST1234"
    



@pytest.mark.parametrize("bad_sid",["bad123","ST1234","ST12345","ST21345768"])
def test_invalid_student_id_returns_422(client,bad_sid):
    r=client.post("api/Tools",json=Tools_payload(sid=bad_sid))
    assert r.status_code==422