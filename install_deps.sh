#!/bin/bash

# Install dependencies directly with pip
pip3 install Flask==2.2.2 \
    Flask-SQLAlchemy==3.0.3 \
    Werkzeug==2.2.2 \
    Flask-Migrate==3.1.0 \
    Flask-RESTful==0.3.9 \
    importlib-metadata==6.0.0 \
    importlib-resources==5.10.0 \
    ipdb==0.13.9 \
    pytest==7.1.3 \
    faker==14.2.0 \
    SQLAlchemy-serializer

echo "Dependencies installed successfully!"
