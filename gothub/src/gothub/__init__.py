import argparse


def main():
    parser = argparse.ArgumentParser(description="GPT Engineer")
    parser.add_argument(
        "prompt",
        nargs="+",
        type=str,
        default="create a web server that greets people in a web page,use python",
        help="Prompt line",
    )
    args = parser.parse_args()
    line = ""
    for i in args.prompt:
        line += i + " "
    print(f'Requirement: {line.strip("")}')

    print("Hello Gothub!")
