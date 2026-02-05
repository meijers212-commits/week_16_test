
# @staticmethod
#     def get_employees_by_age_or_seniority(collection):
#         query = {"$or":[{"age":{"$gt":50}},{"years_at_company":{"$lt":3}}]}
#         projection = {"employee_id":1,"name":1,"age":1,"years_at_company":1,"_id":0}
#         res = collection.find(query,projection)
#         return list(res)