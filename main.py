import argparse
import os
import sys

import pdfRenamer


def main():
    """Handle command-line invocation."""
    parser = argparse.ArgumentParser(description="This is pdfRenamer")
    parser.add_argument("-m",
                        help="match filenames against pattern",
                        action="store",
                        dest="file_pattern",
                        type=str)
    parser.add_argument("input_files_dir", help="directory containing one or more PDF files",
                        nargs=1, # anticipate supporting input from multiple directories
                        type=str)
    args = parser.parse_args()
    file_pattern = args.file_pattern
    input_files_dir = args.input_files_dir[0]
    os.chdir(input_files_dir)
    try:
        gui = pdfRenamer.Gui()
        gui.scanFiles(file_pattern)
        gui.showAndRename()
        gui.loop()
    except Exception as e:
        lg.error("FIXME")
        lg.error(sys.exc_info()[0])
        raise


if __name__ == "__main__":
    main()
