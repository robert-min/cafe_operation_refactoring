import os
import sys
users_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
tests_path = os.path.abspath(os.path.join(users_path, os.path.pardir))
src_path = os.path.abspath(os.path.join(tests_path, os.path.pardir))
apps_path = os.path.abspath(os.path.join(src_path, "apps"))

if src_path not in sys.path:
    sys.path.append(src_path)

if apps_path not in sys.path:
    sys.path.append(apps_path)
