from string import Template
import json

# This will contain any data needed for template substitution
substituteData = {}

# Load all the writer programs into a variable
with open('writer-programs.json', 'r') as f:
  writerProgramsJSON = sorted(json.load(f), key=lambda program: program['name'].lower())

# Generate the list of writer programs
writerPrograms = ''
for program in writerProgramsJSON:
  writerPrograms = writerPrograms + """- [{name}]({link}) - {rate}
  > {description}

""".format(name=program['name'], link=program['link'], rate=program['rate'], description=program['description'])

# Substite variable in template
with open('README.md.tpl', 'r') as f:
  src = Template(f.read())
  result = src.substitute({
    'writerPrograms': writerPrograms
  })
  with open('README.md', 'w') as readme:
    readme.write(result)
