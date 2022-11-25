from selenium import webdriver
from immoClass import immo
import logging
import threading
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def dataExtractor(pagedata, link):
    # Getting Name of HTML Text
    name = pagedata.find("h1", class_="Text-sc-10o2fdq-0 bLnjhH").text

    # Getting LastEdit and Id of HTML Text
    tmp = pagedata.find("div", class_="Box-sc-wfmb7k-0 fNncFQ").find_all("span", class_="Text-sc-10o2fdq-0 kTmUzk")
    lastEdit = tmp[0].text.split(": ")[1]
    id = tmp[1].text.split(": ")[1]

    # Getting Price of HTML Text
    try:
        price = pagedata.find("span", class_="Text-sc-10o2fdq-0 iYbzSg").text
    except:
        price = ""


    # Getting Bundesland and Ort of HTML Text
    tmp = pagedata.find("div", class_="Box-sc-wfmb7k-0 hxEWsd").find_all("div", class_="Box-sc-wfmb7k-0 gtvony")
    bundesland = tmp[3].text
    ort = tmp[4].text

    attrNames = pagedata.find("div", class_="Box-sc-wfmb7k-0 hhZogD").find_all("span", class_="Text-sc-10o2fdq-0 jnPJDV")
    attrValues = pagedata.find("div", class_="Box-sc-wfmb7k-0 hhZogD").find_all("div", class_="Box-sc-wfmb7k-0 PropertyList___StyledBox2-sc-e2zq14-2 YlyIg")
    attributes = {
    "Names": "Values"
    }
    for i in range(0,len(attrNames)):
        attributes[attrNames[i].text] = attrValues[i].text

    temp = immo(id, name, link, lastEdit, price, bundesland, ort, attributes)
    print(temp.toString())
    

def getPageContent(link):   
    browser = webdriver.Firefox()
    browser.get(link)
    assert "willhaben" in browser.title
    browser.find_element(by=By.XPATH, value='//*[@id="didomi-notice-agree-button"]').click()
    doc = BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()
    return doc




def firstPageHandler():
    pageContent = getPageContent("https://www.willhaben.at/iad/immobilien/haus-kaufen/haus-angebote?rows=100")
    temp = pageContent.find_all("div", class_="Box-sc-wfmb7k-0 ResultListAdRowLayout___StyledBox-sc-1rmys2w-0 iXdpLu bHgpCD")
    #temp = pageContent.find("div", class_="Box-sc-wfmb7k-0 ResultListAdRowLayout___StyledBox-sc-1rmys2w-0 iXdpLu bHgpCD").find('a', href=True)
    #link = "https://www.willhaben.at"+ temp['href']
    #newContent = getPageContent(link)
    #dataExtractor(newContent, link)
    print("Test")

def main():
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    x = threading.Thread(target=firstPageHandler)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")


if __name__ == "__main__":
    main()