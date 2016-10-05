'''
initial thoughts on exif and images
'''

from PIL import Image
import piexif

# im = Image.open("blah.jpg")


# print( "The size of the Image is: ")
# print(im.format, im.size, im.mode)



exif_dict = piexif.load("blah2.jpg")

# elm_list =[]

# ID = "Exif"
ID = "GPS"
fh = open("data.txt", "w")

for elm in exif_dict[ID]:
    # elm_list.append(elm)
    str_elm = str(elm)
    str_extract = exif_dict[ID][elm]

    fh.write(str_elm + " : ")
    fh.write(str(str_extract))
    fh.write("\n--------------\n")

    print(str_elm)
    print(str_extract)
    print("--------------\n")

fh.close()

# print(elm_list)



# print(exif_dict["Exif"])

# print(exif_dict["GPS"])