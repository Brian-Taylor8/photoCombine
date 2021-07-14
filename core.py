import numpy as np
import cv2 
import os
from natsort import natsorted

class Collage:
    def __init__(self, initial_photo = None):
        if initial_photo:
            self.paths = [initial_photo]
        else:
            self.paths = []
    
    def add_photo(self, photo_path):
        self.paths.append(photo_path)
    
    def make_square(self):
        print(np.shape(cv2.imread(self.paths[0])), np.shape(cv2.imread(self.paths[1])))
        top = np.hstack((cv2.imread(self.paths[0]), cv2.imread(self.paths[1])))
        print(np.shape(cv2.imread(self.paths[2])), np.shape(cv2.imread(self.paths[3])))
        bottom = np.hstack((cv2.imread(self.paths[2]), cv2.imread(self.paths[3])))
        print(np.shape(top), np.shape(bottom))
        cv2.imwrite("final.png", np.vstack((top, bottom)))

    def trim_photo(self, num=0):
        img = cv2.imread(self.paths[num])
        final = img[220:1650, 500:2180]
        cv2.imwrite(f"trimmed{num}.png", final)

    def list_sizes(self):
        for file in self.paths:
            print(np.shape(cv2.imread(file)))
if __name__ == '__main__':
    print("hey")
    base = "/Users/briantaylor/Desktop/photoCombine/"
    myCollage = Collage()
    # for file in natsorted(os.listdir('.')):
    #     if ".png" in file:
    #         print(file)
    #         myCollage.add_photo(file)
    myCollage.add_photo(base + "trimmed1.png")
    myCollage.add_photo(base + "trimmed0.png")
    myCollage.add_photo(base + "trimmed3.png")
    myCollage.add_photo(base + "trimmed2.png")
    myCollage.list_sizes()
    myCollage.make_square()
    # myCollage.trim_photo(3)

        