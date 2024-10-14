import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize the S3 client
s3_client = boto3.client('s3')

def create_bucket(bucket_name, region=None):
    try:
        # If a region is specified, create the bucket in that region
        if region is None:
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )

        print(f"Bucket {bucket_name} created successfully")
        return response
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Error: {e}")

# Call the create_bucket function
bucket_name = "new-bucket-28-09-2024"  # Ensure bucket name is unique
region = "ap-south-1"  # Change to your desired region

create_bucket(bucket_name, region)
