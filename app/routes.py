from fastapi import APIRouter
from dal import dal
from connection import trigger_insert

router = APIRouter()

# q0
@router.get('/insert_data')
def insert_data():
    return trigger_insert()

# q1
@router.get('/employees/by-age-and-role')
def get_employees_by_age_and_role():
    return dal.get_employees_by_age_and_role()
# q2
@router.get('/employees/engineering/high-salary')
def get_employees_engineering_high_salary():
    return dal.get_engineering_high_salary_employees()
# q3
@router.get('/employees/top-seniority')
def get_employees_top_seniority():
    return dal.get_top_seniority_employees_excluding_hr()
# q4
@router.get('/employees/age-or-seniority')
def get_employees_age_or_seniority():
    return dal.get_employees_by_age_or_seniority()

# q5
@router.get('/employees/managers/excluding-departments')
def get_employees_managers_excluding_departments():
    return dal.get_managers_excluding_departments()

@router.get('/employees/by-lastname-and-age')
def get_employees_by_lastname_and_age():
    return dal.get_employees_by_lastname_and_age()