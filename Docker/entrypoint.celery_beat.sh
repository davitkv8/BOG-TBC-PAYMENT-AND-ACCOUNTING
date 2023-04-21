#!/bin/sh

# wait for django proj to start
wait-for-it -t 30 -s swissCap__app:8000

celery -A app:celery_app beat -l INFO