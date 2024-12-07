import sys
import shutil


file_name = sys.argv[1]

backup_file = file_name + "-backup"

shutil.copy(file_name, backup_file)

print("The copy has been successful!")