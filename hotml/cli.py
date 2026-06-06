from pathlib import Path
import fire


DEFAULTS = {
    "HTML": "index.html",
    "CSS": "style.css",
    "JS": "script.js",
}

EXTENSIONS = {
    "HTML": [".html", ".htm"],
    "CSS": [".css"],
    "JS": [".js"],
}

final_names = {}
overwrite_choices = {}


def get_contents():
    return {
        "HTML": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{final_names["CSS"]}">
</head>
<body>
    <main class="container">
        <h1>Hello, world!</h1>
        <p>Start building your project here.</p>
    </main>

    <script src="{final_names["JS"]}"></script>
</body>
</html>
""",
        "CSS": """* {
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
}
""",
        "JS": """console.log("Script loaded");

document.addEventListener("DOMContentLoaded", () => {
    // Your JavaScript code here
});
""",
    }


def get_file_names():
    final_names.clear()
    overwrite_choices.clear()

    for lang, default_name in DEFAULTS.items():
        while True:
            user_input = input(f"{lang} file ({default_name}): ").strip()

            if user_input == "":
                chosen_name = default_name
            else:
                chosen_name = user_input

            # Validate file extension
            file_ext = Path(chosen_name).suffix.lower()
            valid_exts = EXTENSIONS[lang]
            
            if file_ext and file_ext not in valid_exts:
                print(f"Warning: {lang} file should have extension {' or '.join(valid_exts)}, not '{file_ext}'")
                confirm = input(f"Use '{chosen_name}' anyway? (y/n): ").strip().lower()
                if confirm != "y":
                    print("Please enter a valid filename.")
                    continue
            elif not file_ext and chosen_name != default_name:
                suggested = chosen_name + valid_exts[0]
                confirm = input(f"Did you mean '{suggested}'? (y/n): ").strip().lower()
                if confirm == "y":
                    chosen_name = suggested
                elif confirm != "n":
                    print("Please enter y or n.")
                    continue

            if chosen_name in final_names.values():
                print(f"{chosen_name} is already selected. Please choose another name.")
                continue

            if Path(chosen_name).is_file():
                overwrite_choice = input(
                    f"{chosen_name} already exists. Would you like to overwrite it? (Y/n): "
                ).strip().lower()

                if overwrite_choice == "y" or overwrite_choice == "":
                    final_names[lang] = chosen_name
                    overwrite_choices[lang] = True
                    break

                if overwrite_choice == "n":
                    print("Please choose another file name.")
                    continue

                print("Please enter y or n.")
                continue

            final_names[lang] = chosen_name
            overwrite_choices[lang] = False
            break


def create_files():
    contents = get_contents()

    for lang, filename in final_names.items():
        content = contents[lang]
        mode = "w" if overwrite_choices[lang] else "x"

        try:
            with open(filename, mode) as f:
                f.write(content)

            if mode == "w":
                print(f"Overwritten {filename}")
            else:
                print(f"Created {filename}")
        except PermissionError:
            print(f"Error: Permission denied. Cannot write to {filename}")
        except OSError as e:
            print(f"Error: Could not create {filename} - {e}")
        except Exception as e:
            print(f"Unexpected error creating {filename}: {e}")


def create():
    """
    Create HTML, CSS, and JS boilerplate files.
    """
    get_file_names()
    create_files()


def show_help():
    """
    Show the help message.
    """
    print("""
HoTML - HTML/CSS/JS boilerplate generator

It's called HoTML because boiling is HoT, and this creates boilerplate files
for HTML, CSS, and JS.

Commands:
    create      Create HTML, CSS, and JS boilerplate files
    help        Show this help message

Usage:
    hotml create
    hotml help
""")


def main():
    fire.Fire({
        "create": create,
        "help": show_help,
    })


if __name__ == "__main__":
    main()
    main()