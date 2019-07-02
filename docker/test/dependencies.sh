#!/bin/bash

# installing python

if [ !`which python3.7` ]; then
    echo "...installing python ..."
    { 

        apt-get update -y
        apt-get install python3.7 -y
        echo "Installing Pip"
        apt-get install python3-pip --yes
        echo "Python 3.7 installed"
        echo "Pip installed"
    } || {
        echo "python3.7 installation failed pease install manually"
        exit 1
    }
else
        echo "python3.7 found."
fi

echo "Installing requirements with pip"
pip3 install -r app/server/requirements.txt
echo "Python requirements installed"
