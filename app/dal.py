from connection import get_collection

coll = get_collection()

class dal:
    
    # q1
    @staticmethod
    def get_engineering_high_salary_employees():
        p = {"employee_id": 1, "name": 1, "salary": 1, "_id": 0}

        q = {"job_role.department": "Engineering", "salary": {"$gt": 65000}}

        return list(coll.find(q, p))


    # q2
    @staticmethod
    def get_employees_by_age_and_role():
        projection = {"_id": 0}

        query = {
            "age": {"$gte": 30, "$lte": 45},
            "job_role.title": {"$in": ["Engineer", "Specialist"]},
        }

        mycal = coll.find(query, projection)

        return list(mycal)


    # q3
    @staticmethod
    def get_top_seniority_employees_excluding_hr():
        projection = {"_id": 0}

        query = {"job_role.department": {"$ne": "HR"}}

        mycal = coll.find(query, projection).sort("years_at_company", -1).limit(7)

        return list(mycal)


    # q4
    @staticmethod
    def get_employees_by_age_or_seniority():
        projection = {"employee_id": 1, "name": 1, "age": 1, "years_at_company": 1, "_id": 0}

        query = {"$or": [{"age": {"$gt": 50}}, {"years_at_company": {"$lt": 3}}]}

        mycal = coll.find(query, projection)

        return list(mycal)


    # q5
    @staticmethod
    def get_managers_excluding_departments():
        projection = {"_id": 0}

        query = {
            "job_role.title": {"$eq": "Manager"},
            "job_role.department": {"$ne": "Sales"},
            "job_role.department": {"$ne": "Marketing"},
        }

        mycal = coll.find(query, projection)

        return list(mycal)

    # q6
    @staticmethod
    def get_employees_by_lastname_and_age():
        projection = {"name": 1, "age": 1, "job_role.department": 1, "_id": 0}

        query = {
            "age": {"$lt": 35},
            "$or": [{"name": {"$regex": "Wright$"}}, {"name": {"$regex": "Nelson$"}}],
        }

        mycal = coll.find(query, projection)

        return list(mycal)

