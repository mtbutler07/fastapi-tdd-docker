#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL Started!"

exec "$@"
