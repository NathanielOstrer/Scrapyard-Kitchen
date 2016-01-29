f = open('linkstorecipes.html')
lines = f.readlines()

lines = [line[line.index('<a href="') + len('<a href="'):-2] for line in lines if '<a href="/recipes' in line]

output = open('justlinks.html', 'w')

good = []

for line in lines:
	if not line in good:
		good.append(line)

for line in good:
	output.write(line)
	output.write('\n')

output.close()
