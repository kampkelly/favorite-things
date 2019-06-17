#!/bin/bash

# run alembic migration only

alembic upgrade head
echo "Done"
