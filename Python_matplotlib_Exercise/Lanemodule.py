import matplotlib.pyplot as plt
import matplotlib.image as mping
from PIL import Image
import numpy as np

class laneModule(object):
    def __init__(self):

        self.init()
        self.a0 = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.range = 10
        self.width = 3.5
        self.pointsX = [x for x in np.arange(self.range)]
        self.line0Y = [self.a3*pow(x, 3) + self.a2*pow(x, 2) + self.a1*x + self.a0 for x in self.pointsX]
        self.line1Y = [x + self.width for x in self.line0Y]
        self.line2Y = [x + self.width for x in self.line1Y]
        self.line3Y = [x + self.width for x in self.line2Y]



    def init(self):
        self.a0 = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def transformCoord(self):
        pass

    def updatePost(self):
        pass

    def dspl(self):

        plt.plot(self.line0Y, self.pointsX)
        plt.plot(self.line1Y, self.pointsX)
        plt.plot(self.line2Y, self.pointsX)
        plt.plot(self.line3Y, self.pointsX)
        plt.show()



if __name__ == '__main__':
    img = Image.open("veh.jpg")





    plt.imshow(img)
    # plt.show()
    LM = laneModule()
    LM.dspl()
