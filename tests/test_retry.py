import logging
import pytest
from decorator_retry import retry


def test_retry_reraise_expect():
    @retry(ValueError, KeyError,
           retry=True,
           attempts=3,
           wait=1.5,
           reraise=True,
           logger=logging.warning)
    def retry_reraise_expect():
        raise ValueError("Raise ValueError")
    with pytest.raises(ValueError) as exc_info:
        retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"


def test_retry_reraise_unexpect():
    @retry(ValueError, KeyError,
           retry=True,
           attempts=3,
           wait=1.5,
           reraise=True,
           logger=logging.warning)
    def retry_reraise_unexpect():
        raise IOError("Raise Test")
    with pytest.raises(IOError) as exc_info:
        retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"


def test_no_retry_reraise_expect():
    @retry(ValueError, KeyError,
           retry=False,
           attempts=3,
           wait=1.5,
           reraise=True,
           logger=logging.warning)
    def no_retry_reraise_expect():
        raise ValueError("Raise ValueError")
    with pytest.raises(ValueError) as exc_info:
        no_retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"


def test_no_retry_reraise_unexpect():
    @retry(ValueError, KeyError,
           retry=False,
           attempts=3,
           wait=1.5,
           reraise=True,
           logger=logging.warning)
    def no_retry_reraise_unexpect():
        raise IOError("Raise Test")
    with pytest.raises(IOError) as exc_info:
        no_retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"


def test_retry_no_reraise_expect():
    @retry(ValueError, KeyError,
           retry=True,
           attempts=3,
           wait=1.5,
           reraise=False,
           logger=logging.warning)
    def retry_no_reraise_expect():
        raise ValueError("Raise ValueError")
    assert retry_no_reraise_expect() == None


def test_retry_no_reraise_unexpect():
    @retry(ValueError, KeyError,
           retry=True,
           attempts=3,
           wait=1.5,
           reraise=False,
           logger=logging.warning)
    def retry_no_reraise_unexpect():
        raise IOError("Raise Test")
    assert retry_no_reraise_unexpect() == None


def test_no_retry_no_reraise_expect():
    @retry(ValueError, KeyError,
           retry=False,
           attempts=3,
           wait=1.5,
           reraise=False,
           logger=logging.warning)
    def no_retry_no_reraise_expect():
        raise ValueError("Raise ValueError")
    assert no_retry_no_reraise_expect() == None


def test_no_retry_no_reraise_unexpect():
    @retry(ValueError, KeyError,
           retry=False,
           attempts=3,
           wait=1.5,
           reraise=False,
           logger=logging.warning)
    def no_retry_no_reraise_unexpect():
        raise IOError("Raise Test")
    assert no_retry_no_reraise_unexpect() == None


def test_object_method():
    class ObjedtMethod():
        @retry(ValueError, reraise=True, wait=0.5, logger=logging.warning)
        def raise_error(self):
            raise ValueError("Raise Test")
    obj = ObjedtMethod()
    with pytest.raises(ValueError) as exc_info:
        obj.raise_error()
    assert str(exc_info.value) == "Raise Test"
