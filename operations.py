import base64, hashlib, urllib.parse

def base64_encode(data): return base64.b64encode(data.encode()).decode()
def base64_decode(data): return base64.b64decode(data.encode()).decode()
def hex_encode(data): return data.encode().hex()
def hex_decode(data): return bytes.fromhex(data).decode()
def url_encode(data): return urllib.parse.quote(data)
def url_decode(data): return urllib.parse.unquote(data)
def rot13(data): return data.translate(str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))
def reverse(data): return data[::-1]
def xor(data, key): return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
def replace(data, old, new): return data.replace(old, new)
def md5(data): return hashlib.md5(data.encode()).hexdigest()
def sha1(data): return hashlib.sha1(data.encode()).hexdigest()
def sha256(data): return hashlib.sha256(data.encode()).hexdigest()
def sha512(data): return hashlib.sha512(data.encode()).hexdigest()

OPERATIONS = {
    "base64_encode": base64_encode,
    "base64_decode": base64_decode,
    "hex_encode": hex_encode,
    "hex_decode": hex_decode,
    "url_encode": url_encode,
    "url_decode": url_decode,
    "rot13": rot13,
    "reverse": reverse,
    "xor": xor,
    "replace": replace,
    "md5": md5,
    "sha1": sha1,
    "sha256": sha256,
    "sha512": sha512
}
