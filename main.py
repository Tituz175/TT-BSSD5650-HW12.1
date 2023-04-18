"""
A Proxy Concept Example
https://sbcode.net/python/proxy/#proxyproxy_conceptpy
"""
from PIL import Image
from abc import ABCMeta, abstractmethod


class IImageViewer(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject"

    @staticmethod
    @abstractmethod
    def display_image():
        raise NotImplementedError


class ConcreteImageViewer(IImageViewer):
    "The actual real object that the proxy is representing"

    def __init__(self, imageName):
        # hypothetically enormous amounts of data
        self.image = Image.open(imageName)

    def display_image(self):
        return self.image


class Proxy(IImageViewer):
    """
    The proxy. In this case the proxy will act as a cache for
    `enormous_data` and only populate the enormous_data when it
    is actually necessary
    """

    def __init__(self, imageName):
        self.image = None
        self.real_subject = ConcreteImageViewer(imageName)

    def display_image(self):
        """
        Using the proxy as a cache, and loading data into it only if
        it is needed
        """
        if self.image is None:
            print("pulling data from RealSubject")
            self.image = self.real_subject.display_image()
            print(self.image.format)
            print(self.image.size)
            self.image.show()
        else:
            print("pulling data from Proxy cache")
            self.image.show()


# end class Proxy(IImageViewer):


if __name__ == "__main__":
    image_viewer = Proxy("ld.jpg")
    # use SUBJECT
    print(id(image_viewer))
    # load the enormous amounts of data because now we want to show it.
    image_viewer.display_image()
    # show the data again, but this time it retrieves it from the local cache
    image_viewer.display_image()
