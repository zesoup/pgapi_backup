#!/bin/bash

PYTHONPATH=. pytest-3 --cov=pgapi_backup tests --cov-report=html
