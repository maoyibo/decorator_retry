import logging
import pytest
from decorator_retry import retry


@retry(ValueError, KeyError, 
       retry=True, 
       attempts=3, 
       wait=1.5, 
       reraise=True, 
       logger=logging.warning)
def foo():
    raise ValueError("Raise Test")

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        foo()
    assert str(exc_info.value) == "Raise Test"