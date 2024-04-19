
import shutil
from glob import glob
from os import path
from time import sleep


def get_next_file_number():
    result = 0

    # check if something exists (and if so, add one so we do not overwrite)
    for f in glob("history/*.py"):
        f_str = path.basename(f).replace(".py", "").split("_")[0]
        f_int = int(f_str)
        # print(f_str, f_int)
        if f_int > result:
            result = f_int
    if result > 0:
        result += 1
    # print("----> ", result)
    return result


counter = get_next_file_number()

while (True):
    print(".", end="", flush=True)
    if counter % 60 == 0:
        print(counter)
    for f in ["meditation.py", "meditation.png"]:
        if path.isfile(f):
            target = f"history/{str(counter).zfill(6)}_{f}"
            # print(target)
            shutil.copyfile(f, target)
    counter += 1
    sleep(10)
