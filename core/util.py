import os
import importlib


def get_py_files(src: str, pattern: str):
    cwd = os.getcwd()  # Current Working directory
    py_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file == pattern:
                py_files.append(os.path.join(cwd, root, file))
    return py_files


def dynamic_import(module_name, py_path):
    module_spec = importlib.util.spec_from_file_location(module_name, py_path)
    try:
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module
    except Exception as e:
        raise Exception( f"Error importing module {module_name} from {py_path}") from e
        



def import_source(src: str, pattern: str, star_import=False):
    my_py_files = get_py_files(src, pattern)
    for py_file in my_py_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_module = dynamic_import(module_name, py_file)
        if star_import:
            for obj in dir(imported_module):
                globals()[obj] = imported_module.__dict__[obj]
        else:
            globals()[module_name] = imported_module
    return
