# Provision Your Device with an x509 create_from_x509_certificate

openssl req -outform PEM -x509 -sha256 -newkey rsa:4096 -keyout device.key -out device.pem -days 30 -extensions usr_cert -addext extendedKeyUsage=clientAuth -subj "/CN={device registration id, a-z,A-Z,- or _, only}"