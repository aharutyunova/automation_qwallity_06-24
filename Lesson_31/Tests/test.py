
from selenium import webdriver
from Pages.main_pages import MainPage
from Pages.search_results import SearchResultsPage
from testdata import search_text
from config import url


def search_by_brand():
    driver = webdriver.Chrome()
    try:
        main_page = MainPage(driver)
        search_results_page = SearchResultsPage(driver)
        brand_filter_loc = SearchResultsPage(driver)
        price_filter_loc = SearchResultsPage(driver)

        main_page.open_url(url)
        main_page.search_product(search_text)
        search_results_page.scroll_into_view_and_hover(SearchResultsPage.PRICE_FILTER_LOC, "Scrolled into view and hovered over the element.")
        search_results_page.filter_by_brand(brand_filter_loc)
        search_results_page.filter_by_price(price_filter_loc)

        print("Test passed")
    finally:
        driver.quit()


if __name__ == "__main__":
    search_by_brand()