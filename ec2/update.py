import boto3


def change_status_instances(status, instance_id) -> str:
    client = boto3.client('ec2')
    if status == "start":
        response = client.start_instances(InstanceIds=[instance_id])
        return "start the instance"
    else:
        response = client.stop_instances(InstanceIds=[instance_id])
        return "stop the instance"
