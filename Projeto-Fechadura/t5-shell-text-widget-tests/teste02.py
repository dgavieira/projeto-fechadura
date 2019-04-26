import subprocess

path = "python3 fpsim.py"
process = subprocess.Popen(path.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(stdout)