////////////////////////////////////////////////////////////
//
// Notetaker - A Simple Note Taking app created in Flask
// Copyright(C) 2022 - 2023 Prathamesh Thorat (thoratprathamesh08@gmail.com)
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

window.onload = () => {
  let notes = new NotesLocal();
  if (window.state == "edit") {
    document.querySelector("#title").value = notes.get(window.id).title;
    document.querySelector("#body").value = notes.get(window.id).body;
  }

  document.querySelector("#add").onclick = () => {
    let title = document.querySelector("#title").value.trim();
    let body = document.querySelector("#body").value;

    if (title == "" && body == "") return;

    if (window.state == "edit") notes.set(window.id, title, body);
    else notes.add(title, body);

    window.open("/", "_self");
  };
};
