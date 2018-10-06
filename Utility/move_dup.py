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

if len(sys.argv) != 2:
	print("Wrong number of many arguments.")
	print("python {} [directory]".format(sys.argv[0]))
	sys.exit()

p = Path(sys.argv[1])
print(p.resolve().name)

p_originals = p / "originals"
p_duplicates = p / "duplicates"

if not p_originals.is_dir():
	p_originals.mkdir()

if not p_duplicates.is_dir():
	p_duplicates.mkdir()

hash_dict = {}

for file in enumerate_files(p):
	hash = create_hash(file)

	if hash not in hash_dict:
		hash_dict[hash] = file

	else:
		file_original = hash_dict[hash]
		name = file_original.name
		stem = file_original.stem
		suffix = "".join(file_original.suffixes)

		if not (p_originals / name).is_file():
			file_original.rename((p_originals / name))
			print(file_original)
			file.rename(p_duplicates / name)
		else:
			i = 1
			while ((p_duplicates / (stem + str(i) + suffix)).is_file()):
				i += 1
			file.rename((p_duplicates / (stem + str(i) + suffix)))
