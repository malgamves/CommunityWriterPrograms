import json
import sys

with open('writer-programs.json', 'r') as f:
  programs = sorted(json.load(f), key=lambda program: program['name'].lower())

name = input("Name of company: ")
link = input("Link to Writer Program: ")
rate = input("Pay rate: ")
description = input("Describe the Writer Program: ")

program = {
  'name': name,
  'link': link,
  'rate': rate,
  'description': description,
}
programs.append(program)

with open('writer-programs.json', 'w') as f:
  programsSorted = sorted(programs, key=lambda program: program['name'].lower())
  f.write(json.dumps(programsSorted,indent=2))