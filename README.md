# s3deploy
Deploy a local folder to an s3 bucket.

If you are uploading a website, make sure you have configured your bucket to host static site.

# Install

`pip install s3deploy`

# How to use

## Set up a config file

Create a json file containing necessary information.
A sample config file is like this:
```
{
  "access_key":"YOUR ACCESS KEY",
  "secret_key":"YOUR SECRET KEY",
  "bucket_name": "YOUR BUCKET",
  "local_folder": "YOUR LOCAL FOLDER",
  "bucket_folder": "YOUR BUCKET FOLDER",
  "region":"YOUR REGION"
}
```

## Upload to bucket

```
from s3deploy import s3deploy

s3deploy.publish("path/to/config_fn")
```