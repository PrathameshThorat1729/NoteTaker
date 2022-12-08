/**********************************************************
*
* Notetaker - A Simple Note Taking app created in Flask
* Copyright(C) 2022 - 2023 Prathamesh Thorat (thoratprathamesh1729@gmail.com)
*
* This software is provided 'as-is', without any express or implied warranty.
* In no event will the authors be held liable for any damages arising from the use of this software.
*
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it freely,
* subject to the following restrictions:
*
* 1. The origin of this software must not be misrepresented
* you must not claim that you wrote the original software.
* If you use this software in a product, an acknowledgment
* in the product documentation would be appreciated but is not required.
*
* 2. Altered source versions must be plainly marked as such,
* and must not be misrepresented as being the original software.
*
* 3. This notice may not be removed or altered from any source distribution.
*
***********************************************************/

/* Creating Database */
CREATE DATABASE IF NOT EXISTS notetaker;
USE notetaker;

/* Creating Table for Users */
CREATE TABLE IF NOT EXISTS users (
    ID varchar(36),
    Username varchar(100) NOT NULL,
    Email varchar(320) NOT NULL,
    Password varchar(256) NOT NULL,
    PRIMARY KEY(ID)
);

/* Creating Table for Notes */
CREATE TABLE IF NOT EXISTS notes (
    ID varchar(36),
    Title varchar(100) DEFAULT "Note Title",
    Body text,
    User_ID varchar(36) NOT NULL,
    PRIMARY KEY(ID)
);