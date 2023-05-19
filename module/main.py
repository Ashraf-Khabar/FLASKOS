from __db__ import Connect
from __field__ import Field
from __model__ import Model

# Creating the table with the same name "user":
    
class Users(Model):
    id = Field("id", "NUMBER", primary_key=True)
    name = Field("name", "VARCHAR2(100)", nullable=False)
    role_id = Field("role_id", "NUMBER", foreign_key=("roles", "id"))

class Roles(Model):
    id = Field("id", "NUMBER", primary_key=True)
    name = Field("name", "VARCHAR2(100)", nullable=False)
    
def main():
    Roles.create_table()
    Users.create_table()

if __name__ == "__main__":
    main()
