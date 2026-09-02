with open('buildozer.spec', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip().startswith('requirements ='):
        new_lines.append('requirements = kivy\n')
    else:
        new_lines.append(line)

with open('buildozer.spec', 'w') as f:
    f.writelines(new_lines)

print("Spec requirements updated!")
