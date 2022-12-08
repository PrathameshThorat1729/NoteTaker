############################################################
#
# Notetaker - A Simple Note Taking app created in Flask
# Copyright(C) 2022 - 2023 Prathamesh Thorat (thoratprathamesh1729@gmail.com)
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

import re
from flask import render_template, request, redirect
from model.database import Database
from model.session import Session


db = Database()


def signup_get():
    if Session.logged():
        return redirect("/")
    return render_template("user/signup.html", logged=Session.logged())


def login_get():
    if Session.logged():
        return redirect("/")
    return render_template("user/login.html", logged=Session.logged())


def signup_post():
    if Session.logged():
        return redirect("/")
    data = request.form.to_dict()
    regx = {
        "email": r"""\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b""",
        "username": r"""(?=.*\d)(?=.*[A-z])""",
        "password": r"""(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@  # $%^&*()_\-+=[\]{}|\\:;'"?/.>,<`~])"""
    }

    print(data["email"])

    if (re.match(regx["username"], data["username"])) and \
       (re.match(regx["email"], data["email"])) and \
       (re.match(regx["password"], data["password"])):
        data = db.add_user(data["username"], data["password"], data["email"])
        if not data["error"]:
            return redirect("/user/login")

    return render_template("user/signup.html", error=data["error"], message=data["message"], logged=Session.logged())


def login_post():
    if Session.logged():
        return redirect("/")

    data = request.form.to_dict()
    log = Session.login(data["usermail"], data["password"])

    if not log["error"]:
        return redirect(f"/cloud")

    return render_template("user/login.html", error=log["error"], message=log["message"], logged=Session.logged())


def logout_get():
    Session.logout()
    return redirect("/")


def delete_get():
    if not Session.logged():
        return redirect("/")
    return render_template("user/delete.html", logged=Session.logged())


def delete_post():
    if Session.logged():
        db.delete_user(Session.get_id(), request.form.get("password"))
        if (db.exists_ID(Session.get_id())) == False:
            Session.logout()
        else:
            return render_template("user/delete.html", logged=Session.logged(), error=True, message="Incorrect Password")

    return redirect("/")
