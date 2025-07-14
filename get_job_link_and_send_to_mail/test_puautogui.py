""" Apply on a job"""
import os
import subprocess
import urllib.parse
import pyautogui
import pyperclip

URL_LINK = "https://eg.indeed.com/jobs?q=Embedded+linux&l=&from=searchOnHP&v"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LINK_IMAGE_PATH = os.path.join(SCRIPT_DIR, "link.png")
SEND_IMAGE_PATH = os.path.join(SCRIPT_DIR, "send.png")
BROSWER_PATH = r"firefox"
MAIL_PATH = r"thunderbird"
SUBJECT = r"Job link"
MAIL =r"moh.hafez98@gmail.com"
def click_image(image_path):
    while True:
        try:
            if pyautogui.locateOnScreen(image_path, confidence = 0.8) is not None:
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.sleep(1)


subprocess.run([BROSWER_PATH, URL_LINK])
click_image(LINK_IMAGE_PATH)
pyautogui.click(pyautogui.locateCenterOnScreen(LINK_IMAGE_PATH, confidence = 0.8))
pyautogui.sleep(2)
job_link = pyperclip.paste()
mail_to_send = f"mailto:{MAIL}?subject={urllib.parse.quote(SUBJECT)}&body={urllib.parse.quote(job_link)}"
subprocess.Popen(["thunderbird", mail_to_send])
click_image(SEND_IMAGE_PATH)
pyautogui.click(pyautogui.locateCenterOnScreen(SEND_IMAGE_PATH, confidence = 0.8))
pyautogui.sleep(2)
