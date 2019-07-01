#!/bin/bash

# installing python

if [ !`which python3` ]; then
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

echo "Installing virtualenv"
pip3 install virtualenv

echo "Installing requirements with pip"
pip3 install -r app/server/requirements.txt
echo "Python requirements installed"

echo "Installing nodejs"
# cd ../..
{
    apt-get install curl --yes
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
    nvm install 11.14
    echo "Nodejs installed"
} || {
    echo "Nodejs installation failed"
}

echo "Installing node sass"
npm rebuild node-sass --force
echo "Node sass installed"

echo "Install package.json dependencies"
cd app/client && npm install --versbose
echo "Npm install finished"

echo "Building client"
npm run build
echo "Npm build finished"

echo "Installing nginx"
apt-get install nginx --yes

cd ../..
echo "Copy nginx.conf file"
cp nginx.conf /etc/nginx/nginx.conf

echo "Dependencies script finished"
