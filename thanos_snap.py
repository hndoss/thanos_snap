from python_terraform import Terraform
from thanos_banners import *
from shutil import copyfile
import argparse
import os


def validate_context(args):
    parser = argparse.ArgumentParser()

    if args.region is None:
        parser.error('--region argument is obligatory.')

    if args.location == 'remote' and (args.bucket is None or args.key is None or args.region is None):
        parser.error(
            '--location=remote requires --bucket, --region and --key arguments.')

    if args.location == 'local' and (args.file is None):
        parser.error(
            '--location=local requires --file argument')

    if 'AWS_ACCESS_KEY_ID' in os.environ and 'AWS_SECRET_ACCESS_KEY':
        pass
    else:
        parser.error('Missing AWS credentials as environment variables.')

    return True


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Destroy Terraform infrastructure with Thanos.')

    parser.add_argument('--location', choices=['local', 'remote'],
                        type=str, help='Where is the terraform.tfstate to be destroyed.')
    parser.add_argument('--bucket', type=str,
                        help='The bucket in AWS S3 where is the terraform.tfstate located.')
    parser.add_argument('--key', type=str,
                        help='The bucket directory where is the terraform.tfstate located.')
    parser.add_argument('--region', type=str,
                        help='The region where the AWS S3 bucket is located.')
    parser.add_argument('--file', type=str,
                        help='Path to the terraform.tfstate.')

    args = parser.parse_args()

    return args


def init_terraform(dir='.', backend_config=''):
    tf = Terraform(working_dir=dir)
    tf.init(capture_output=False, backend_config=backend_config)
    return tf


def destroy_local_environment(region='', file=''):
    print('Destroying local terraform state.')
    current_directory = os.getcwd()
    try:
        copyfile(file, current_directory + '/local')
    except:
        print('An error occured with the file ' + file)
    tf = init_terraform('local')
    tf.destroy(capture_output=False, vars={'aws_region': region})


def destroy_remote_environment(bucket='', key='', region=''):
    print('Destroying remote terraform state.')
    config = {
        'key': key,
        'bucket': bucket,
        'region': region
    }
    tf = init_terraform('remote', backend_config=config)
    tf.destroy(capture_output=False, vars={'aws_region': region})


def main():
    args = parse_arguments()
    validate_context(args)

    print_thanos_banner_before_snap()

    if args.location == 'remote':
        destroy_remote_environment(
            bucket=args.bucket, key=args.key, region=args.region)
    else:
        destroy_local_environment(region=args.key, file=args.file)

    print_thanos_banner_after_snap()


main()
