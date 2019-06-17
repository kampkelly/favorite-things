#!/bin/bash

# make alembic migrations only
MESSAGE="$1"
if [ -z "$MESSAGE" ] 
then
    echo "No migration message..."
else
    alembic revision -m "$MESSAGE"
    echo "Migrations made"
fi
