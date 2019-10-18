import pytest

@pytest.mark.windows
def test_windows_1():
    assert True
@pytest.mark.windows
def test_windows_2():
    assert True
@pytest.mark.mac
def test_mac_1():
    assert True
@pytest.mark.mac
def test_mac_2():
    assert True

    import sys
    #     # @pytest.mark.skip
    #     # @pytest.mark.skip(reason="not included in the build")
    #     # def test_demo_1():
    #     #     assert  True
    #     # @pytest.mark.skipif(sys.version_info >(3,6), reason= "requires python 3.6 or higher")
    #     # def test_demo_2():
    #     #     assert True
    #     # def test_demo_3():
    #     #     assert True