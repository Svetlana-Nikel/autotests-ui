import pytest

SISTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(
    SISTEM_VERSION == "v1.3.0",
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_sistem_version_valid():
    ...

@pytest.mark.skipif(
    SISTEM_VERSION == "v1.2.0",
reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_sistem_version_invalid():
    ...