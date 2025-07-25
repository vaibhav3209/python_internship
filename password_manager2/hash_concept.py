import hashlib
from getpass import getpass
#USE ENCODE()
# dobara bhi same password likhrnge to same hash banake dega
# vaib123
# 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
#vaib1234
# 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
#malav123
# 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
def create_password(password):

    # initialize the algo
    hash_object = hashlib.sha256()

    #it is a byte string
    # password = b"vaib123"
    hash_object.update(password)

    res = hash_object.hexdigest()
    # print("password",res)
    return res

def main():
    user_pass = getpass("enter pass:")
    # user_pass = b"user_pass"              #****very imp... ye string user_pass ko encode kar
                                                # rha hia use encode()

    #bytes string mein daalna padega password variable
    user_pass = user_pass.encode()
    get_pass = create_password(user_pass)
    print("cureent password is:",get_pass)
    print(type(get_pass))


if __name__ == '__main__':
    main()