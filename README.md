# raspiobserver
RaspBerry Pi App


## Setup
```
$ git clone git@github.com:tayutaedomo/raspiobserver.git
```

### pip install
```
$ pip3 install google-cloud-storage==1.33.0
```


## crontab
```
$ crontab -e

RASPIOBSERVER_ROOT=<Root directory path>
5 * * * * $RASPIOBSERVER_ROOT/scripts/export_temperature_metrics.py >> /dev/null 2>&1
10 * * * * $RASPIOBSERVER_ROOT/scripts/export_hardware_metrics.py >> /dev/null 2>&1

export RASPIOBSERVER_GCS_CREDENTIALS=<Credentials file name>
export RASPIOBSERVER_GCS_PROJECT=<Project ID>
export RASPIOBSERVER_GCS_BUCKET=<Bucket name>
15 0 * * * $RASPIOBSERVER_ROOT/scripts/upload_temperature_metrics.py >> /dev/null 2>&1
```

