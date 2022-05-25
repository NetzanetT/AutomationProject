import requests
import pytest
import jsonpath


class Test_Login:

    def test_login_correctly_when_insert_exist_Password_and_Email(self):
        url= "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"hhh@walla.com","password":"1234567"}
        res= requests.post(url, data= body)
        assert res.status_code == 200
        json= res.json()
        assert json['message'] == "login successful"
        assert json['success'] == True
        assert json ['token'] is not None


    def test_login_incorrectly_when_email_isNumbers(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "123456", "password": "1234567"}
        res = requests.post(url, data=body)
        assert res.status_code == 400
        json = res.json()
        assert json['message'] == "no user found"
        assert json ['success'] == False


    def test_login_inccorectly_when_fieldsNULL(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "", "password": ""}
        res = requests.post(url, data=body)
        assert res.status_code == 400
        assert res.elapsed.total_seconds()< 3
        json = res.json()
        assert json['message'] == "password or email incorrect"
        assert json ['success'] == False


    def test_login_incorrectly_when_password_isNULL(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "hhh@walla.com", "password": ""}
        res = requests.post(url, data=body)
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 2

    def test_register_incorrectly_when_insert_exist_email(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email":"hhh@walla.com","password":"12345","name":"tt","lastName":"tt","birthDate":"1980-09-17"}
        res = requests.post(url, data=body)
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 3
        json= res.json()
        assert json['message']== "user with that email already exists"
        assert json['success']== False


    def test_regiester_incorrectly_when_insert_onlyEmail(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "", "name": "", "lastName": "","birthDate": ""}
        res = requests.post(url, data=body)
        assert res.status_code == 500
        assert res.elapsed.total_seconds() <5
        json = res.json()
        assert json['message'] == "User validation failed: name: Path `name` is required., lastName: Path `lastName` is required., birthDate: Path `birthDate` is required."
        assert json['success'] == False

    def test_regiester_incorrectly_when_insert_onlyEmail_andName(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "", "name": "netza", "lastName": "", "birthDate": ""}
        res = requests.post(url, data=body)
        assert res.status_code == 500
        assert res.elapsed.total_seconds() < 3
        json = res.json()
        assert json['message']== "User validation failed: lastName: Path `lastName` is required., birthDate: Path `birthDate` is required."
        assert json['success'] == False

    def test_regiester_incorrectly_when_insert_onlyEmail_Birthdate_andLastname(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "", "name": "", "lastName": "tad", "birthDate": "1980-08-19"}
        res = requests.post(url, data=body)
        assert res.status_code == 500
        assert res.elapsed.total_seconds()<3
        json = res.json()
        assert json['message']== "User validation failed: name: Path `name` is required."
        assert json['success']== False


    def test_regiester_incorrectly_when_insert_onlyEmail_Birthdate_Lastname_andPassword(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "123456", "name": "", "lastName": "tad", "birthDate": "1980-07-19"}
        res = requests.post(url, data=body)
        json = res.json()
        assert res.status_code == 500
        assert json['message'] == "User validation failed: name: Path `name` is required."
        assert json['success'] == False
        assert res.elapsed.total_seconds()<2

    def test_regiester_incorrectly_when_insert_onlyEmail_Birthdate_name_andPassword(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "123456", "name": "jjk", "lastName": "", "birthDate": "1980-07-19"}
        res = requests.post(url, data=body)
        json = res.json()
        assert json['message'] == "User validation failed: lastName: Path `lastName` is required."
        assert json['success'] == False
        assert res.status_code == 500
        assert res.elapsed.total_seconds()<3


    def test_regiester_incorrectly_when_insert_onlyEmail_Birthdate_andPassword(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": "nn@walla.com", "password": "123456", "name": "", "lastName": "", "birthDate": "1980-07-19"}
        res = requests.post(url, data=body)
        json = res.json()
        assert json['message'] == "User validation failed: name: Path `name` is required., lastName: Path `lastName` is required."
        assert json['success'] == False
        assert res.status_code == 500
        assert res.elapsed.total_seconds()<3

    def test_regiester_incorrectly_when_insert_onlyName_lastName_Birthdate_andPassword(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": " ", "password": "123456", "name": "nium", "lastName": "sksk", "birthDate": "1980-07-19"}
        res = requests.post(url, data=body)
        json = res.json()
        assert json['message']== "User validation failed: email: Path `email` is invalid ( )."
        assert json['success'] == False
        assert res.status_code == 500
        assert res.elapsed.total_seconds() < 3

    def test_regiester_incorrectly_when_insert_onlyName_lastName_Birthdate(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"email": " ", "password": "   ", "name": "nium", "lastName": "sksk", "birthDate": "1980-07-19"}
        res = requests.post(url, data=body)
        json = res.json()
        assert res.status_code == 500
        assert res.elapsed.total_seconds()<3
        assert json['message'] == "User validation failed: email: Path `email` is invalid ( )."
        assert json['success'] == False
        print(res.text)




























