from selenium import webdriver
import logging
import threading
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def pageHandler(temp):
    a=temp.find('a', href=True)
    print ("Found the URL:", a['href'])


def shutdown():
    browser.quit()

def test(name):
    logging.info("Thread %s: starting", name)
    xt = webdriver.Firefox()
    xt.get("https://www.willhaben.at/iad/immobilien/haus-kaufen/haus-angebote?rows=100")
    assert "Haus kaufen - willhaben" in xt.title
    xt.find_element(by=By.XPATH, value='//*[@id="didomi-notice-agree-button"]').click()
    time.sleep(2)
    xt.quit()
    logging.info("Thread %s: finishing", name)

def main():
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    #logging.info("Main    : before creating thread")

    x = threading.Thread(target=test, args=(1,))
    y = threading.Thread(target=test, args=(2,))
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    x.join()
    logging.info("Main    : all done")

    #global browser
    #browser = webdriver.Firefox()
    #browser.get("https://www.willhaben.at/iad/immobilien/haus-kaufen/haus-angebote?rows=100")
    #assert "Haus kaufen - willhaben" in browser.title
    #browser.find_element(by=By.XPATH, value='//*[@id="didomi-notice-agree-button"]').click()

    #doc = BeautifulSoup(browser.page_source, "html.parser")
    #temp = doc.find("div", class_="Box-sc-wfmb7k-0 ResultListAdRowLayout___StyledBox-sc-1rmys2w-0 iXdpLu bHgpCD")
    #pageHandler(temp)
    #time.sleep(2)

    #shutdown()


if __name__ == "__main__":
    main()