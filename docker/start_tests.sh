#!/bin/bash
export $(cat .env.tests | xargs)
eval $@
