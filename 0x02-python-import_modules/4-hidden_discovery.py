#!/usr/bin/python3
import sys
import types
import importlib.util

# Load the compiled module
spec = importlib.util.spec_from_file_location
("hidden_4", "/path/to/hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = sorted(dir(module))

for name in names:
    if not name.startswith("__"):
        print(name)
