import csv
import shutil
import datetime

today = datetime.date.today()
date_string = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
shutil.copyfile("data/images_hash.csv","data/past_hash/hash_at_" + date_string + ".csv")
with open("data/images_hash.csv", "w"):
        pass