import json
from string import Template

substituteData = {}

writerPrograms = ''
with open('writer-programs.json', 'r') as f:
  writerPrograms = json.load(f)

writerPrograms = sorted(writerPrograms, key=lambda program: program['name'].lower())

programsPrint = ''
for program in writerPrograms:
  programsPrint = programsPrint + """- [{name}]({link}) - {rate}
  > {description}

""".format(name=program['name'], link=program['link'], rate=program['rate'], description=program['description'])

substituteData['writerPrograms'] = programsPrint

# print(json.dumps(writerPrograms, sort_keys=False, indent=2))

with open('README.md.tpl', 'r') as f:
  src = Template(f.read())
  result = src.substitute(substituteData)
  with open('README.md', 'w') as readme:
    readme.write(result)
