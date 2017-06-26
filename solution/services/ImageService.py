'''
@file: ImageService.py
@author: M.Jastad
'''

from model.Image import Image


class ImageService:

    def __init__(self):
        self.RESOURCE_IMG = '/images/'

    def getImage(self, conn, uuid):
        imageDictionary = conn.get(self.RESOURCE_IMG + uuid)
        return Image(imageDictionary)

    def getImages(self, conn):
        imageList = []
        imageDictionary = conn.get(self.RESOURCE_IMG)

        for image in imageDictionary['entities']:
             imageList.append(Image(image))

        return imageList

    def find(self, conn, id):
        imageList = self.getImages(conn)
        for image in imageList :
            if image.name.find(id) >= 0 : return image

        return None
