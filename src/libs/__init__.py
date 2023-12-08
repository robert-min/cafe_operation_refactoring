import os
import json

libs_path: str = os.path.abspath(os.path.join(__file__, os.path.pardir))
conf_file: str = os.path.abspath(os.path.join(libs_path, "conf.json"))
with open(conf_file, "rt") as f:
    conf = json.load(f)
    
ENCRYPTION_KEY = conf["encrypt_dek"]