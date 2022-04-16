import argparse
import os
from pathlib import Path
import subprocess
from InquirerPy import inquirer
import sys
import stat

script_dir = Path(os.path.dirname(os.path.realpath(__file__))).absolute()

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode")
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_copy = subparsers.add_parser("copy")
p_copy.add_argument("--choose", action="store_true", help="Choose lib")

p_install = subparsers.add_parser("install")

args = parser.parse_args()

if args.command == "copy":
    all_libs = [entry.name for entry in (script_dir / "rlibs").iterdir() if entry.is_dir()]
    if args.choose:
        name = inquirer.select(message="Chose lib:", choices=all_libs).execute()
        libs = [name]
    else:
        libs = [entry.name for entry in Path("./rlibs").iterdir() if entry.is_dir()]
    for lib in all_libs:
        print(f"Copying lib \"{lib}\"")
        rlibs_to = Path("./rlibs")
        subprocess.run(['rclone', 'sync', '-v', '--filter-from', str(script_dir / "rclone_filter.txt"), str(script_dir / "rlibs" / lib), str(rlibs_to / lib)])
elif args.command == "install":
    if os.name == "nt":
        main_script = script_dir / "main.py"
        text = f"@echo off\n\"{sys.executable}\" \"{main_script}\" %*"
        path = Path("C:\\Windows\\rlibs.bat")
        path.write_text(text)
    else:
        main_script = script_dir / "main.py"
        text = f"#!/bin/bash\n\"{sys.executable}\" \"{main_script}\" $@"
        path = Path().home() / ".local/bin/rlibs"
        if not path.parent.exists():
            path.parent.mkdir()
        path.write_text(text)
        st = path.stat()
        os.chmod(path, st.st_mode | stat.S_IEXEC)


   


