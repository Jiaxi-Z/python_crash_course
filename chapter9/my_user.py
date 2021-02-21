from user import User
from privileges import Privileges
from admin import Admin

fang = Admin("jie", "mei")
fang.describe_user()
fang.greet_user()
fang.privileges.show_privileges()
