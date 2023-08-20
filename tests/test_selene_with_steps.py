import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "alexandra_borland")
@allure.description("Тест c помощью шагов")
@allure.feature("'Поиск issues в Github")
@allure.link('https://github.com', name='Testing')
def test_github():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открывает таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)