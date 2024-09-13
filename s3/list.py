import boto3


def list_buckets(buckets) -> None:
    for bucket in buckets:
        print(bucket)
