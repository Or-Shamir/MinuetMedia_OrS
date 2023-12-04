"""
Test steps:
1. Open a new browser window.
2. Navigating to the required url : https://www.90min.com.
3. Maximize the window in order to see the links in the header menu.
4. Locate the headers menu element.
5. Find all the links texts within the header and insert them into a 'header_links' list.
6. Create a 'links_to_assert' list with all the required links texts.
7. Iterate through both lists and validate the links texts from the 'links_to_assert' list
   appears in the 'header_links' list.


Expected results:
1-4. None
5. header_links = ['News', 'Transfer News', 'Premier League', 'European Leagues', 'Champions League', 'Women', 'Features']
6. links_to_assert = ["Premier League", "Champions League", "FanVoice", "The Switch", "EFL",
                     "La Liga", "Serie A", "More", "Transfers", ]
7. Assertion error will fail the test in the first required link text that wasn't in the 'header_links' list.


Actual results:
1-4. None
5. header_links = ['News', 'Transfer News', 'Premier League', 'European Leagues', 'Champions League', 'Women', 'Features']
6. links_to_assert = ["Premier League", "Champions League", "FanVoice", "The Switch", "EFL",
                     "La Liga", "Serie A", "More", "Transfers", ]
7. AssertionError: 'FanVoice' link is not displayed in the header menu
          assert 'FanVoice' in ['News', 'Transfer News', 'Premier League', 'European Leagues', 'Champions League', 'Women', ...]

"""


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    yield driver


def test_check_header_links(driver_setup):
    driver = driver_setup
    # Navigating to the required url
    driver.get('https://www.90min.com')
    # Maximize the window in order to see the links
    driver.maximize_window()

    # Locate the headers menu element
    headers_menu = driver.find_element(By.XPATH, '//ul[@class="fixedUl_ka6l4t"]')

    # Find all the links texts within the header
    header_links = headers_menu.text.split('\n')

    # These are the links texts that are required to search
    links_to_assert = ["Premier League", "Champions League", "FanVoice", "The Switch", "EFL",
                     "La Liga", "Serie A", "More", "Transfers"]

    # Iterate through both lists and validate the links texts from the 'links to assert' list
    # appears in the header_links list
    for text in links_to_assert:
        assert text in header_links, f"'{text}' link is not displayed in the header menu"










