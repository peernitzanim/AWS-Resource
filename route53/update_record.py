import boto3


def update_record(hosted_zone_id, name_record, name_host_zone, ip):
    client = boto3.client('route53')
    name_record_new = name_record + "." + name_host_zone
    response = client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id
    )
    for record in response['ResourceRecordSets']:
        if name_record_new + "." in record['Name']:
            print("the record exists:" + record['Name'])
            response = client.change_resource_record_sets(
                ChangeBatch={
                    'Changes': [
                        {
                            'Action': 'UPSERT',
                            'ResourceRecordSet': {
                                'Name': name_record_new,
                                'ResourceRecords': [
                                    {
                                        'Value': ip,
                                    },
                                ],
                                'TTL': record['TTL'],
                                'Type': 'A',
                            },
                        },
                    ],
                    'Comment': 'Web Server',
                },
                HostedZoneId=hosted_zone_id,
            )
            print(response)

            break
    else:
        print("The record doesnt exists check yourself")
