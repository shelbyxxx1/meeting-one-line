"""The Meeting That Should Have Been One Line.
Write its winning one-liner to the configured make.fun output file.
"""

import os


def main():
    entry = "Nobody here can approve the work, so end the meeting; this calendar invite is just a witness list."
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(entry + "\n")


if __name__ == "__main__":
    main()
