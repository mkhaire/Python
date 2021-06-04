This script will run every time we upload image file on source bucket.
It will try to resize image as thumbnail image.

Steps:

1) Create unique source and destination bucket.
aws s3 mb s3://test-img-up (Source bucket)
aws s3 mb s3://test-img-res (Bucket where resize image will appear)
2) Edit iam.json with source and destination bucket name.
3) Create new role for lambda execution and attached iam.json policy to role for granting required access.
4) We are importing pillow library which is not present so we will need to download it and create zip file of it with lambda function.

$wget https://files.pythonhosted.org/packages/6a/1c/6426906aed9215168f0885f8c750c89f7619d9a10709591d111af44c0b57/Pillow-8.2.0-cp38-cp38-manylinux1_x86_64.whl

$unzip Pillow-8.2.0-cp38-cp38-manylinux1_x86_64.whl
$ zip -r lambda.zip lambda_function.py PIL Pillow.libs

5) Upload lambda.zip in your lambda function.
6) Create environment variable with key as DEST_BUCKET and value of your destination bucket name.