# Aplikasi Manajemen Buku Pribadi

Aplikasi web untuk mengelola koleksi buku pribadi yang memungkinkan pengguna mencatat buku-buku yang dimiliki, sedang dibaca, atau ingin dibeli. Dibangun menggunakan React dan Tailwind CSS.

## Fitur Aplikasi

- ✅ Penambahan buku baru (judul, penulis, status: dimiliki/sedang dibaca/ingin dibeli)
- ✅ Edit dan hapus buku dari koleksi
- ✅ Filter buku berdasarkan status
- ✅ Pencarian buku berdasarkan judul atau penulis
- ✅ Penyimpanan data lokal pada browser

## Teknologi yang Digunakan

- React.js (Functional Components dengan Hooks)
- React Router untuk navigasi antar halaman
- Context API untuk state management
- Custom Hooks (`useLocalStorage`, `useFilteredBooks`)
- Tailwind CSS untuk styling
- React Testing Library untuk unit test
- PropTypes untuk type checking

## Tampilan Aplikasi

### Halaman Beranda
![Halaman Beranda](/api/placeholder/800/400)
*Screenshot halaman beranda aplikasi menampilkan daftar buku dengan filter dan pencarian*

### Form Tambah/Edit Buku
![Form Tambah Buku](/api/placeholder/800/400)
*Screenshot form untuk menambah atau mengedit buku*

### Filter dan Pencarian
![Filter dan Pencarian](/api/placeholder/800/400)
*Screenshot fitur filter status dan pencarian buku*

## Cara Instalasi

1. Clone repository ini:
```bash
git clone
```

2. Install dependencies:
```bash
npm install
```

3. Jalankan aplikasi:
```bash
npm start
```

Aplikasi akan berjalan pada `http://localhost:3000`

## Menjalankan Test

Aplikasi ini dilengkapi dengan unit test untuk komponen utama.

```bash
npm test
```

## Struktur Direktori

```
book-management-app/
├── public/
├── src/
│   ├── components/          # Komponen reusable
│   │   ├── BookCard.js      # Komponen kartu buku
│   │   ├── BookFilter.js    # Filter status buku
│   │   └── SearchBar.js     # Pencarian buku
│   │
│   ├── context/
│   │   └── BookContext.js   # Context API untuk state management
│   │
│   ├── hooks/
│   │   ├── useFilteredBooks.js  # Custom hook untuk filtering buku
│   │   └── useLocalStorage.js   # Custom hook untuk localStorage
│   │
│   ├── pages/
│   │   ├── BookForm.jsx     # Halaman form tambah/edit buku
│   │   ├── Home.jsx         # Halaman utama
│   │   └── NotFound.jsx     # Halaman 404
│   │
│   ├── App.css
│   ├── App.js               # Setup router dan aplikasi utama
│   └── index.js
├── package.json
└── README.md
```

## Penggunaan

1. **Beranda**: Lihat semua buku, filter berdasarkan status, dan cari buku
2. **Tambah Buku**: Klik tombol "Tambah Buku" dan isi form yang disediakan
3. **Edit Buku**: Klik tombol "Edit" pada kartu buku untuk mengubah informasi
4. **Hapus Buku**: Klik tombol "Hapus" pada kartu buku untuk menghapus dari koleksi

## Kontribusi

Kontribusi selalu diterima! Silakan fork repository ini dan buat pull request dengan fitur atau perbaikan yang Anda usulkan.
