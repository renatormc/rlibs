import argparse
import os
from pathlib import Path
import subprocess
from InquirerPy import inquirer
import sys

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
        libs = all_libs
    for lib in all_libs:
        rlibs_to = Path("./rlibs")
        subprocess.run(['rclone', 'sync', '-v', str(script_dir / "rlibs" / lib), str(rlibs_to / lib)])
elif args.command == "install":
    if os.name == "nt":
        main_script = script_dir / "main.py"
        text = f"@echo off\n\"{sys.executable}\" \"{main_script}\" %*"
        path = Path("C:\\Windows\\rlibs.bat")
        path.write_text(text)


   

