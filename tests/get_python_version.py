import constants
import subprocess

# file will be created or rewrites on every run
output = subprocess.check_output(constants.COMMAND)
new_file = open(constants.FILENAME, 'wb')
new_file.write(output)
new_file.close()


