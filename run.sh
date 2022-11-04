echo -- staring up server --
pip3 freeze > requirements.txt
python3 manage.py makemigrations purchase_sale_api
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080