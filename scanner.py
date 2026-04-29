with open("/etc/passwd") as f:
for line in f:
if "bash" in line:
print(line.strip())
