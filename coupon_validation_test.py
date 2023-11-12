from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.implicitly_wait(20)

try:
    driver.get("http://dev.bootcamp.store.supersqa.com/")

    add_to_cart_button =driver.find_element(By.LINK_TEXT, 'Add to cart')
    add_to_cart_button.click()

    view_cart_button =driver.find_element(By.LINK_TEXT,'View cart')
    view_cart_button.click()

    coupon_input = driver.find_element(By.ID, 'coupon_code')
    coupon_input.send_keys("EXP20231031")
    apply_coupon_button = driver.find_element(By.NAME, 'apply_coupon')
    apply_coupon_button.click()

    error_message_locator = (By.XPATH, '//ul[@class="woocommerce-error"]/li[contains(text(), "This coupon has expired.")]')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(error_message_locator))

    error_message = driver.find_element(*error_message_locator).text
    if error_message == "This coupon has expired.":
        print("Successful")
    else:
        print("Coupon validation failed")

finally:
    driver.quit()
