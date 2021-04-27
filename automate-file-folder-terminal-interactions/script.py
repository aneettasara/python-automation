import subprocess

for i in range(5):
    # runs example.py in this loop
    subprocess.check_call(['python','example.py'])