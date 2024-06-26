import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def download_file_from_s3(bucket_name, s3_key, local_file_name):
    try:
        print(f'Start download {s3_key} from {bucket_name} to {local_file_name}')
        
        # Create an S3 client
        s3_client = boto3.client('s3')

        # Download the file from S3
        s3_client.download_file(bucket_name, s3_key, local_file_name)
        print(f'Successfully downloaded {s3_key} from {bucket_name} to {local_file_name}')
    except NoCredentialsError:
        print('No credentials provided.')
    except PartialCredentialsError:
        print('Incomplete credentials provided.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    # Define your S3 bucket and file details
    bucket_name = 'vf-library-access-76-gws1r47z5sfwewnwp4hubt3fmmihause2b-s3alias'
    s3_key = 'Enamine_REAL_Space_2022q12/c1/3c/Enamine_REAL_Space_2022q12-sparse/pdbqt/SPARSE10/0000978.tar.gz'
    local_file_name = 'downloadedfile.tar.gz'

    # Download the file
    download_file_from_s3(bucket_name, s3_key, local_file_name)
