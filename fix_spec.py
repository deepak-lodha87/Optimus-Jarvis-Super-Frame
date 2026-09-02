with open('buildozer.spec', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip().startswith('source.include_exts ='):
        new_lines.append('source.include_exts = py,png,jpg,kv,atlas\n')
    elif line.strip().startswith('source.exclude_dirs ='):
        new_lines.append('source.exclude_dirs = tests, bin, storage, .git\n')
    else:
        new_lines.append(line)

with open('buildozer.spec', 'w') as f:
    f.writelines(new_lines)

print("Spec file configured to exclude heavy storage folders!")
