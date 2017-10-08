import os
import datetime

toMerge = os.listdir("Sample-Files")

def content_extractor(filename):
    with open("Sample-Files"+"/"+filename, "r") as file:
        file.seek(0)
        content = file.read()
        return content

newfile = datetime.datetime.now()

for i in toMerge:
    with open(newfile.strftime("%Y-%m-%d")+".txt", "a") as file:
        file.write(content_extractor(i)+"\n")
