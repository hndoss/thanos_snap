from python_terraform import *
import sys
import os
import shutil
import argparse


# python main.py --project falcon --branch my-branch --location local

def parse_arguments():
    # print(str(sys.argv))
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--branch', metavar='N', type=str, nargs='+',
                   help='an integer for the accumulator')

    parser.add_argument('--project', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

    parser.add_argument('--location', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

def main():
    print('testing')
    parse_arguments()
    os.chdir('local/')

    cwd = os.getcwd()
    print(cwd)
    tf = Terraform(working_dir=cwd)
    tf.init(capture_output=False)
    # tf.destroy(capture_output=False, var={'access_key': '', 'secret_key': '', 'aws_region': ''})
    dir_path = cwd+'/.terraform'
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
    os.remove('terraform.tfstate')


main()


  terraform apply -var='a=b' -var='c=d'
  --> tf.apply(var={'a':'b', 'c':'d'})