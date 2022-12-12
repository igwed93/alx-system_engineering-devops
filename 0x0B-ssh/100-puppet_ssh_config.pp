#!/usr/bin/env bash

# configure ssh client to use private key and refuse
# password authentication

Host 50998-web-01
    HostName 54.157.182.63
    User    ubuntu
    IdentityFile    ~/.ssh/school
    PasswordAuthentication  no
