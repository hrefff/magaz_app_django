# stop and delete docker container
docker rm -f magaz

# build container
docker build --tag magaz:latest .

# run container
docker run --name magaz -d -p 8000:8000 magaz:latest

# show container
docker ps -f "name=magaz"

# collect static
docker exec -it magaz sh -c "python manage.py collectstatic --no-input"

# create migrations
docker exec -it magaz sh -c "python manage.py makemigrations"

# accept
docker exec -it magaz sh -c "python manage.py migrate"
