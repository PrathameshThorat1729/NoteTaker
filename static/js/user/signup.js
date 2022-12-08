////////////////////////////////////////////////////////////
//
// Notetaker - A Simple Note Taking app created in Flask
// Copyright(C) 2022 - 2023 Prathamesh Thorat (thoratprathamesh1729@gmail.com)
//
// This software is provided 'as-is', without any express or implied warranty.
// In no event will the authors be held liable for any damages arising from the use of this software.
//
// Permission is granted to anyone to use this software for any purpose,
// including commercial applications, and to alter it and redistribute it freely,
// subject to the following restrictions:
//
// 1. The origin of this software must not be misrepresented
// you must not claim that you wrote the original software.
// If you use this software in a product, an acknowledgment
// in the product documentation would be appreciated but is not required.
//
// 2. Altered source versions must be plainly marked as such,
// and must not be misrepresented as being the original software.
//
// 3. This notice may not be removed or altered from any source distribution.
//
////////////////////////////////////////////////////////////

const trim = (ev) => {
  let val = ev.target.value.trim();

  ev.target.value = val;
};

window.onload = () => {
  let re = {
    email:
      /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
    username: /(?=.*\d)(?=.*[A-z])/g,
    password:
      /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_\-+=[\]{}|\\:;'"?/.>,<`~])/g,
  };
  document.getElementById("form").onsubmit = (e) => {
    let is = true;
    let data = new FormData(e.target);

    if (!data.get("username").match(re.username)) {
      is = false;
      document.getElementById("username").classList.add("wrong");
    } else document.getElementById("username").classList.remove("wrong");

    if (!data.get("email").match(re.email)) {
      is = false;
      document.getElementById("email").classList.add("wrong");
    } else document.getElementById("email").classList.remove("wrong");

    if (
      !data.get("password").match(re.password) ||
      !(data.get("password").length >= 8)
    ) {
      is = false;
      document.getElementById("password").classList.add("wrong");
    } else document.getElementById("password").classList.remove("wrong");

    if (is == false) e.preventDefault();
  };
};
