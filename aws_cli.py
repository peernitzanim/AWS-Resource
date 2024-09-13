import argparse
import ec2
import s3
import route53

parser = argparse.ArgumentParser(description='Peer CLI for AWS:')

parser.add_argument(
    "--resource",
    required=True,
    choices=["s3", "ec2", "route53"],
    help="Specify the AWS resource to manage (s3, ec2, or route53)"
)

parser.add_argument(
    "--action",
    choices=["list", "create", "delete", "update"],
    help="Specify the action for the resource (list, create, update or delete)",
    required=True
)

parser.add_argument(
    "--myname",
    required=True,
    help="Enter you name for managing"
)
parser.add_argument(
    "--name",
    help="The name of the S3 bucket (required if creating an S3 bucket)"
)

parser.add_argument(
    "--public",
    choices=["yes", "no"],
    help="Whether the S3 bucket should be public (yes or no) if creating"
)

parser.add_argument(
    "--filename",
    help="Path of the file you want to upload"
)

# EC2-specific argument
parser.add_argument(
    "--instance_type",
    choices=["t3.nano", "t4g.nano"],
    help="The instance type for the EC2 instance (required for EC2)"
)

parser.add_argument(
    "--status",
    choices=["stop", "start"],
    help="start or stop the EC2 instance (required for EC2)"
)

parser.add_argument(
    "--ami",
    choices=["ubuntu", "amazon"],
    help="The ami for the EC2 instance"
         " (required for EC2)- latest Ubuntu AMI or the latest Amazon Linux AMI"
)

args = parser.parse_args()

if args.resource == "ec2":
    ec2.action(args)
elif args.resource == "s3":
    s3.action(args)
elif args.resource == "route53":
    route53.action(args)