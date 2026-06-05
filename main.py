from pathlib import Path

defaults = {
    "HTML": "index.html",
    "CSS": "style.css",
    "JS": "script.js"
}

contents = {
    "HTML": "HyperText Markup Language",
    "CSS": "Cascading Style Sheets",
    "JS": "Javascript"
}

finalNames = {}
overwriteChoices = {}


def gettingFileNames():
    for lang, defaultName in defaults.items():
        while True:
            userInput = input(f"{lang} file ({defaultName}): ").strip()

            if userInput == "":
                chosenName = defaultName
            else:
                chosenName = userInput

            if chosenName in finalNames.values():
                print(f"{chosenName} is already selected. Please choose another name.")
                continue

            if Path(chosenName).is_file():
                overwriteChoice = input(
                    f"{chosenName} already exists. Would you like to overwrite it? (Y/n): "
                ).strip().lower()

                if overwriteChoice == "y" or overwriteChoice == "":
                    finalNames[lang] = chosenName
                    overwriteChoices[lang] = True
                    break

                elif overwriteChoice == "n":
                    print("Please choose another file name.")
                    continue

                else:
                    print("Please enter y or n.")
                    continue

            else:
                finalNames[lang] = chosenName
                overwriteChoices[lang] = False
                break


def fileCreation():
    for lang, file in finalNames.items():

        content = contents[lang]

        if overwriteChoices[lang]:
            mode = "w"
        else:
            mode = "x"

        with open(file, mode) as file:
            file.write(content)

        if mode == "w":
            print(f"Overwritten {file}")
        else:
            print(f"Created {file}")


gettingFileNames()
print(finalNames)
print(overwriteChoices)
fileCreation()