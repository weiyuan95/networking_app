#!/bin/bash
cd ..
pipenv run gunicorn --bind 0.0.0.0:5000 app:app </dev/null &>/dev/null &