import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from Sprint2.login import loginpage
from Sprint2.signin import signinpage
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="type of browser: chrome, safari, firefox, edge"
    )

    
@pytest.fixture(scope="session")
def driver(request): 
    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser_type == "safari":
        driver = webdriver.Safari()

    elif browser_type == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    else:
        raise ValueError(f"browser {browser_type} not supported")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    return loginpage(driver)


@pytest.fixture
def registro(driver):
    return signinpage(driver)
