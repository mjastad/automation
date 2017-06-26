'''
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"
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
