import google.protobuf as pro2buf
import protobufTest.addressbook_pb2 as addressbook_pb2
import sys
import protobufTest.testCreate_pb2 as userCreate

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME
try:
    person.no_such_field = 1  # raises AttributeError
    person.id = "1234"  # raises TypeError
except AttributeError as e1:
    print("except:",e1)
except TypeError as e2:
    print("except:",e2)
finally:
    print("proto error type test.")
    print("person:")
    print(person)
    print("phone:")
    print(phone)
    print(sys.getsizeof(person))

admin=userCreate.Admin()
admin.Cmd="UserCreate"
admin.U="admin"
admin.P="admin"
NewUser1=admin.newUs.add()
NewUser1.N="ostartj"
NewUser1.P="ostar123"
NewUser1.Level=1

NewUser2=admin.newUs.add()
NewUser2.N="ostartj2"
NewUser2.P="ostar123"
NewUser2.Level=1

print(admin)
print(type(admin))
print("admin.ByteSize():")
print(admin.ByteSize())
