mkdir -p secrets
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout secrets/key.pem -out secrets/cert.pem \
-subj /C=PL/ST=mazowieckie/L=Warszawa/O=Organizacja/OU=Jednostka/CN=Nazwa