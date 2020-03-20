from python_terraform import *
import os
import shutil

cwd = os.getcwd()
print(cwd)
tf = Terraform(working_dir=cwd)
tf.init(capture_output=False)
tf.destroy(capture_output=False)
dir_path = cwd+'/.terraform'
try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))
os.remove('terraform.tfstate')