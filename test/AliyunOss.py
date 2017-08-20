# -*- coding: utf-8 -*-
import oss2
import sys

endpoint = 'http://oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('xxx', 'xxx')
bucket = oss2.Bucket(auth, endpoint, 'xxx')


# -*- parameters -*-
args = sys.argv

keys = ['SBC.war', 'spider-web.war', 'test.txt']
paths = ['/opt/apache-tomcat-7.0.63/webapps', '/opt/spider', '.']
kp = dict(zip(keys, paths))


# # upload
def upload(key, path):
    print('-*- Uploading: {0}'.format(key))
    bucket.put_object_from_file(key, path + '/' + key)


# # download
def download(key):
    print('-*- Downloading: {0}'.format(key))
    bucket.get_object_to_file(key, '/tmp' + '/' + key)


# # list files on OSS
def list_objects():
    print("-*- Files on OSS: -*-")
    for object_info in oss2.ObjectIterator(bucket):
        k = object_info.key
        t = bucket.get_object(object_info.key).headers['Last-Modified']
        print('{0} \t -*- \t {1}'.format(k, t))


# # prepare for args
def prepare():
    if len(args) == 1:
        print("## No arguments.")
        sys.exit(1)
    elif len(args) == 2:
        print("## 2 arguments needed, only got 1 input.")
        sys.exit(1)
    elif len(args) == 3:
        pass
    else:
        print("## Too many arguments.")
        sys.exit(1)


# # ============================================
if __name__ == "__main__":
    prepare()

    action = args[1]
    key = args[2]
    path = kp[key]

    if action == "upload":
        upload(key, path)
    elif action == "download":
        download(key)
    else:
        print("## Wrong action.")
        
    list_objects()

