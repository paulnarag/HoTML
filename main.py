from pathlib import Path
import fire

defaults = {
    "HTML": "index.html",
    "CSS": "style.css",
    "JS": "script.js"
}



finalNames = {}
overwriteChoices = {}

def getContents():
    return {
        "HTML": f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{finalNames["CSS"]}">
</head>
<body>
    <main class="container">
        <h1>Hello, world!</h1>
        <p>Start building your project here.</p>
    </main>

    <script src="{finalNames["JS"]}"></script>
</body>
</html>''',
        "CSS": '''* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    line-height: 1.5;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
}''',
        "JS": '''console.log("Script loaded");

document.addEventListener("DOMContentLoaded", () => {
    // Your JavaScript code here
});'''
    }

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
    contents=getContents()
    for lang, filename in finalNames.items():

        content = contents[lang]

        if overwriteChoices[lang]:
            mode = "w"
        else:
            mode = "x"

        with open(filename, mode) as f:
            f.write(content)

        if mode == "w":
            print(f"Overwritten {filename}")
        else:
            print(f"Created {filename}")

def main():
    gettingFileNames()
    fileCreation()


if __name__ == "__main__":
    main()