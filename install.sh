#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Installation terminée ! Lance l'application avec : source .venv/bin/activate && python main.py"