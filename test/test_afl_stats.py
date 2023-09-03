import pytest
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
    with testbook('../afl_stats.ipynb', execute=True) as tb:
        yield tb

# Test using function call.
def test_int(tb):
    int_ref = tb.ref("int_ref")
    assert int_ref == 1