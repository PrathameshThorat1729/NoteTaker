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

class NotesLocal {
  constructor() {
    this.keys = [];

    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      if (key.startsWith("note-")) this.keys.push(key);
    }

    if (this.length <= 0) this.add("Note Title", "Note Here");
  }

  get length() {
    let len = localStorage.getItem("length");
    if (!len) {
      localStorage.setItem("length", 0);
      len = 0;
    }

    return len;
  }

  add(title, body, id) {
    try {
      if (id == null || !id.startsWith("note-")) id = "note-" + uuidv1();
      localStorage.setItem(
        id,
        JSON.stringify({
          title,
          body,
        })
      );
      localStorage.setItem("length", parseInt(this.length) + 1);
      this.keys.push(id);
    } catch {
      return;
    }
  }

  set(id, title, body) {
    if (!this.keys.includes(id)) this.add(title, body, id);
    let data = JSON.parse(localStorage.getItem(id));
    data.title = title;
    data.body = body;
    localStorage.setItem(id, JSON.stringify(data));
  }

  get(id) {
    let data = JSON.parse(localStorage.getItem(id));
    data.id = id;

    return data;
  }

  delete(id) {
    localStorage.removeItem(id);
    let ind = this.keys.indexOf(id);
    if (ind >= 0) this.keys.splice(ind, 1);
    localStorage.setItem("length", this.length - 1);

    if (this.length <= 0) this.add("Note Title", "Note Here");
  }

  getAll() {
    return this.keys.map((el) => {
      return this.get(el);
    });
  }
}
