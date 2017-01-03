from PIL import Image
import imagehash
import csv
import os

# Empty the csv file
with open("data/images_hash.csv", "w"):
    pass

with open('data/images_hash.csv', 'w', newline='') as csvfile:
    hashwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for file in os.listdir("data/images"):
        if file.endswith(".jpg") or file.endswith(".png"):
            hashwriter.writerow([imagehash.average_hash(Image.open("data/images/" + file)),"data/images/" + file])


print("Done.")
 