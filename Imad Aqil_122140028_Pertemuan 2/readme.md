<<<<<<< HEAD
Pertemuan 2
fitur ES6+ (JavaScript modern) yang diimplementasikan:

1. Arrow Functions

Digunakan secara konsisten dalam kode, contohnya const updateDateTime = () => {...} di app.js
Membantu penulisan kode yang lebih singkat dan menghindari masalah binding this

2. Class dan Inheritance

Penggunaan class untuk membuat objek StorageManager sebagai parent class
Class turunan (TaskManager, ScheduleManager, dan NoteManager) yang meng-extend StorageManager
Memanfaatkan constructor dan inheritance untuk pola kode yang lebih OOP

3. Modules (import/export)

Implementasi ES modules dengan import dan export untuk memisahkan kode ke dalam bagian yang terorganisir
Contoh: import { TaskManager } from './modules/data.js' di main.js

4. Template Literals

Penggunaan string template literals dengan backtick (`) untuk membuat string multi-baris dan interpolasi
Contoh: taskElement.innerHTML = <div class="task-header">...</div>;

5. Destructuring Assignment

Menggunakan destructuring dalam map operation: tasks.map(task => task.id === id ? { ...task, ...updates } : task)

6. Spread Operator

Digunakan untuk membuat salinan array dan menggabungkan objek: const sortedTasks = [...tasks]
Digunakan juga untuk meng-update objek: { ...task, ...updates }

7. Default Parameters

Parameter fungsi dengan nilai default, contoh: showNotification(message, type = 'info')

8. const dan let

Menggunakan const untuk variabel yang tidak berubah nilainya dan let untuk variabel yang akan diubah

9. Method Properties dan Concise Methods

Penulisan metode dalam class dengan sintaks yang lebih singkat: getTasks = () => {...}

10. Local Storage API

Penggunaan localStorage untuk menyimpan data secara persisten di browser

Penjelasan Singkat Aplikasi dan Fitur-fiturnya
Tentang Aplikasi
Dashboard Produktif Imad adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa mengelola dan mengatur tugas akademik, jadwal kelas, dan catatan penting. Aplikasi ini memiliki antarmuka yang modern dan responsif, dibuat dengan HTML, CSS, dan JavaScript murni tanpa framework tambahan.

1. Fitur Utama

Pengelolaan Tugas (Task Management)

Menambahkan tugas baru dengan judul, tanggal deadline, dan prioritas
Menampilkan tugas dalam daftar yang diurutkan berdasarkan deadline
Menandai tugas dengan warna berbeda berdasarkan prioritas (rendah, menengah, tinggi)
Fungsi edit dan hapus tugas
Penanda visual untuk tugas yang mendekati deadline (due soon)

2. Jadwal Kelas (Class Schedule)

Menambahkan jadwal kelas dengan nama, hari, waktu, dan lokasi
Menampilkan jadwal yang dikelompokkan berdasarkan hari dan diurutkan berdasarkan waktu
Highlight khusus untuk jadwal hari ini
Fungsi edit dan hapus jadwal kelas

3. Catatan (Notes)

Menambahkan catatan dengan judul dan konten
Format konten yang mendukung paragraf multi-baris
Menampilkan catatan diurutkan dari yang terbaru
Fungsi edit dan hapus catatan

4. Fitur Tambahan

Tampilan tanggal dan waktu real-time yang diperbarui setiap detik
Penyimpanan data lokal menggunakan localStorage browser
Notifikasi untuk aksi seperti menambah, mengedit, atau menghapus item
Desain responsif yang bekerja di berbagai ukuran layar
Animasi dan efek visual untuk meningkatkan pengalaman pengguna

5. Manajemen Data

Semua data disimpan secara lokal di browser pengguna
Penggunaan kelas StorageManager untuk abstraksi operasi penyimpanan
Implementasi sistem ID unik untuk setiap item
Pemisahan logika data dan tampilan untuk memudahkan pemeliharaan kode

Secara keseluruhan, aplikasi ini memberikan solusi all-in-one bagi mahasiswa untuk mengorganisir kegiatan akademik mereka dengan antarmuka yang intuitif dan menarik secara visual.
![image](https://github.com/user-attachments/assets/cef10ab4-36a6-480c-b497-1dc5cba99f5c)
=======
Pertemuan 2

fitur ES6+ (JavaScript modern) yang diimplementasikan:

1. Arrow Functions

Digunakan secara konsisten dalam kode, contohnya const updateDateTime = () => {...} di app.js
Membantu penulisan kode yang lebih singkat dan menghindari masalah binding this

2. Class dan Inheritance

Penggunaan class untuk membuat objek StorageManager sebagai parent class
Class turunan (TaskManager, ScheduleManager, dan NoteManager) yang meng-extend StorageManager
Memanfaatkan constructor dan inheritance untuk pola kode yang lebih OOP

3. Modules (import/export)

Implementasi ES modules dengan import dan export untuk memisahkan kode ke dalam bagian yang terorganisir
Contoh: import { TaskManager } from './modules/data.js' di main.js

4. Template Literals

Penggunaan string template literals dengan backtick (`) untuk membuat string multi-baris dan interpolasi
Contoh: taskElement.innerHTML = <div class="task-header">...</div>;

