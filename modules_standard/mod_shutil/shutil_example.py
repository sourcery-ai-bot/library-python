import shutil
import os

DIR_LOC = f"{os.path.dirname(os.path.realpath(__file__))}"

# Creates an archive called 'archive.zip' with all files
# within the base_dir (mod_shutil)
def create_archive():
    shutil.make_archive(
        base_name=f"{DIR_LOC}{'/archive'}",
        format="zip",
        root_dir=DIR_LOC,
        base_dir='.',
    )

if __name__ == '__main__':
    create_archive()
