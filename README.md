# My App Django

Student Django project (Magaz app)

## Run on Docker
0. clone repo
```bash
git clone git@github.com:hrefff/magaz_app_django.git
cd magaz_app_django
```

1. run deploy script
```bash
./deploy.sh
```

## Run for development

0. clone repo
```bash
git clone git@github.com:hrefff/magaz_app_django.git
cd magaz_app_django
```

1. Install pyenv (if not installed)
```bash
curl https://pyenv.run | bash
```

2. Install needed python version (3.10)
```bash
pyenv install 3.10
pyenv local 3.10
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Collect static files
```bash
python manage.py collectstatic --no-input
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run server
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)