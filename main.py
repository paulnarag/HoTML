import fire
from pathlib import Path

HTMLpath = "index.html"
CSSpath = "style.css"
JSpath = "script.js"

paths = ["index.html", "style.css", "script.js"]

def createFiles():
    for file in paths:
        file = open(file, "w")

for i in range(len(paths)):
    print(f"The {paths[i].split(".", 1)[1].upper()} file will be named {paths[i]}")
    choice = input("Are you ok with this? (y/n): ")
    if choice == "n":
        newName = input("Your choice of file name: ")
        paths[i] = newName
    #if choice == "y":

print(paths)

createFiles()


#def createInWD():



#if __name__ == '__main__':
#    fire.Fire(createInWD)