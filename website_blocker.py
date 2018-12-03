import time
from datetime import datetime as dt

hosts_temp = r"D:\SOFTWARES\My Programming Study\Python Total\PythonExcercise\12 Application 3 Building a Website Blocker\124 Implementing the Second Part\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"
website_lists = ["www.facebook.com","facebook.com","4tube.com","www.4tube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Office time...")
        with open(hosts_path, "r+") as file:
            #opened file from hosts_path in write and append mode. and gave a neme "file"
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                # pass = skip
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines() # reading line1,2,3...
            file.seek(0) #courser return to the 1st/0 position
            for line in content:
                if not any(website in line for website in website_lists):
                #if website absent in line then write the line
                    file.write(line)
            file.truncate()

        print("Take rest...")
    time.sleep(5)
