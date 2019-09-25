import subprocess

process = subprocess.Popen(['lxterminal','-e','python3','fpsim.py'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
stdin, stdout, stderr = process.communicate()
line = process.stdout.readline()
print(line)