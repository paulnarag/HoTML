import fire
from pathlib import Path

# HTMLpath = "index.html"
# CSSpath = "style.css"
# JSpath = "script.js"

# paths = ["index.html", "style.css", "script.js"]

# yesInputs = ["y", "Y", ""]




            
# def getFilenames():
#     for i in range(len(paths)):
#         extension = paths[i].split(".", 1)[1].upper()
#         choice = input(f"Are you ok with the {extension} file, {paths[i]}? (y/n): ")
#         if choice == "n":
#             while True:
#                 newName = input(f"Your choice of file name for the {extension} file (not ok with file): ")

#                 if newName != "":
#                     paths[i] = newName
#                     break
                
#                 print("You have entered an invalid name, please try again.")



# def createFiles():
#     for x in range(len(paths)):
#         extension = paths[x].split(".", 1)[1].upper()

#         try:
#             file = open(paths[x], "x")
#             file.close()
#             print(f"File created {paths[x]}")
#         except FileExistsError:
#             newName = input(f"Your choice of file name for the {extension} file (file exists error): ")
#             while True:
#                 if newName == "" or newName in paths or Path(newName).is_file():
#                     newName = input(f"Please choose a new file name: ")
#                 else:
#                     paths[x] = newName
#                     break
#             file = open(paths[x], "x")
#             file.close()
#             print(f"new attempt File created {paths[x]}")

            
                
                

defaults = {
    "HTML": "index.html",
    "CSS": "style.css",
    "JS": "script.js"
}

for lang, fileName in defaults.items():
    print(f"{lang} file: ({fileName}): ")

# getFilenames()
# createFiles()


#if __name__ == '__main__':
#    fire.Fire(createInWD)