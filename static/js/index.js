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

let notes;

const addNote = (note) => {
  const el = document.getElementById("temp").content.cloneNode(1);

  el.querySelector(".note").setAttribute("id", note.id);
  el.querySelector(".title").innerText = note.title;
  el.querySelector(".body").innerText = note.body;

  el.querySelector(".note").addEventListener(
    "click",
    () => {
      let show = document.querySelector(".show");
      show.innerHTML = "";
      show.classList.remove("none");
      show.appendChild(
        document.querySelector(".note[id='" + note.id + "']").cloneNode(true)
      );

      show.querySelector(" .close").addEventListener("click", (e) => {
        show.innerHTML = "";
        show.classList.add("none");
      });

      show.querySelector(".delete").addEventListener("click", (e) => {
        notes.delete(note.id);
        window.location.reload();
      });

      show.querySelector(".edit").addEventListener("click", (e) => {
        window.open("/edit/" + note.id, "_self");
      });
    },
    true
  );

  el.querySelector(".delete").addEventListener("click", (e) => {
    notes.delete(note.id);
    window.location.reload();
  });

  document.getElementById("container").appendChild(el);
};

window.addEventListener("DOMContentLoaded", () => {
  notes = new NotesLocal();
  notes.getAll().forEach((el) => {
    addNote(el);
  });
});
