#!/usr/bin/env bash

if [[ $(cat /etc/*release*) =~ "Manjaro" ]]; then
    sudo pacman -Syu --noconfirm python-pip
    sudo pacman -Syu --noconfirm tk
fi


python3 -m venv venv 
pip3 install -r requirements.txt 

