from PIL import Image
import imagehash
import csv
import urllib.request

from datetime import datetime
from datetime import timedelta

#######################################
# 
#######################################
def load_hash():
    hash_arr = []
    with open("data/images_hash.csv", 'r' , newline='') as csvfile:
        hashreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for h in hashreader:
            hash_arr.append(h)
    return hash_arr

def compare(img_hash, hash_arr, threshold):
    for h in hash_arr:
        if abs(img_hash - int(h[0], 16)) < threshold:
            print("Repost detected")
            print("Repost from: " + str(h[1]))
            return False
    return True

reference_array = load_hash()

URL = "https://scontent.xx.fbcdn.net/v/t1.0-0/s130x130/15825978_1412528322113468_829569879456018077_n.jpg?oh=c2be5eb3b0d16c9803229d7b2ae67c97&oe=591AA57E"
urllib.request.urlretrieve(URL, "data/temp.jpg")
img = Image.open("data/temp.jpg")

img_hash = int(str(imagehash.average_hash(img)),16)

if compare(img_hash,reference_array,10):
    print("This is not a repost")
    with open('data/images_hash.csv', 'a', newline='') as csvfile:
        hashwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        hashwriter.writerow(['{:016x}'.format(img_hash),URL])

