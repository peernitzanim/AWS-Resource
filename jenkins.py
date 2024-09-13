from ec2 import action_jenkins_ec2
import s3
import route53


def ec2_create(name, myname, ami, instance_type):
    jenkins_info = {'action': 'create', 'name': name, 'myname': myname, 'ami': ami, 'instance_type': instance_type}
    action_jenkins_ec2(jenkins_info)
    print(jenkins_info)
