import subprocess
subprocess.run(["ls", "-al"])
subprocess.run(["git", "status"])

import subprocess
subprocess.Popen(["ls", "-al"])
subprocess.Popen(["/usr/bin/git", "status"])

import os
os.system("ls -al")
os.system("git status")