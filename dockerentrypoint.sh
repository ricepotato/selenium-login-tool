#!/bin/bash

gunicorn app:app --bind 0.0.0.0:8080 --graceful-timeout 60