5. Destructuring Assignment

Menggunakan destructuring dalam map operation: tasks.map(task => task.id === id ? { ...task, ...updates } : task)

6. Spread Operator

Digunakan untuk membuat salinan array dan menggabungkan objek: const sortedTasks = [...tasks]
Digunakan juga untuk meng-update objek: { ...task, ...updates }

7. Default Parameters

Parameter fungsi dengan nilai default, contoh: showNotification(message, type = 'info')

8. const dan let

Menggunakan const untuk variabel yang tidak berubah nilainya dan let untuk variabel yang akan diubah

9. Method Properties dan Concise Methods

Penulisan metode dalam class dengan sintaks yang lebih singkat: getTasks = () => {...}

10. Local Storage API

Penggunaan localStorage untuk menyimpan data secara persisten di browser

Penjelasan Singkat Aplikasi dan Fitur-fiturnya
Tentang Aplikasi
Dashboard Produktif Imad adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa mengelola dan mengatur tugas akademik, jadwal kelas, dan catatan penting. Aplikasi ini memiliki antarmuka yang modern dan responsif, dibuat dengan HTML, CSS, dan JavaScript murni tanpa framework tambahan.

1. Fitur Utama

Pengelolaan Tugas (Task Management)

Menambahkan tugas baru dengan judul, tanggal deadline, dan prioritas
Menampilkan tugas dalam daftar yang diurutkan berdasarkan deadline
Menandai tugas dengan warna berbeda berdasarkan prioritas (rendah, menengah, tinggi)
Fungsi edit dan hapus tugas
Penanda visual untuk tugas yang mendekati deadline (due soon)

2. Jadwal Kelas (Class Schedule)

Menambahkan jadwal kelas dengan nama, hari, waktu, dan lokasi
Menampilkan jadwal yang dikelompokkan berdasarkan hari dan diurutkan berdasarkan waktu
Highlight khusus untuk jadwal hari ini
Fungsi edit dan hapus jadwal kelas

3. Catatan (Notes)

Menambahkan catatan dengan judul dan konten
Format konten yang mendukung paragraf multi-baris
Menampilkan catatan diurutkan dari yang terbaru
Fungsi edit dan hapus catatan

4. Fitur Tambahan

Tampilan tanggal dan waktu real-time yang diperbarui setiap detik
Penyimpanan data lokal menggunakan localStorage browser
Notifikasi untuk aksi seperti menambah, mengedit, atau menghapus item
Desain responsif yang bekerja di berbagai ukuran layar
Animasi dan efek visual untuk meningkatkan pengalaman pengguna

5. Manajemen Data

Semua data disimpan secara lokal di browser pengguna
Penggunaan kelas StorageManager untuk abstraksi operasi penyimpanan
Implementasi sistem ID unik untuk setiap item
Pemisahan logika data dan tampilan untuk memudahkan pemeliharaan kode

Secara keseluruhan, aplikasi ini memberikan solusi all-in-one bagi mahasiswa untuk mengorganisir kegiatan akademik mereka dengan antarmuka yang intuitif dan menarik secara visual.
![image](https://github.com/user-attachments/assets/cef10ab4-36a6-480c-b497-1dc5cba99f5c)
>>>>>>> 46ef116e4c333020536d97f8df7297f9452c8646
