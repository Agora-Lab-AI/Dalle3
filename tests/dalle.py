import pytest
import os
from unittest.mock import patch, MagicMock
from dalle3 import Dalle

test_cookie = os.getenv("BING_COOKIE") or ""


@pytest.fixture
def dalle():
    return Dalle(test_cookie)


def test_init(dalle):
    assert dalle.cookie_value == test_cookie
    assert dalle.driver is not None
    assert dalle.options is not None


@patch("os.makedirs")
@patch("requests.get")
def test_download_images(mock_get, mock_makedirs, dalle):
    mock_response = MagicMock()
    mock_response.content = b"test_content"
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    urls = ["http://test.com/image1.png", "http://test.com/image2.png"]
    save_folder = "test_folder"

    dalle.download_images(urls, save_folder)

    assert mock_get.call_count == len(urls)
    assert mock_makedirs.called


@patch("selenium.webdriver.Chrome.get")
@patch("selenium.webdriver.Chrome.add_cookie")
@patch("selenium.webdriver.Chrome.refresh")
def test_open_website(mock_refresh, mock_add_cookie, mock_get, dalle):
    query = "test_query"
    result = dalle.open_website(query)

    assert result
    mock_get.assert_called_once_with(f"https://www.bing.com/images/create?q={query}")
    mock_add_cookie.assert_called_once_with({"name": "_U", "value": test_cookie})
    mock_refresh.assert_called_once()


@patch("selenium.webdriver.support.ui.WebDriverWait.until")
def test_get_urls(mock_until, dalle):
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "http://test.com/image.png?param=value"
    mock_until.return_value = [mock_element]

    urls = dalle.get_urls()

    assert urls == ["http://test.com/image.png"]
    mock_until.assert_called_once()
