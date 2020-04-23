# coding: utf-8

import sys
import os
import yaml
from random import randint
from hashlib import sha256
from base64 import b64encode

KEY_DIST_FILE_NAME = "dist_file_name"
KEY_DIST_PATH = "dist_path"
KEY_NODE_LIST = "node_list"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: SubParser <config_file_name>")
        exit(-1)

    file_name = sys.argv[1]

    obj = None
    with open(file_name, "r", encoding="utf-8") as fp:
        obj = yaml.load(fp.read())
        print("File loaded: " + file_name)

    dist_file_name = obj.get(KEY_DIST_FILE_NAME, "")
    if not dist_file_name.strip():
        dist_file_name = sha256(str(randint(10000, 32768)).encode("utf-8")).hexdigest()
        print("To new file name: " + dist_file_name)
    dist_path = obj.get(KEY_DIST_PATH)
    with open(os.path.join(dist_path, dist_file_name), "w", encoding="utf-8") as fp:
        node_list = obj.get(KEY_NODE_LIST, [])
        out = "\n".join(node_list)
        out = b64encode(out.encode("utf-8")).decode()
        fp.write(out)
        print("Finished!")
