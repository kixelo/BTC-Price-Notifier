from selenium import webdriver
import time
import yagmail
import os

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://coinmarketcap.com/")
  return driver

def clean_text(text):
  output=text.replace(",","").replace("$", "")
  return float(output)

def main():
  driver=get_driver()
  print(driver)
  time.sleep(2)
  element = driver.find_element(by="xpath", value='//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[4]/div/a/span')
  return clean_text(element.text)

def notification():
  crypto_price=main()
  sender = "pypip2022@gmail.com"
  receiver = "igorolexik@gmail.com"
  subject = "BTC price change"
  contents = f"Bitcoin price change notification, the current BTC price is {crypto_price}"

  yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
  if crypto_price > 20942:
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent!")
  else:
    print("No significant change")
  return crypto_price

print(notification())