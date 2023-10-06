import logging
import pytest
from decorator_retry import retry


@retry(ValueError,KeyError,
       retry=True, 
       attempts=3, 
       wait=1.5, 
       reraise=True, 
       logger=logging.warning)
def retry_reraise_expect():
    raise ValueError("Raise ValueError")

def test_retry_reraise_expect():
    with pytest.raises(ValueError) as exc_info:
        retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"

@retry(ValueError,KeyError,
       retry=True, 
       attempts=3, 
       wait=1.5, 
       reraise=True, 
       logger=logging.warning)
def retry_reraise_unexpect():
    raise IOError("Raise Test")

def test_retry_reraise_unexpect():
    with pytest.raises(IOError) as exc_info:
        retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"

@retry(ValueError,KeyError,
       retry=False, 
       attempts=3, 
       wait=1.5, 
       reraise=True, 
       logger=logging.warning)
def no_retry_reraise_expect():
    raise ValueError("Raise ValueError")

def test_no_retry_reraise_expect():
    with pytest.raises(ValueError) as exc_info:
        no_retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"

@retry(ValueError,KeyError,
       retry=False, 
       attempts=3, 
       wait=1.5, 
       reraise=True, 
       logger=logging.warning)
def no_retry_reraise_unexpect():
    raise IOError("Raise Test")

def test_no_retry_reraise_unexpect():
    with pytest.raises(IOError) as exc_info:
        no_retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"

@retry(ValueError,KeyError,
       retry=True, 
       attempts=3, 
       wait=1.5, 
       reraise=False, 
       logger=logging.warning)
def retry_no_reraise_expect():
    raise ValueError("Raise ValueError")

def test_retry_no_reraise_expect():
    assert retry_no_reraise_expect()==None

@retry(ValueError,KeyError,
       retry=True, 
       attempts=3, 
       wait=1.5, 
       reraise=False, 
       logger=logging.warning)
def retry_no_reraise_unexpect():
    raise IOError("Raise Test")

def test_retry_no_reraise_unexpect():
    assert retry_no_reraise_unexpect() ==None


@retry(ValueError,KeyError,
       retry=False, 
       attempts=3, 
       wait=1.5, 
       reraise=False, 
       logger=logging.warning)
def no_retry_no_reraise_expect():
    raise ValueError("Raise ValueError")

def test_no_retry_no_reraise_expect():
    assert no_retry_no_reraise_expect()==None

@retry(ValueError,KeyError,
       retry=False, 
       attempts=3, 
       wait=1.5, 
       reraise=False, 
       logger=logging.warning)
def no_retry_no_reraise_unexpect():
    raise IOError("Raise Test")

def test_no_retry_no_reraise_unexpect():
    assert no_retry_no_reraise_unexpect() ==None