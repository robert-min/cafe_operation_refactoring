import os
import json

# TODO : conf 파일 별도 폴더로 관리
libs_path: str = os.path.abspath(os.path.join(__file__, os.path.pardir))
conf_file: str = os.path.abspath(os.path.join(libs_path, "conf.json"))
with open(conf_file, "rt") as f:
    conf = json.load(f)

ENCRYPTION_KEY = conf["encrypt_dek"]
MYSQL_CONNECTION = conf["mysql_connection"]
