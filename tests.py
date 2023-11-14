import os
from unittest.mock import MagicMock, Mock, patch
import pytest
from dalle3.dalle import Dalle

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
def test_download(mock_get, mock_makedirs, dalle):
    mock_response = MagicMock()
    mock_response.content = b"test_content"
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    urls = ["http://test.com/image1.png", "http://test.com/image2.png"]
    save_folder = "test_folder"

    dalle.download(urls, save_folder)

    assert mock_get.call_count == len(urls)
    assert mock_makedirs.called


@patch("selenium.webdriver.Chrome.get")
@patch("selenium.webdriver.Chrome.add_cookie")
@patch("selenium.webdriver.Chrome.refresh")
def test_create(mock_refresh, mock_add_cookie, mock_get, dalle):
    query = "test_query"
    result = dalle.create(query)

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


# Create a mock for the Chrome driver
@pytest.fixture
def mock_chrome_driver():
    return Mock()

# Create a mock for the requests module
@pytest.fixture
def mock_requests_module():
    return Mock()

# Sample cookie value for testing
@pytest.fixture
def sample_cookie_value():
    return "sample_cookie_value"

# Sample query for testing
@pytest.fixture
def sample_query():
    return "sample_query"

# Test the Dalle class initialization
def test_dalle_init(sample_cookie_value):
    dalle = Dalle(sample_cookie_value)
    assert dalle.cookie_value == sample_cookie_value

# Test the Dalle class get_time method
def test_dalle_get_time():
    dalle = Dalle("")
    time = dalle.get_time()
    assert isinstance(time, str)

# Test the Dalle class get_time_save method
def test_dalle_get_time_save():
    dalle = Dalle("")
    time_save = dalle.get_time_save()
    assert isinstance(time_save, str)

# Test the Dalle class download method
def test_dalle_download(sample_requests_module, sample_query):
    dalle = Dalle("")
    urls = ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
    save_folder = "test_images"
    dalle.download(urls, save_folder)
    # Add assertions here to check if images were downloaded correctly

# Test the Dalle class create method
def test_dalle_create(mock_chrome_driver, sample_cookie_value, sample_query):
    dalle = Dalle(sample_cookie_value)
    dalle.driver = mock_chrome_driver
    cookie_value = {"name": "_U", "value": sample_cookie_value}
    assert not dalle.create(sample_query)
    dalle.driver.add_cookie.assert_called_once_with(cookie_value)

# Test the Dalle class get_urls method
def test_dalle_get_urls(mock_chrome_driver, sample_query):
    dalle = Dalle("")
    dalle.driver = mock_chrome_driver
    mock_chrome_driver.get.return_value = None
    mock_chrome_driver.find_elements.return_value = [
        Mock(get_attribute=Mock(return_value="https://example.com/image1.jpg")),
        Mock(get_attribute=Mock(return_value="https://example.com/image2.jpg")),
    ]
    urls = dalle.get_urls()
    assert len(urls) == 2
    assert "https://example.com/image1.jpg" in urls
    assert "https://example.com/image2.jpg" in urls

# Test the Dalle class run method
def test_dalle_run(mock_chrome_driver, sample_query, sample_requests_module):
    dalle = Dalle("")
    dalle.driver = mock_chrome_driver
    mock_chrome_driver.get.return_value = None
    mock_chrome_driver.find_elements.return_value = [
        Mock(get_attribute=Mock(return_value="https://example.com/image1.jpg")),
        Mock(get_attribute=Mock(return_value="https://example.com/image2.jpg")),
    ]
    mock_requests_module.get.return_value = Mock(content="image_content")
    dalle.run(sample_query)
    # Add assertions here to check if the download was successful


# Test the Dalle class close method
def test_dalle_close(mock_chrome_driver):
    dalle = Dalle("")
    dalle.driver = mock_chrome_driver
    dalle.close()
    mock_chrome_driver.quit.assert_called_once()



