import subprocess

print("=== Live Incident Response Process Check ===")

output = subprocess.getoutput("ps aux")

keywords = ["nc", "bash", "python", "sh", "curl", "wget"]

for line in output.splitlines():
if any(word in line for word in keywords):
print(line)
