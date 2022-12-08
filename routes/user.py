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

from flask import Blueprint
from controller.user import *  # User Controller in ./controller Directory

# Blueprint of User Routes
user = Blueprint("user", __name__, url_prefix="/user")

# User Signup Routes
user.get("/signup")(signup_get)
user.post("/signup")(signup_post)

# User Login Routes
user.get("/login")(login_get)
user.post("/login")(login_post)

# User Logout Routes
user.get("/logout")(logout_get)

# User Delete Routes
user.get("/delete")(delete_get)
user.post("/delete")(delete_post)
