import fire
from pathlib import Path

HTMLpath = "index.html"
CSSpath = "style.css"
JSpath = "script.js"

paths = ["index.html", "style.css", "script.js"]

yesInputs = ["y", "Y", ""]

# def createFiles():
#     while True:
#         for x in range(len(paths)):
#             #if Path(paths[x]).is_file():
#             #    paths[x] = open(paths[x], "x")
#             #else:
#             #    newName=input(f"The {paths[x]} file already exists, please enter a new name: ")
#             #    paths[x] = newName

#             try:
#                 file = open(paths[x], "x")
#                 break
#             except FileExistsError:
#                 newName=input(f"The {paths[x]} file already exists, please enter a new name: ")
#                 paths[x] = newName


            
def getFilenames():
    for i in range(len(paths)):
        extension = paths[i].split(".", 1)[1].upper()
        choice = input(f"Are you ok with the {extension} file, {paths[i]}? (y/n): ")
        if choice == "n":
            while True:
                newName = input(f"Your choice of file name for the {extension} file: ")

                if newName != "":
                    paths[i] = newName
                    break
                
                print("You have entered an invalid name, please try again.")



print(paths)

#createFiles()


#def createInWD():



#if __name__ == '__main__':
#    fire.Fire(createInWD)