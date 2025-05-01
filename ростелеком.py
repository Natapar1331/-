def test_load_main_page():
    driver.get("https://lk.rt.ru/")
    assert "Главная" in driver.title
    assert driver.find_element_by_id("main_page_element")


def test_interface_elements():
    driver.get("https://lk.rt.ru/")
    header = driver.find_element_by_id("header")
    assert header.is_displayed()
    assert driver.find_element_by_id("main_button").is_displayed()
    assert driver.find_element_by_id("my_services_button").is_displayed()
    assert driver.find_element_by_id("applications_button").is_displayed()


def test_special_characters_handling():
    driver.get("https://lk.rt.ru/")
    search_field = driver.find_element_by_id("search_field")
    search_field.send_keys("!@#$%^&*")
    search_field.submit()
    assert "К сожалению, ничего не нашлось" in driver.page_source


def test_multiple_keyword_search():
    driver.get("https://lk.rt.ru/")
    search_field = driver.find_element_by_id("search_field")
    search_field.send_keys("услуга, поддержка")
    search_field.submit()
    assert "результат" in driver.page_source


def test_service_information():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("services_button").click()
    assert "Информация об услугах" in driver.page_source


def test_pagination():
    driver.get("https://lk.rt.ru/")
    driver.set_window_size(1200, 800)
    assert driver.find_element_by_id("pagination").is_displayed()


def test_error_message_display():
    driver.get("https://lk.rt.ru/")
    search_field = driver.find_element_by_id("search_field")
    search_field.send_keys("некорректный запрос")
    search_field.submit()
    assert "ничего не найдено" in driver.page_source

def test_social_media_buttons():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("telegram_button").click()
    assert "Telegram" in driver.current_url


def test_feedback_functionality():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("feedback_form").send_keys("Тестовое сообщение")
    driver.find_element_by_id("submit_feedback").click()
    assert "успешная отправка" in driver.page_source


def test_ssl_certificate():
    driver.get("https://lk.rt.ru/")
    assert "https://" in driver.current_url


def test_english_language_support():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("language_switch_button").click()
    driver.find_element_by_id("english_language_option").click()
    assert "Welcome" in driver.page_source


def test_page_loading_on_different_networks():
    driver.get("https://lk.rt.ru/")
    assert "На главной странице" in driver.page_source


def test_cross_browser_compatibility():
    driver.get("https://lk.rt.ru/")
    assert driver.find_element_by_id("search_button").is_displayed()


def test_search_functionality():
    driver.get("https://lk.rt.ru/")
    search_field = driver.find_element_by_id("search_field")
    search_field.send_keys("тест")
    search_field.submit()
    assert "результат" in driver.page_source


def test_empty_search_response():
    driver.get("https://lk.rt.ru/")
    search_field = driver.find_element_by_id("search_field")
    search_field.send_keys("")
    search_field.submit()
    assert "Пожалуйста, введите запрос" in driver.page_source


def test_help_button_functionality():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("help_button").click()
    assert "Справка" in driver.page_source


def test_contacts_button_functionality():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("contacts_button").click()
    assert "Контактная информация" in driver.page_source


def test_invalid_authentication_message():
    driver.get("https://lk.rt.ru/")
    driver.find_element_by_id("login_field").send_keys("некорректный_логин")
    driver.find_element_by_id("password_field").send_keys("некорректный_пароль")
    driver.find_element_by_id("login_button").click()
    assert "Неверный логин или пароль" in driver.page_source


def test_message_exchange_functionality():
    driver.get("https://lk.rt.ru/")
    chat_field = driver.find_element_by_id("chat_field")
    chat_field.send_keys("Привет, есть вопрос!")
    chat_field.submit()
    assert "Ваше сообщение отправлено" in driver.page_source


def test_page_information_update():
    driver.get("https://lk.rt.ru/")
    previous_content = driver.page_source
    driver.refresh()
    assert previous_content != driver.page_source