# Script to prompt user for paths to files to be backed up - then build out a .txt list of directories to be fed into backuptool. 

import sys

def build_srcfile():
    try:
        print("Lets Choose What To Backup....")

        with open ("src_dirs.txt", "w") as file:
            while True:
                src_dir = input("Please Enter The Absolute Path To The Folder You Wish To Backup: \n")
                file.write(src_dir + "\n")
                if input("Add Another Directory? Y/N \n") == "N" or "n":
                    break
                elif input("Add Another Directory? Y/N \n") == "Y" or "y":
                    continue
                else:
                    print("Invalid Selection")
                    break

            print("Directories Saved To src_dirs.txt")
            print("Please Run backuptool.py To Backup Your Files")
            sys.exit()
    except Exception as e:
        print(f"Error during backup: {e}")
        pass