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

echo "Installing nodejs"
{
    apt-get install curl --yes
    curl -sL https://deb.nodesource.com/setup_11.x | bash
    apt-get install nodejs --yes
} || {
    echo "Nodejs installation failed"
}

echo "Installing node sass"
npm rebuild node-sass --force
echo "Node sass installed"

echo "Installing package.json dependencies"
cd app/client && npm install

echo "Npm install finished"
