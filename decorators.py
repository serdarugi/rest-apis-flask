import functools


# user = {"username": "jose", "access_level": "guest"}

# def make_secure(access_level):
#     def decorator(func):
#         # it takes make secure function. 
#         # functools.wraps(func) is used to preserve the metadata of the original function
#         @functools.wraps(func)
#         # secure_function is the function that will be called, also called wrapper function
#         def secure_function(*args, **kwargs):
#             if user['access_level'] == access_level:
#                 return func(*args, **kwargs)
#             else:
#                 return f"No {access_level} permission for {user['username']}"
#         return secure_function
#     return decorator

# # below is the decorator syntax
# @make_secure("admin") ##### get_dashboard = make_secure("guest")(get_dashboard) #####
# def get_admin_password():
#     return "admin : 1234"

# @make_secure("guest")
# def get_guest_password():
#     return "guest : 1234"

# print(get_admin_password())
# print(get_guest_password())


user = {"username" : "serdar", "access_level" : "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def security_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args,**kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"
        return security_function
    return decorator

@make_secure('admin')
def get_admin_password():
    return "admin : Serougur.1706*"

print(get_admin_password())