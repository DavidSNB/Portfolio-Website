import codecs
import os
from bs4 import BeautifulSoup

fileType = ".html"
parentPath = "."

htmlFiles = []

print("Initial Paths: ", os.listdir(parentPath))


def deepFolderSearch(fT, pP='.'):
    filePaths = []

    def search(ft, pp):
        childPaths = os.listdir(pp)

        for path in childPaths:
            if path[0] != "." and "python-ignore" not in path:
                fullPath = pp + "\\" + path
                if os.path.isdir(fullPath):
                    # print(fullPath)
                    search(ft, fullPath)
                elif ft in path:
                    filePaths.append(fullPath)

    search(fT, pP)

    return filePaths


# print(deepFolderSearch(fileType, parentPath))

with open(".\\components python-ignore\\head.html", "r") as f:
    contents = f.read()
    standardHead = BeautifulSoup(contents, 'lxml')

"""
with open(path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        print(soup.head)
        soup.head = standardHead

with open(path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        print(soup.head)
        soup.head = standardHead
"""

count = 0

for path in deepFolderSearch(fileType, parentPath):
    with open(path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        # soup.head = standardHead
        print(soup.find("head", class_="python-allow"))

    """
    htmlFiles.append([codecs.open(path[0], 'r', 'utf-8').read(), path[1]])
    print(htmlFiles[count][1])
    count += 1
    """
