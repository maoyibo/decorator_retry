import logging
import pytest
from decorator_retry import async_retry
pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_retry_reraise_expect():
    @async_retry(ValueError, KeyError,
                 retry=True,
                 attempts=3,
                 wait=1.5,
                 reraise=True,
                 logger=logging.warning)
    async def retry_reraise_expect():
        raise ValueError("Raise ValueError")
    with pytest.raises(ValueError) as exc_info:
        await retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"


@pytest.mark.asyncio
async def test_retry_reraise_unexpect():
    @async_retry(ValueError, KeyError,
                 retry=True,
                 attempts=3,
                 wait=1.5,
                 reraise=True,
                 logger=logging.warning)
    async def retry_reraise_unexpect():
        raise IOError("Raise Test")
    with pytest.raises(IOError) as exc_info:
        await retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"


@pytest.mark.asyncio
async def test_no_retry_reraise_expect():
    @async_retry(ValueError, KeyError,
                 retry=False,
                 attempts=3,
                 wait=1.5,
                 reraise=True,
                 logger=logging.warning)
    async def no_retry_reraise_expect():
        raise ValueError("Raise ValueError")
    with pytest.raises(ValueError) as exc_info:
        await no_retry_reraise_expect()
    assert str(exc_info.value) == "Raise ValueError"


@pytest.mark.asyncio
async def test_no_retry_reraise_unexpect():
    @async_retry(ValueError, KeyError,
                 retry=False,
                 attempts=3,
                 wait=1.5,
                 reraise=True,
                 logger=logging.warning)
    async def no_retry_reraise_unexpect():
        raise IOError("Raise Test")
    with pytest.raises(IOError) as exc_info:
        await no_retry_reraise_unexpect()
    assert str(exc_info.value) == "Raise Test"


@pytest.mark.asyncio
async def test_retry_no_reraise_expect():
    @async_retry(ValueError, KeyError,
                 retry=True,
                 attempts=3,
                 wait=1.5,
                 reraise=False,
                 logger=logging.warning)
    async def retry_no_reraise_expect():
        raise ValueError("Raise ValueError")
    assert await retry_no_reraise_expect() == None


@pytest.mark.asyncio
async def test_retry_no_reraise_unexpect():
    @async_retry(ValueError, KeyError,
                 retry=True,
                 attempts=3,
                 wait=1.5,
                 reraise=False,
                 logger=logging.warning)
    async def retry_no_reraise_unexpect():
        raise IOError("Raise Test")
    assert await retry_no_reraise_unexpect() == None


@pytest.mark.asyncio
async def test_no_retry_no_reraise_expect():
    @async_retry(ValueError, KeyError,
                 retry=False,
                 attempts=3,
                 wait=1.5,
                 reraise=False,
                 logger=logging.warning)
    async def no_retry_no_reraise_expect():
        raise ValueError("Raise ValueError")
    assert await no_retry_no_reraise_expect() == None


@pytest.mark.asyncio
async def test_no_retry_no_reraise_unexpect():
    @async_retry(ValueError, KeyError,
                 retry=False,
                 attempts=3,
                 wait=1.5,
                 reraise=False,
                 logger=logging.warning)
    async def no_retry_no_reraise_unexpect():
        raise IOError("Raise Test")
    assert await no_retry_no_reraise_unexpect() == None


@pytest.mark.asyncio
async def test_object_method():
    class ObjedtMethod():
        @async_retry(ValueError, reraise=True, wait=0.5, logger=logging.warning)
        async def raise_error(self):
            raise ValueError("Raise Test")
    obj = ObjedtMethod()
    with pytest.raises(ValueError) as exc_info:
        await obj.raise_error()
    assert str(exc_info.value) == "Raise Test"
