python main.py --project falcon --branch my-branch

### With the command line
``` 
python main.py \
    --location remote \
    --bucket acklen-terraform-state \
    --key falcon/staging \
    --region us-east-1
```

### With Docker
```
sudo docker run --rm -ti -e AWS_ACCESS_KEY_ID=MY_ID -e AWS_SECRET_ACCESS_KEY=MY_SECRET thanos_snap \
    --location remote \
    --bucket acklen-terraform-state \
    --key falcon/staging \
    --region us-east-1
```