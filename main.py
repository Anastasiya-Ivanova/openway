from selenium import webdriver
from time import sleep

login = 'openwaytask@yandex.ru'
passwd = 'openwaypassword'


def is_el_displayed(element) -> None:
    if element.is_displayed():
        return
    raise Exception('No element is displayed')


def press_button(class_name: str, num: int = 1) -> None:
    global browser
    btn = browser.find_elements_by_class_name(class_name)[num]
    is_el_displayed(btn)
    btn.click()
    sleep(5)


def paste_value_in_input_filed(filed: str, value: str) -> None:
    global browser
    input_field = browser.find_element_by_name(filed)
    is_el_displayed(input_field)
    input_field.send_keys(value)


def is_letter_unread(letter) -> bool:
    unread_flags = letter.find_elements_by_class_name('state_toRead')
    return len(unread_flags) != 0


def get_unread_messages() -> str:
    for letter in browser.find_elements_by_class_name('ns-view-messages-item-wrap'):
        if is_letter_unread(letter):
            letter_title = letter.find_element_by_class_name('js-message-snippet-text').text
            return letter_title.split('\n')[0]
    raise Exception('No unread messages')


while True:
    browser = webdriver.Chrome('./chromedriver.exe')
    browser.get('https://mail.yandex.ru')
    try:
        press_button('button2')

        paste_value_in_input_filed('login', login)

        press_button('button2')

        paste_value_in_input_filed('passwd', passwd)

        press_button('button2', 0)

        print(get_unread_messages())
    except Exception as e:
        print(e)
        browser.close()
        continue
    break

browser.close()
