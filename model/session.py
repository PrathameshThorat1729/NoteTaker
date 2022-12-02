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

from flask import session
from model.database import Database
from validators.email import email as is_email

db = Database()


class Session:
    """Session Model Class to Handle Sessions in App"""

    @staticmethod
    def login(usermail: str, password: str):
        """Method for login a User
        - username : Username of User
        - password : Password of User"""

        if not db.exists(usermail):
            return {
                "error": True,
                "message": "Invalid Credentials"
            }

        ID = db.get_user_id(usermail, password)

        if ID:
            session["ID"] = ID

            return {
                "error": False
            }

        print(ID)

        return {
            "error": True,
            "message": "Invalid Credentials"
        }

    @staticmethod
    def logged():
        """Method to check is logged or not"""

        if Session.get_id() != None:
            return True
        return False

    @staticmethod
    def get_id() -> str:
        """Method to ID of current logged user"""

        return session.get("ID")

    @staticmethod
    def logout():
        """Method to logout user"""

        session.clear()
