import oss2

key = 'spider-web.war'
path = '/opt/spider/'

endpoint = 'http://oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('VWIA4F2xUcVQJ8gW', 'FSXJEAXi6ug6R3BwzxRej9wPbBXDRP')
bucket = oss2.Bucket(auth, endpoint, 'caiexdeploy')

# # upload
#print("-*- Downloading ... -*-")
#bucket.put_object_from_file(key, path+key)

# # download
print("-*- Downloading ... -*-")
bucket.get_object_to_file(key, '/tmp/'+key)
#bucket.delete_object(key)

print("-*- Files on OSS: -*-")
for object_info in oss2.ObjectIterator(bucket):
    print(object_info.key)
