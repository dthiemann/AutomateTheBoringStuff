import shutil, os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\sample_files"

shutil.copy(dir_path + "\\test1.txt", dir_path + "\\test1_copy.txt")
