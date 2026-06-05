import fire
from pathlib import Path

defaults = {
    "HTML": "index.html",
    "CSS": "style.css",
    "JS": "script.js"
}

finalNames = {

}

for lang, defaultName in defaults.items():
    while True:
        userInput = input(f"{lang} file: ({defaultName}): ")
        if userInput == "":
            chosenName = defaultName
        else:
            chosenName = userInput

        if Path(chosenName).is_file():
            print(f"{chosenName} already exists. Please choose another name.")
        elif chosenName in finalNames.values():
            print(f"{chosenName} is already selected. Please choose another name.")
        else:
            finalNames[lang] = chosenName
            break
for file in finalNames.values():
    with open(file, "x"):
        pass

print(finalNames)