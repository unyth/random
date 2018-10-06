#!/usr/bin/python3

from pathlib import Path
import hashlib

import sys


def enumerate_files(path):
	if not path.is_dir():
		return []
	else:
		return [x for x in path.iterdir() if x.is_file()]

def create_hash(file_path, hash=hashlib.sha256):
	bytes = file_path.read_bytes()
	hashed = hash(bytes).hexdigest()
	return hashed[:512]

def file_exists(file_path, dir_path):
	return (dir_path / file_path.resolve().name).is_file

if len(sys.argv) < 2:
	print("Wrong number of many arguments.")
	print("python {} [directory] [optional stem]".format(sys.argv[0]))
	sys.exit()

p = Path(sys.argv[1])

stem = "file_"

if len(sys.argv) == 3:
    stem = sys.argv[2]

i = 0
for file in enumerate_files(p):
    suffix = "".join(file.suffixes)
    name = stem + "{:0>6}".format(i) + suffix
    file.rename(name)
    i += 1
