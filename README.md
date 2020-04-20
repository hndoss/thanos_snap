
### With the command line
``` 
python thanos_snap.py \
    --location remote \
    --bucket MYBUCKET \
    --key terraform/state/location.js \
    --region MY_AWS_REGION
```

## Local 
```
python thanos_snap.py \
    --location local \
    --file /home/rto/staging.json \
    --region us-east-1
```

### With Docker
```
sudo docker run --rm -ti -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY hndoss/thanos_snap \
    --location remote \
    --bucket MYBUCKET \
    --key terraform/state/location.js \
    --region MY_AWS_REGION
```