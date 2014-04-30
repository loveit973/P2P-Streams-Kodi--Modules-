import os
current_file_path = os.path.dirname(os.path.realpath(__file__))
print current_file_path
livebuffervalue_file = os.path.join(os.path.split(current_file_path)[0],"values","port.txt")
print livebuffervalue_file
print os.path.split(current_file_path)[0]
