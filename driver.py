from selenium import webdriver
import time
from pynput.keyboard import Key, Controller

def scraper(pages, url):
	driver = webdriver.Firefox()
	driver.get(url)
	time.sleep(6)
	keyboard = Controller()
	for x in range(pages):
		keyboard.press(Key.page_down)
		keyboard.release(Key.page_down)
	javaScript = """let jspdf = document.createElement("script");
	jspdf.onload = function () {
	    let pdf = new jsPDF();
	    let elements = document.getElementsByTagName("img");
	    for (let i in elements) {
	        let img = elements[i];
	        console.log("add img ", img);
	        if (!/^blob:/.test(img.src)) {
	            console.log("invalid src");
	            continue;
	        }
	        let can = document.createElement('canvas');
	        let con = can.getContext("2d");
	        can.width = img.width;
	        can.height = img.height;
	        con.drawImage(img, 0, 0);
	        let imgData = can.toDataURL("image/jpeg", 1.0);
	        pdf.addImage(imgData, 'JPEG', 0, 0);
	        pdf.addPage();
	    }

	    pdf.save("download.pdf");
	};
	jspdf.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.debug.js';
	document.body.appendChild(jspdf);"""
	driver.execute_script(javaScript)
	time.sleep(2)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

if __name__ == '__main__':
	print("Please be magnanimous with how many pages you specify...")
	pages = input("Approximate Pages to Scrape: ") or "14"
	print(pages)
	url = input("Google Drive Url to Scrape From: ")
	scraper(int(pages), url)



