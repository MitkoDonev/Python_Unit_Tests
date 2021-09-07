from student import StudentDB
import pytest


@pytest.fixture(scope="module")
def db():
    print("----Setup----")
    db = StudentDB()
    db.connect("data.json")
    yield db

    print("----Tear Down----")
    db.close()


def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1
    assert scott_data["name"] == "Scott"
    assert scott_data["result"] == "pass"


def test_steve_data(db):
    steve_data = db.get_data("Steve")
    assert steve_data["id"] != 1
    assert steve_data["name"] == "Steve"
    assert steve_data["result"] == "fail"
