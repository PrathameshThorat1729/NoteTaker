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

from flask import Blueprint
from controller.home import *  # Home Controller in ./controller Directory

# Blueprint of Home Routes
home = Blueprint("home", __name__, url_prefix="/")

# Local Notes Routes
home.get("/")(home_get)

# Local Notes Add Routes
home.get("/add")(add_get)

# Local Notes Edit Routes
home.get("/edit/<note_id>")(set_get)
