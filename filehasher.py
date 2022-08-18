import hashlib

def sha256_file(content=None):
    if content is None:
        return ''
    sha256gen = hashlib.sha256()
    with open(content, mode = 'rb') as fd:
        data = fd.read()
    sha256gen.update(data)
    sha256code = sha256gen.hexdigest()
    sha256gen = None
    return sha256code

#if __name__ == '__main__':
#    gen = sha256_file("test.txt")
#    print(gen)