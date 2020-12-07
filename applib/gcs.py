import os
from google.cloud import storage as gcs
from google.oauth2 import service_account


ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
KEY_NAME = os.environ.get('RASPIOBSERVER_GCS_CREDENTIALS')
KEY_PATH = os.path.join(ROOT_PATH, 'etc', 'google-cloud', KEY_NAME)
PROJECT_ID = os.environ.get('RASPIOBSERVER_GCS_PROJECT')
BUCKET_NAME = os.environ.get('RASPIOBSERVER_GCS_BUCKET')


def upload(gcs_path, local_path):
    credential = service_account.Credentials.from_service_account_file(KEY_PATH)
    client = gcs.Client(PROJECT_ID, credentials=credential)
    bucket = client.get_bucket(BUCKET_NAME)

    blob_gcs = bucket.blob(gcs_path)
    blob_gcs.upload_from_filename(local_path)



if __name__ == '__main__':
    import sys
    gcs_path = sys.argv[1]
    local_path = sys.argv[2]
    upload(gcs_path, local_path)

