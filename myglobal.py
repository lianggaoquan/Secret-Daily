from Crypto.Cipher import DES
key = 'jsfghutp'
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text
cipher = DES.new(key, DES.MODE_ECB)