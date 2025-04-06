#!/bin/bash

echo "Running auth service migrations..."
alembic upgrade head 