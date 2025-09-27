from main.app import App

import argparse

# entry Point of the app
def main():
    # Pars the path for the 2 input files
    parser = argparse.ArgumentParser(description="Run the segment function app with 2 input files as arguments")
    parser.add_argument("file1", type=str, help="Path to the first input file")
    parser.add_argument("file2", type=str, help="Path to the second input file")
    args = parser.parse_args()
    # Initialise and run the app
    app = App()
    app.run(args.file1,args.file2)



if __name__ == "__main__":
    main()

