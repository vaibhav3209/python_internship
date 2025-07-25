import sqlite3
# import hashlib
from hash_concept import create_password
# status = 'not specified'

# print('''WELCOME USERNAME ''')   jab login ho jae tab doobara name print karana
def main():
    while True:
        print('''
                1. CREATE AN ACOOUNT 
                2. ALREADY HAVE ACCOUNT LOGIN / LOGOUT
                3. EXIT 
                ''')

        # print ka code bhi choice mein likh sakte
        choice = int(input())

        match choice:
            case 1:
                # *********to do: check if username already exists tab naya naam daalna *********

                username = input('enter username to store : ')
                text_password = input('enter  your password :')

                #convert pass into hash using hash_concept file

                #NOTE ISS PASSWORD KO BYTE STRING MEIN BANAKE BHEJNA .........TYOE ERROR DEGA THAT
                # 'STRINGS MUST BE ENCODED BEFORE HASHING '
                hashed_password = create_password(text_password)


                # print(hashed_password,username)   #sahi aa rha hai

    #now put entry into database *** WITHOUT LOGIN STATUS******
                enter_user = sqlite3.connect('user_database.db')
                enter_user.execute('''
                    INSERT INTO user_info(username,password) 
                    VALUES (?,?) 
                ''',(username,hashed_password)
                                   )
                enter_user.commit()
                enter_user.close()

                print("USER CREATION SUCCESFULL ....PLEASSE LOGIN AGAIN")

            case 2:
                ...
                #LOGIN LOGOUT DONO ISI MEIN BANAO

                username_forlogin = input("enter username for login")
                password_forlogin = input("enter password for login")

                hashed_password_login = create_password(password_forlogin)
                # print(hashed_password_login)



                getting_user_info = sqlite3.connect("user_database.db")
                c =getting_user_info.cursor()
                c.execute('''
                    select * from user_info 
                    WHERE username = (?)  AND password = (?)
                ''',(username_forlogin,hashed_password_login)
                                                 )
                data = c.fetchall()


                # now check password and USERNAME ALREADY THERE
                # stoer it in a variable

                if data:
                    existing_user = data[0][0]
                    existing_pass = data[0][1]
                    # print(existing_user, existing_pass)
                    # print(data)         #giving a cursor object

                    # **********CHANGE STATUS******
                    c.execute('''
                        UPDATE user_info 
                        SET status = 'logged in '
                        WHERE username = (?) AND password = (?)
                    ''',(existing_user,existing_pass))
                    getting_user_info.commit()

                    choice2 = int(input('''successfull login..
                            DO YOU WANT TO 
                            1. LOGOUT OR 
                            2. CHANGE PASSWORD?
                            '''))
                    match choice2:
                        case 1:
                            ...
                            c.execute('''
                                                        UPDATE user_info 
                                                        SET status = 'logged out'
                                                        WHERE username = (?) AND password = (?)
                                                    ''', (existing_user, existing_pass))
                            getting_user_info.commit()
                            break
                        case 2:
                            ...

                            new_password = input("enter new password: ")
                            hashed_new_password = create_password(new_password)
                            c.execute(f'''  UPDATE user_info 
                                      SET password = {hashed_new_password}
                                      WHERE username = (?) AND password = (?)
                                                                                ''',
                                      (existing_user,))
                            getting_user_info.commit()
                else:
                    print("no such user......create a user again")

                getting_user_info.close()









            case 3:
                break


if __name__ == '__main__':
    main()