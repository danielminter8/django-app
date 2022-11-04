# export POSTGRES_NAME=postgres
# export POSTGRES_USER=
# export POSTGRES_PASSWORD=
# export POSTGRES_HOST=
echo -- staring up server --
pip3 freeze > requirements.txt
python3 manage.py makemigrations purchase_sale_api
python3 manage.py migrate
python3 manage.py runserver 8080