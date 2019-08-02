from zipfile import *
import zipfile

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
import os

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# make a dic to save our detected text and faces
dic = {}


# make folder
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")

    # make sure if it exists
    isExists = os.path.exists(path)

    # then make it or not
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


# detect faces
def detect_faces(image, faces):
    detectedFaces = []
    for x, y, w, h in faces:
        face = Image.new('RGB', (w, h), (0, 0, 0))
        for i in range(w):
            for j in range(h):
                x1 = int(x + i)
                y1 = int(y + j)
                pixel = image.getpixel((x1, y1))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                face.putpixel((i, j), (r, g, b))

        # resize face images
        face = face.resize((100, 100))

        # add them into a list
        detectedFaces.append(face)

    return detectedFaces


def unzip(fileName):
    source_zip = "readonly/" + fileName + ".zip"
    target_dir = "readonly/images/"

    myzip = ZipFile(source_zip)
    myfilelist = myzip.namelist()

    mkdir(target_dir)

    dic = {}

    for name in myfilelist:

        # unzip file
        f_handle = open(target_dir + name, "wb")
        f_handle.write(myzip.read(name))

        # detect text
        img = Image.open(target_dir + name)
        text = pytesseract.image_to_string(img)

        # detect faces
        cv_img = cv.imread(target_dir + name)
        faces = face_cascade.detectMultiScale(cv_img, 1.3, 5)

        dic[text] = {}

        # if there are no faces
        if len(faces) == 0:
            dic[text][name] = "But there were no faces in that file!"
        else:
            # get detected faces
            faceImgs = detect_faces(img, faces)

            # create a contact sheet
            first_image = faceImgs[0]

            if len(faceImgs) % 5 != 0:
                b = 1 + int(len(faceImgs) / 5)
            else:
                b = int(len(faceImgs) / 5)

            contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 5, first_image.height * b))
            x = 0
            y = 0

            for img in faceImgs:
                # Lets paste the current image into the contact sheet
                contact_sheet.paste(img, (x, y))

                # Now we update our X position. If it is going to be the width of the image, then we set it to 0
                # and update Y as well to point to the next "line" of the contact sheet.
                if x + first_image.width == contact_sheet.width:
                    x = 0
                    y = y + first_image.height
                else:
                    x = x + first_image.width
            # debug   
            # display(contact_sheet)

            # now save them into a dic, text as keys, faces as values
            dic[text][name] = contact_sheet

        f_handle.close()

    myzip.close()

    return dic


def match(strs, dic):
    for key in dic:
        if strs in key:
            for nameKey in dic[key]:
                print("Results found in file " + nameKey)
                if isinstance(dic[key][nameKey], str):
                    print("But there were no faces in that file!")
                else:
                    display(dic[key][nameKey])


match("Christopher", unzip("small_img"))
match("Mark", unzip("images"))
