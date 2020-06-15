import base64
import hashlib

def base64_md5(image):
    d = {}
    string = base64.b64encode(image.read())
    string = string.decode('utf-8')
    d['base64']=string
    hash_obj = hashlib.md5(string.encode())
    md5_hash = hash_obj.hexdigest()
    d['md5_hash']=md5_hash
    return d

if __name__ == '__main__':
    image = open('C:/Users/Mudit/OneDrive/Documents/New folder/django_projects/testing/media/images/cons1.JPG', 'rb')
    print(base64_md5(image))
