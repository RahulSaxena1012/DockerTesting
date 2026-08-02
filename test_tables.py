from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    price_index = 0
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content() == "Price":
            price_index = index
            break

    ispresent = page.locator("tr").get_by_text("Strawberry").count()>0
    ricerow = page.locator("tr").filter(has_text="Strawberry")
    ricePrice = ricerow.locator("td").nth(price_index).text_content()
    assert ricePrice == "56"
