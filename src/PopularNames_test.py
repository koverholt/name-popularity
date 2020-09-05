from . import PopularNames

def test_PopularNames():
    assert PopularNames.apply("Jane") == "hello Jane"
