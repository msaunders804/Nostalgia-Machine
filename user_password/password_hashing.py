'''
Bryan Coleman
'''

from hashlib import sha256

def hash_password(pw):
    return sha256(pw.encode())
