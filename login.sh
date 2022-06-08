#!/bin/bash
STRING="Hello Populix! I'm Tito Valiant"
echo $STRING

echo This is Login Function
# Ask the user for login details

read -p 'Username: ' uservar
read -p 'Password: ' passvar
echo

if [ "$uservar" = 'qa' ] && [ "$passvar" = 'engineer' ]; then
        echo "Login Success"
    else
        echo "Login Failed"
fi
sleep 2
