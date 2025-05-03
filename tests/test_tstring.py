def test_tstring():
    result = t"Hello World"
    assert result.strings == ("Hello World",)
