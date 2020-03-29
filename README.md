python main.py --project falcon --branch my-branch

### With the command line
``` 
python thanos_snap.py \
    --location remote \
    --bucket acklen-terraform-state \
    --key falcon/53-test-coverage/backend.json \
    --region us-east-1
```

## Local 
```
python thanos_snap.py \
    --location local \
    --file /path/to/my/terraform/state \
    --region us-east-1
```

### With Docker
```
sudo docker run --rm -ti -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY hndoss/thanos_snap \
    --location remote \
    --bucket acklen-terraform-state \
    --key falcon/186-all-guests-list-alphabetically-sorting-not-taking-lowercase-profiles-into-consideration \
    --region us-east-1
```