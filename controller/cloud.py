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

from flask import redirect, render_template, request
from model.notes import Notes
from model.session import Session

notes = Notes()


def cloud_get():
    if not Session.logged():
        return redirect("/user/login")

    return render_template("cloud/index.html", logged=Session.logged(), notes=notes.get_all_notes(), cloud=True)


def cloud_add_get():
    if not Session.logged():
        return redirect("/user/login")

    return render_template("cloud/add.html", logged=Session.logged(), cloud=True)


def cloud_delete_get(note_id):
    if not Session.logged():
        return redirect("/user/login")

    notes.delete_note(note_id)

    return redirect("/cloud")


def cloud_add_post():
    if not Session.logged():
        return redirect("/user/login")

    data = request.form.to_dict()

    notes.add_note(data["title"], data["body"])

    return redirect("/cloud")


def cloud_edit_get(note_id):
    if not Session.logged():
        return redirect("/user/login")

    data = notes.get_note(note_id)

    return render_template("cloud/add.html", id=note_id, logged=Session.logged(), title=data["Title"], body=data["Body"], cloud=True)


def cloud_edit_post(note_id):
    if not Session.logged():
        return redirect("/user/login")

    data = request.form.to_dict()

    data = notes.edit_note(note_id, data["title"], data["body"])

    return redirect("/cloud")
