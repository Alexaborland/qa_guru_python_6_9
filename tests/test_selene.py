import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "alexandra_borland")
@allure.description("Тест без шагов и декораторов")
@allure.feature("'Поиск issues в Github")
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open("https://github.com")
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

    browser.quit()