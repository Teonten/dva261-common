#!/bin/bash

# Create openssl-"$(hostname)".cnf
cat << EOF > openssl-"$(hostname)".cnf
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

# Details about the issuer of the certificate
[req_distinguished_name]
C = SV
ST = Vastmanland
L = Vasteras
O = DVA261
OU = Projekt
CN = "$(hostname)"

[v3_req]
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

# IP addresses and DNS names the certificate should include
# Use IP.### for IP addresses and DNS.### for DNS names,
# with ### being a consecutive number.
[alt_names]
IP.1 = "$(hostname -I | cut -d' ' -f1)"
DNS.1 = "$(hostname)"
EOF

# Create a PKCS#5 private key and X.509 certificate
openssl version
openssl req -x509 -days 365 -nodes -newkey rsa:2048 -config openssl-"$(hostname)".cnf -keyout pkcs5-plain.pem -out "$(hostname)"-cert.pem

# Convert the PKCS#5 private key into a unencrypted PKCS#8 private key:
openssl pkcs8 -in pkcs5-plain.pem -topk8 -nocrypt -out "$(hostname)"-key.pem

# Set permissions
chmod 640 "$(hostname)"-cert.pem
chmod 600 "$(hostname)"-key.pem
chown 1000:1000 "$(hostname)"-*

# Clean up
rm -rf openssl-"$(hostname)".cnf pkcs5-plain.pem