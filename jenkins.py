from ec2 import action_jenkins_ec2
import s3
import route53


def ec2_create(name, myname, ami, instance_type):
    jenkins_info = {'action': 'create', 'name': name, 'myname': myname, 'ami': ami, 'instance_type': instance_type}
    action_jenkins_ec2(jenkins_info)

def ec2_list(myname):
    jenkins_info = {'action': 'list', 'myname': myname}
    action_jenkins_ec2(jenkins_info)

def ec2_delete(name, myname):
    jenkins_info = {'action': 'delete', 'name': name, 'myname': myname}
    action_jenkins_ec2(jenkins_info)

def ec2_update(name, myname, status):
    jenkins_info = {'action': 'update', 'name': name, 'myname': myname, 'status': status}
    action_jenkins_ec2(jenkins_info)
