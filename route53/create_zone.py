import boto3
import datetime

x = datetime.datetime.now()
route53 = boto3.client('route53')
response = route53.create_hosted_zone(
    Name='peer1.peer-test-2',
    VPC={
        'VPCRegion': 'us-east-1',
        'VPCId': 'vpc-01fa3051c3f32df2e'
    },
    CallerReference=str(x),
    HostedZoneConfig={
        'Comment': 'test',
        'PrivateZone': True
    }
)

hosted_zone_id = response['HostedZone']['Id'].split('/')[-1]

response = route53.change_tags_for_resource(
    ResourceType='hostedzone',
    ResourceId=hosted_zone_id,
    AddTags=[
        {
            'Key': 'MyName',
            'Value': 'peer'
        },
    ]
)