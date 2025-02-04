import parser
import appUi
import validify_commands

import shutil
import os

# Validify commands are all correcly defined
validify_commands.validify_commands()

with open("scripts/chatgpt2.scrtxt", "r") as f:
    code = f.read()
    f.close()

project_file = os.path.normpath('generated_projects/program.sb3')

shutil.copyfile('static/start.sb3', 'generated_projects/program.sb3')
shutil.copyfile('static/logs.txt', 'generated_projects/logs.txt')
project_parser = parser.project(project_file)

project_parser.add_sprite_scripts("S1", code)
project_parser.write(project_file)

appUi.open_sb3_TW(project_file)