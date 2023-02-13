import boto3

BUCKET_NAME = "random-test-file-upload"

s3 = boto3.client("s3")

# list all buckets
# buckets_resp = s3.list_buckets()
# for bucket in buckets_resp["Buckets"]:
#     print(bucket)

# list all objects in a bucket
# response = s3.list_objects_v2(Bucket=BUCKET_NAME)
# for obj in response["Contents"]:
#     print(obj)

# upload file
# with open('./brain-map.jpg', 'rb') as f:
#     s3.upload_fileobj(
#         f,
#         BUCKET_NAME,
#         'upload_by_boto.jpg',
#         ExtraArgs={"ACL": "public-read"}
#     )

# download file
# s3.download_file(BUCKET_NAME, "upload_by_boto.jpg", "download_by_boto.jpg")

# download with binary file
# with open("download_by_binary.jpg", "wb") as f:
#     s3.download_fileobj(BUCKET_NAME, "upload_by_boto.jpg", f)

# presigned URL to give limited access to an unauthorized user
# url = s3.generate_presigned_url("get_object",
#                                 Params={"Bucket": BUCKET_NAME, "Key": "never-forget-limited-access.jpg"},
#                                 ExpiresIn=10
#                                 )
# print(url)

# bucket create
# bucket_location = s3.create_bucket(ACL="public-read", Bucket="New_Bucket")
# print(bucket_location)

# copy object
# s3.copy_object(
#     ACL="public-read",
#     Bucket="new-bucket",
#     CopySource=f"/{BUCKET_NAME}/my_image.jpg",
#     Key="CopiedImg.jpg"
# )

# get object
# response = s3.get_object(Bucket=BUCKET_NAME, Key='upload_by_boto.jpg')
# print(response)
