import fire
import os

def createInWD():
    if os.path.isfile("index.html"):
        print("index.html already exists")
        choice=input("Do you want it to be overwritten with the boilerplate HTML? (y/n): ")
        if choice=="" or choice =="y":
            indexFile = open("index.html", "")


if __name__ == '__main__':
    fire.Fire(createInWD)