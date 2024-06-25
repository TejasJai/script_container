import base64

# Encoded keys
access_key = "Q3AM3UQ867SPQQA43P2F"
secret_key = "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG"

# Decode base64
decoded_access_key = base64.b64decode(access_key).decode('latin-1')
decoded_secret_key = base64.b64decode(secret_key).decode('latin-1')

print("Decoded Access Key:", decoded_access_key)
print("Decoded Secret Key:", decoded_secret_key)

