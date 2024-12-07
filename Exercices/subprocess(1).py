import subprocess
import os

# Run a terminal command
# result = subprocess.run(['ls'], capture_output=True, text=True)  # For Linux/MacOS

command=input('enter yout command : ').strip()

result = subprocess.run([command], capture_output=True, text=True, shell=True) 

# Print the command output
print(result.stdout)



# Open an interactive process
process = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

# Send input to the process
process.stdin.write('print("Hello from Python Terminal!")\n')
process.stdin.flush()

# Read the output
output = process.stdout.readline()
print(output)


import os

# Run a command
os.system('echo "Hello from the terminal!"')
