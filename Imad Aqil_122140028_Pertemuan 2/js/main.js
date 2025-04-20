<<<<<<< HEAD
import { TaskManager } from "./modules/data.js";
import { ScheduleManager } from "./modules/data.js";
import { NoteManager } from "./modules/data.js";
import { renderTasks, renderSchedule, renderNotes } from "./modules/utils.js";
import { initDateTime } from "./app.js";

document.addEventListener("DOMContentLoaded", () => {
  initDateTime();

  const taskManager = new TaskManager();
  const scheduleManager = new ScheduleManager();
  const noteManager = new NoteManager();

  renderTasks(taskManager.getTasks());
  renderSchedule(scheduleManager.getSchedule());
  renderNotes(noteManager.getNotes());

  const taskForm = document.getElementById("task-form");
  taskForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("task-title").value;
    const deadline = document.getElementById("task-deadline").value;
    const priority = document.getElementById("task-priority").value;

    taskManager.addTask(title, deadline, priority);
    renderTasks(taskManager.getTasks());

    taskForm.reset();
  });

  const scheduleForm = document.getElementById("schedule-form");
  scheduleForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const className = document.getElementById("class-name").value;
    const day = document.getElementById("class-day").value;
    const time = document.getElementById("class-time").value;
    const location = document.getElementById("class-location").value;

    scheduleManager.addClass(className, day, time, location);
    renderSchedule(scheduleManager.getSchedule());

    scheduleForm.reset();
  });

  const noteForm = document.getElementById("note-form");
  noteForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("note-title").value;
    const content = document.getElementById("note-content").value;

    noteManager.addNote(title, content);
    renderNotes(noteManager.getNotes());

    noteForm.reset();
  });

  const tasksList = document.getElementById("tasks-list");
  tasksList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const taskId = e.target.dataset.id;
      taskManager.deleteTask(taskId);
      renderTasks(taskManager.getTasks());
    } else if (e.target.classList.contains("edit-btn")) {
      const taskId = e.target.dataset.id;
      const task = taskManager.getTaskById(taskId);

      if (task) {
        document.getElementById("task-title").value = task.title;
        document.getElementById("task-deadline").value = task.deadline;
        document.getElementById("task-priority").value = task.priority;

        taskManager.deleteTask(taskId);
        renderTasks(taskManager.getTasks());
      }
    }
  });

  const scheduleList = document.getElementById("schedule-list");
  scheduleList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const classId = e.target.dataset.id;
      scheduleManager.deleteClass(classId);
      renderSchedule(scheduleManager.getSchedule());
    } else if (e.target.classList.contains("edit-btn")) {
      const classId = e.target.dataset.id;
      const classItem = scheduleManager.getClassById(classId);

      if (classItem) {
        document.getElementById("class-name").value = classItem.name;
        document.getElementById("class-day").value = classItem.day;
        document.getElementById("class-time").value = classItem.time;
        document.getElementById("class-location").value = classItem.location;

        scheduleManager.deleteClass(classId);
        renderSchedule(scheduleManager.getSchedule());
      }
    }
  });

  const notesList = document.getElementById("notes-list");
  notesList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const noteId = e.target.dataset.id;
      noteManager.deleteNote(noteId);
      renderNotes(noteManager.getNotes());
    } else if (e.target.classList.contains("edit-btn")) {
      const noteId = e.target.dataset.id;
      const note = noteManager.getNoteById(noteId);

      if (note) {
        document.getElementById("note-title").value = note.title;
        document.getElementById("note-content").value = note.content;

        noteManager.deleteNote(noteId);
        renderNotes(noteManager.getNotes());
      }
    }
  });
});
=======
import { TaskManager } from "./modules/data.js";
import { ScheduleManager } from "./modules/data.js";
import { NoteManager } from "./modules/data.js";
import { renderTasks, renderSchedule, renderNotes } from "./modules/utils.js";
import { initDateTime } from "./app.js";

document.addEventListener("DOMContentLoaded", () => {
  initDateTime();

  const taskManager = new TaskManager();
  const scheduleManager = new ScheduleManager();
  const noteManager = new NoteManager();

  renderTasks(taskManager.getTasks());
  renderSchedule(scheduleManager.getSchedule());
  renderNotes(noteManager.getNotes());

  const taskForm = document.getElementById("task-form");
  taskForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("task-title").value;
    const deadline = document.getElementById("task-deadline").value;
    const priority = document.getElementById("task-priority").value;

    taskManager.addTask(title, deadline, priority);
    renderTasks(taskManager.getTasks());

    taskForm.reset();
  });

  const scheduleForm = document.getElementById("schedule-form");
  scheduleForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const className = document.getElementById("class-name").value;
    const day = document.getElementById("class-day").value;
    const time = document.getElementById("class-time").value;
    const location = document.getElementById("class-location").value;

    scheduleManager.addClass(className, day, time, location);
    renderSchedule(scheduleManager.getSchedule());

    scheduleForm.reset();
  });

  const noteForm = document.getElementById("note-form");
  noteForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("note-title").value;
    const content = document.getElementById("note-content").value;

    noteManager.addNote(title, content);
    renderNotes(noteManager.getNotes());

    noteForm.reset();
  });

  const tasksList = document.getElementById("tasks-list");
  tasksList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const taskId = e.target.dataset.id;
      taskManager.deleteTask(taskId);
      renderTasks(taskManager.getTasks());
    } else if (e.target.classList.contains("edit-btn")) {
      const taskId = e.target.dataset.id;
      const task = taskManager.getTaskById(taskId);

      if (task) {
        document.getElementById("task-title").value = task.title;
        document.getElementById("task-deadline").value = task.deadline;
        document.getElementById("task-priority").value = task.priority;

        taskManager.deleteTask(taskId);
        renderTasks(taskManager.getTasks());
      }
    }
  });

  const scheduleList = document.getElementById("schedule-list");
  scheduleList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const classId = e.target.dataset.id;
      scheduleManager.deleteClass(classId);
      renderSchedule(scheduleManager.getSchedule());
    } else if (e.target.classList.contains("edit-btn")) {
      const classId = e.target.dataset.id;
      const classItem = scheduleManager.getClassById(classId);

      if (classItem) {
        document.getElementById("class-name").value = classItem.name;
        document.getElementById("class-day").value = classItem.day;
        document.getElementById("class-time").value = classItem.time;
        document.getElementById("class-location").value = classItem.location;

        scheduleManager.deleteClass(classId);
        renderSchedule(scheduleManager.getSchedule());
      }
    }
  });

  const notesList = document.getElementById("notes-list");
  notesList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const noteId = e.target.dataset.id;
      noteManager.deleteNote(noteId);
      renderNotes(noteManager.getNotes());
    } else if (e.target.classList.contains("edit-btn")) {
      const noteId = e.target.dataset.id;
      const note = noteManager.getNoteById(noteId);

      if (note) {
        document.getElementById("note-title").value = note.title;
        document.getElementById("note-content").value = note.content;

        noteManager.deleteNote(noteId);
        renderNotes(noteManager.getNotes());
      }
    }
  });
});
>>>>>>> 46ef116e4c333020536d97f8df7297f9452c8646
