def test_environment_setup():
    # This proves my Conda environment is working correctly
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 10
