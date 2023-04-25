from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

#   task 1

def test_task1_returns_correct_1():
    response = client.get("/task1/", params={"code":"USD","date":"2022-05-05"})
    assert response.status_code == 200
    assert response.json() == 4.4017

def test_task1_returns_correct_2():
    response = client.get("/task1/", params={"code":"GBP","date":"2023-01-02"})
    assert response.status_code == 200
    assert response.json() == 5.2768

def test_task1_returns_correct_3():
    response = client.get("/task1/", params={"code":"EUR", "date":"2023-01-01"})
    assert response.status_code == 200
    assert response.json() == None

def test_task1_returns_error_wrong_currency():
    response = client.get("/task1/", params={"code":"USS", "date":"2023-01-01"})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Provided wrong currency code."
        }    

def test_task1_returns_error_wrong_currency_format():
    response = client.get("/task1/", params={"code":"US", "date":"2023-01-01"})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Currency codes consist of three letters."
        }

def test_task1_returns_error_wrong_date_format():
    response = client.get("/task1/", params={"code":"USD", "date":"2023"})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Date should follow YYYY-MM-DD"
        }

#   task 2 (values might change as new quotations are added)

def test_task2_returns_correct_1():
    response = client.get("/task2/", params={"code":"USD","N":168})
    assert response.status_code == 200
    assert response.json() == [
            4.1649,
            5.0381
        ]
    
def test_task2_returns_correct_2():
    response = client.get("/task2/", params={"code":"GBP","N":255})
    assert response.status_code == 200
    assert response.json() == [
            5.1958,
            5.7338
        ]
    
def test_task2_returns_correct_3():
    response = client.get("/task2/", params={"code":"EUR","N":192})
    assert response.status_code == 200
    assert response.json() == [
            4.598,
            4.8711
        ]
    
def test_task2_returns_error_wrong_currency():
    response = client.get("/task2/", params={"code":"USS","N":192})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Provided wrong currency code."
        }    
    
def test_task2_returns_error_wrong_currency_format():
    response = client.get("/task2/", params={"code":"US","N":192})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Currency codes consist of three letters."
        }

def test_task2_returns_error_integer_out_of_range():
    response = client.get("/task2/", params={"code":"USD","N":300})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Quotations should be in range 0-255."
        }
    
def test_task2_returns_error_number_not_and_integer():
    response = client.get("/task2/", params={"code":"USD","N":1.1})
    assert response.status_code == 422
    assert response.json() == {
            "detail": [
                {
                    "loc": [
                        "query",
                        "N"
                    ],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer"
                }
            ]
        }
    
#   task 3 (values might change as new quotations are added)

def test_task3_returns_correct_1():
    response = client.get("/task3/", params={"code":"USD","N":192})
    assert response.status_code == 200
    assert response.json() == 0.10040000000000049

def test_task3_returns_correct_2():
    response = client.get("/task3/", params={"code":"GBP","N":255})
    assert response.status_code == 200
    assert response.json() == 0.11439999999999984

def test_task3_returns_correct_3():
    response = client.get("/task3/", params={"code":"EUR","N":168})
    assert response.status_code == 200
    assert response.json() == 0.09740000000000038
    
def test_task3_returns_error_wrong_currency():
    response = client.get("/task3/", params={"code":"USS","N":192})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Provided wrong currency code."
        }    
    
def test_task3_returns_error_wrong_currency_format():
    response = client.get("/task3/", params={"code":"US","N":192})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Currency codes consist of three letters."
        }

def test_task3_returns_error_integer_out_of_range():
    response = client.get("/task3/", params={"code":"EUR","N":300})
    assert response.status_code == 500
    assert response.json() == {
            "detail": "Quotations should be in range 0-255."
        }
    
def test_task3_returns_error_number_not_and_integer():
    response = client.get("/task3/", params={"code":"EUR","N":1.1})
    assert response.status_code == 422
    assert response.json() == {
            "detail": [
                {
                    "loc": [
                        "query",
                        "N"
                    ],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer"
                }
            ]
        }