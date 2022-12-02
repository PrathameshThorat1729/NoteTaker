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

from model.database import Database
from model.session import Session
from hashlib import md5
from uuid import uuid1


class Notes(Database):
    def __init__(self):
        """Notes Model Class derived from Database Model Class to Handle Database work realated to Notes table"""
        super().__init__()

    def add_note(self, title: str = "Cloud Note Title", body: str = "Cloud Note Here"):
        """Method for adding note in Database
        - title : Title of Note
        - body : Body of Note"""

        query = "INSERT INTO notes (ID, Title, Body, User_ID) VALUES (%s,%s,%s,%s)"
        ID = md5(str(uuid1()).encode("utf-8")).hexdigest()
        User_ID = Session.get_id()

        if title.strip(" ") == "":
            title = "Cloud Note Title"
        if body.strip(" ") == "":
            body = "Cloud Note Here"

        return self.execute(query, params=(ID, title, body, User_ID,), commit=True)

    def get_note(self, ID: str):
        """Method for getting a note in Database by ID
        - ID = ID of note"""

        query = "SELECT ID, Title, Body FROM notes WHERE ID = %s AND User_ID = %s"
        User_ID = Session.get_id()

        return self.execute(query, params=(ID, User_ID,))

    def delete_note(self, ID: str):
        """Method for delete note in Database
        - ID = ID of note"""

        query = "DELETE FROM notes WHERE ID = %s AND User_ID = %s"
        count = "SELECT COUNT(*) as count FROM notes WHERE User_ID = %s"
        User_ID = Session.get_id()

        count = self.execute(count, params=(User_ID,), )["count"]

        if count == 1:
            self.edit_note(ID)
            return

        self.execute(query, params=(ID, User_ID,))

        return 0

    def get_all_notes(self):
        """Method for adding all notes in Database"""

        query = "SELECT ID, Title, Body FROM notes WHERE User_ID = %s"
        User_ID = Session.get_id()

        data = self.execute(query, params=(User_ID,), all=True)

        if (len(data) == 0):
            self.add_note()

        data = self.execute(query, params=(User_ID,), all=True)

        return data

    def edit_note(self, id: str, title: str = "Cloud Note Title", body: str = "Cloud Note Here"):
        """Method for editing a note in Database
        - id : ID of Note
        - title : Title of Note
        - body : Body of Note"""

        if title.strip(" ") == "":
            title = "Cloud Note Title"
        if body.strip(" ") == "":
            body = "Cloud Note Here"

        query = "UPDATE notes SET Title = %s, Body = %s WHERE ID = %s AND User_ID = %s"

        return self.execute(query, params=(title, body, id, Session.get_id(),), commit=True)
