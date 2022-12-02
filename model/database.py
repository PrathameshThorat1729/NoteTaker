############################################################
#
# Notetaker - A Simple Note Taking app created in Flask
# Copyright(C) 2022 - 2023 Prathamesh Thorat (thoratprathamesh08@gmail.com)
#
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the authors be held liable for any damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it freely,
# subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented
# you must not claim that you wrote the original software.
# If you use this software in a product, an acknowledgment
# in the product documentation would be appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such,
# and must not be misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.
#
############################################################

from validators import email as is_email
from uuid import uuid1
from hashlib import sha256
from config import *
import mysql.connector as SQL


class Database():
    def __init__(self):
        """Database Model Class to Handle Database"""
        try:
            """Connecting to Database"""
            self.conn = SQL.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB
            )
        except:
            self.conn = None

    def execute(self, query: str,  params: tuple | None = None, commit=False, all=False) -> dict | list | None:
        """Method for Executing Commands and Return Data
        - query : Query is Command to Execute in MySQL syntax
        - params : Params are parameters passed in Query to replace %s
        - commit: Commit is wheather to save somthing in databse or not
        - all : All is wheather to fetch all results (in List) or only first (in Dict)
        """
        try:
            if not self.conn.is_connected():
                self.__init__()
            data = []
            curr = self.conn.cursor(dictionary=True)

            curr.execute(query, params)

            if commit == True:
                self.conn.commit()
            else:
                if all == True:
                    data = curr.fetchall()
                else:
                    data = curr.fetchone()

            curr.close()

            return data
        except:
            return None

    def exists(self, usermail: str):
        """Method to check if User exist or not From Username or Email
        - usermail : Usermail is Username or Email of User"""

        query = ""
        if is_email(usermail):
            query = "SELECT * FROM users WHERE Email = %s"
        else:
            query = "SELECT * FROM users WHERE Username = %s"

        if not self.execute(query, params=(usermail,), all=True):
            return False
        return True

    def exists_ID(self, ID: str):
        """Method to check if User exist or not From User_ID
        - ID : ID of User"""

        query = "SELECT * FROM users WHERE ID = %s"

        if not self.execute(query, params=(ID,), all=True):
            return False
        return True

    def add_user(self, username: str, password: str, email: str):
        """Method to Add new User
        - username : Username of User
        - password : Password of User
        - email : Email of User"""

        if not self.exists(email) and is_email(email):
            if self.execute("INSERT INTO users (ID, Username, Email,Password) VALUES (%s,%s,%s,%s)", params=(
                str(uuid1()),
                username,
                email,
                sha256(password.encode("utf-8")).hexdigest()
            ), commit=True) != None:
                return {"error": False}
        else:
            return {
                "error": True,
                "message": "User Already Exists"
            }

        return {
            "error": True,
            "message": "Internal Error Occured"
        }

    def get_user_id(self, usermail: str, password: str):
        """Method to get User_ID of User
        - username : Username of User
        - password : Password of User"""
        if not self.exists(usermail):
            return False

        query = ""
        if is_email(usermail):
            query = "SELECT ID FROM users WHERE Email = %s AND Password = %s"
        else:
            query = "SELECT ID FROM users WHERE Username = %s AND Password = %s"

        data = self.execute(query, params=(
            usermail, sha256(password.encode("utf-8")).hexdigest(),))

        if data:
            return data["ID"]

        return None

    def delete_user(self, ID: str, password: str):
        """Method to Delete a User from User_ID
        - ID : ID of User
        - password : Password of User"""

        query = "DELETE FROM users WHERE ID = %s AND Password = %s"
        query2 = "DELETE FROM notes WHERE User_ID = %s"
        password = sha256(password.encode("utf-8")).hexdigest()

        self.execute(query, params=(ID, password,), commit=True)
        return self.execute(query2, params=(ID, ), commit=True)
