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
from controller.cloud import *  # Cloud Controller in ./controller Directory

# Blueprint of Cloud Routes
cloud = Blueprint("cloud", __name__, url_prefix="/cloud")

# Cloud Notes Routes
cloud.get("/")(cloud_get)

# Cloud Notes Add Routes
cloud.get("/add")(cloud_add_get)
cloud.post("/add")(cloud_add_post)

# Cloud Notes Edit Routes
cloud.get("/edit/<note_id>")(cloud_edit_get)
cloud.post("/edit/<note_id>")(cloud_edit_post)

# Cloud Notes Delete Routes
cloud.get("/delete/<note_id>")(cloud_delete_get)
