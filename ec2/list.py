import boto3


def list_instances(ec2_myname, info) -> list:
    list_of_instances = []
    if info == "cli":
        ec2_myname = ec2_myname + " cli"
    elif info == "app":
        ec2_myname = ec2_myname + " app"
    else:
        ec2_myname = ec2_myname + " Jenkins"
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        if instance.state['Name'] == "running" or instance.state['Name'] == "stopped":
            name = ""
            myname = ""
            for tags in instance.tags:
                if tags['Key'] == 'MyName':
                    myname = tags['Value']
                if tags['Key'] == 'Name':
                    name = tags['Value']
            if myname == ec2_myname:
                list_of_instances.append(name)
    print(list_of_instances)
    return list_of_instances
