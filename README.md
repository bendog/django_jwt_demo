# Django JWT Demo

## references

Getting DRF setup  
<https://www.django-rest-framework.org/tutorial/quickstart/>

Setting up JWT authentication for Django + DRF  
<https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html>

## Install packages

### with pipenv

1. in this directory, run `pipenv install`
1. activate the environment with `pipenv shell`

### with pip and virtualenv

1. in this directory setup a new virtual environment run `python3 -m venv .venv`
1. activate that virtual environment `source ./.venv/bin/activate` on mac/linux
1. install pip packages with `pip install -U -r requirements.txt`

## setup database

    (.venv)$ cd project
    (.venv)$ python manage.py migrate
    (.venv)$ python manage.py loaddata data.json

## run dev server

    (.venv)$ python manage.py runserver


## Accessing the resources

### authenticating 

run this in your terminal to authenticate
```
curl --request POST \
  --url http://127.0.0.1:8000/api/token/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "bendog",
	"password": "meowmeow"
}'
```

you should get a response like this
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDU3MTg3MCwianRpIjoiNGRmMzQ1ZDcwZmEyNDRiZTg4MzRkY2ZjMTVkN2FmZjMiLCJ1c2VyX2lkIjoxfQ.VMLqAZL4mqUBgmh3Hqg0NOgm2XyI8D9htjfccM1UO1I",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI"
}
```

**Make sure to copy the value of "access", you will need this to access all future resources**

### listing users

```
curl --request GET \
  --url http://127.0.0.1:8000/app/users/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI'
```

### listing profiles

```
curl --request GET \
  --url http://127.0.0.1:8000/app/profiles/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI'
```

### retrieving a specific url

```
curl --request GET \
  --url http://127.0.0.1:8000/app/profiles/2/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI' \
  --header 'content-type: application/json'
```

### updating a specific profile

```
curl --request PATCH \
  --url http://127.0.0.1:8000/app/profiles/2/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI' \
  --header 'content-type: application/json' \
  --data '{
	"nick_name": "choose goose"
}'
```

### create a new user

```
curl --request POST \
  --url http://127.0.0.1:8000/app/users/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDg1NzcwLCJqdGkiOiI2ZjcyY2RmYzAxN2E0NDc4ODFiMjdhNWY5NjEyNzMyOCIsInVzZXJfaWQiOjF9.W1Ph-VsaoXeHIJEQmv3Y1zs-_Ja9HHAmlQCiUz4cmfI' \
  --header 'content-type: application/json' \
  --data '{
	"username": "test3",
	"password": "moomoomoo",
	"email": "cow@nope.com",
	"first_name": "test",
	"last_name": "cow"
}'
```


