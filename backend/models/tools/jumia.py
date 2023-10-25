"""
jumia
makes requests
saves the content in file
then
"""
import os, sys, time
import random
import requests
import datetime

class Jumia:
    """
    Jumia class
    """
    web_dir = "jumia"
    url = ""
    j_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    def __init__(self):
        """
        initialization
        """
        if os.path.exists(self.web_dir) and os.path.isdir(self.web_dir):
            pass
        else:
            os.makedirs(self.web_dir)

    def check_url(self, url=""):
        """chacks the url"""
        web = "www.jumia.co.ke"
        _web = url.split("/")[2]
        if _web == web:
            return True
        elif self.web_dir in _web:
            print(f"--W--(WARN) Warning your url ({url}) does not include ({web}) got ({_web}) instead")
            return True
        else:
            print(f"--E--(ERR) Your url ({url}) is not valid. It should contain ({web})")
            return False

    def get_time(self):
        """returns the time"""
        tm = str(datetime.datetime.now()).split(".")[0].replace(" ", "_")
        tm = tm.replace(":", "-")
        return tm


    def time_to_wait(mn=5, mx=15):
        """generates the time to wait"""
        tm = random.randint(5, 15)
        return tm

    def get_item(self, url):
        """returns the item"""

        webdir = url.split(".")[1]
        if webdir != self.web_dir:
            print(f"--W--(WARN) {webdir} is not same as {self.web_dir}")
        item = str(url.split(".")[-1]).split("=")[1]
        return item

    def save_content(self, path="item", content=""):
        """saves the content to a file"""
        tm = self.get_time()
        path = f"{self.web_dir}/{path}_{tm}.html"
        try:
            with open(path, "wb") as f:
                f.write(content)
                print(f"~~SVD~~(SAVED): Saved Content in {path}")
        except Exception as e:
            print(f"--E--(ERR): While saving Content in {path}\n{e}")

    def confirm_item(self, item=""):
        """checks for item requests before making another one"""

        found_request = []
        if os.path.exists(self.web_dir):
            files = os.listdir(self.web_dir)
            for file in files:
                if item in file:
                    found_request.append(file)
        if len(found_request) > 0:
            print(f"--FND--(FOUND): No need to Request \n File: {found_request[0]}")
            if len(found_request) > 1:
                print(f"--A--(ALERT): Found multiple content of same item \n Files:{found_request}")
            return found_request[0]
        else:
            return False

    def get_item_content(self, item_path=""):
        """Returns the content from the file"""

        path = f"{self.web_dir}/{item_path}"
        try:
            with open(path, "rb") as f:
                content = f.read()
                return content
        except Exception as e:
            print(f"--E--(ERR): Could not get the item in {path}\n{e}")


    def make_request(self, url, headers=j_headers):
        """
        makes the request and returns the content
        """
        self.url = url
        if self.check_url(url):
            item = self.get_item(url)
            status = self.confirm_item(item)
            if status is False:
                tm = self.time_to_wait()
                print(f"\t\tWait for {tm} sec...")
                time.sleep(tm)
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    self.save_content(item, response.content)
                    return response.content
                else:
                    print(f"---E-X-(ERROR CODE: {response.status_code}) While Making the Request CODE: {response.status_code}")
                    print(f"--E-X-(ERR): Can't continue")
                    return False
            else:
                content = self.get_item_content(status)
                return content
        else:
            return False

