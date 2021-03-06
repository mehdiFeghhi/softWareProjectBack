import unittest

from handler.cours_selection import is_person_professor, is_person_student, is_assignment_education, \
    is_in_period_of_student_course_selection, is_this_permitted_course_ok_for_this_student
from handler.model.modelDB import Student
from user_handler import find_user_by_username_and_password
import pprint

import requests
import json


def test_find_user_by_username_and_password(user_name, password, status):
    data = find_user_by_username_and_password(user_name, password)
    pprint.pprint(data)

    assert data.get('Status') == status


def test_is_this_user_student(user_id, boolean):
    assert is_person_student(user_id) == boolean


def test_is_person_professor(user_id, boolean):
    assert is_person_professor(user_id) == boolean


def test_is_assignment_education(user_id, boolean):
    assert is_assignment_education(user_id) == boolean


def test_is_in_period_of_student_course_selection(user_id, boolean):
    assert is_in_period_of_student_course_selection(user_id) == boolean


def test_is_this_permitted_course_ok_for_this_student(student: Student, list_id_permitted_course, boolean):
    assert is_this_permitted_course_ok_for_this_student(student, list_id_permitted_course) == boolean



def test_is_this_token_is_authentication(token, status):
    url = "http://127.0.0.1:5000/is-authentication"

    payload = ""
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert json.loads(response.json()).get('Status') == status


def test_login(user, password):
    url = "http://127.0.0.1:5000/api/login"

    payload = json.dumps({
        "username": user,
        "password": password
    })
    headers = {
        'Authorization': 'Bearer {{bearer_token}}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())


if __name__ == '__main__':
    pass
    # test_find_user_by_username_and_password('9732527', '1234', 'OK')
    # test_find_user_by_username_and_password('9732527', '4321', 'ERROR')
    # test_find_user_by_username_and_password('sami@gmail.com', '4231', 'OK')
    # test_find_user_by_us9732527ername_and_password('Parsain', '4231', 'OK')
    # test_find_user_by_username_and_password('Hossainy', '4231', 'OK')
    # test_login("9732527", "1234")
    # test_is_this_token_is_authentication(eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MDUyNzk2MCwianRpIjoiNWEwNWIxMTctYmQ5ZC00NGM0LThmMjktNmI5OTUxYjJkZjY3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ijk3MzI1MjciLCJuYmYiOjE2NDA1Mjc5NjAsImV4cCI6MTY0MDYxNDM2MH0.GqmFs_PVMtjdsMjs0RbbQkuUoJvXtX_pV1bVDO8DiFw,'OK')
