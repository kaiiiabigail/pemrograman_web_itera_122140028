from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class LibraryItem(ABC):
    """
    Abstract class yang menjadi dasar untuk semua item di perpustakaan.
    """
    def __init__(self, item_id, title, publisher, year_published):
        self._item_id = item_id  
        self._title = title  
        self._publisher = publisher  
        self._year_published = year_published  
        self._is_borrowed = False  
        self._due_date = None  

    @property
    def item_id(self):
        """Property untuk mengakses ID item."""
        return self._item_id

    @property
    def title(self):
        """Property untuk mengakses judul item."""
        return self._title

    @property
    def publisher(self):
        """Property untuk mengakses penerbit item."""
        return self._publisher

    @property
    def year_published(self):
        """Property untuk mengakses tahun terbit item."""
        return self._year_published

    @property
    def is_borrowed(self):
        """Property untuk mengecek status peminjaman item."""
        return self._is_borrowed

    @property
    def due_date(self):
        """Property untuk mengakses tanggal pengembalian item."""
        return self._due_date

    def borrow(self, days=14):
        """
        Method untuk meminjam item perpustakaan.
        
        Args:
            days (int): Jumlah hari peminjaman. Default: 14 hari.
            
        Returns:
            bool: True jika berhasil dipinjam, False jika tidak.
        """
        if not self._is_borrowed:
            self._is_borrowed = True
            self._due_date = datetime.now() + timedelta(days=days)
            return True
        return False

    def return_item(self):
        """
        Method untuk mengembalikan item perpustakaan.
        
        Returns:
            bool: True jika berhasil dikembalikan, False jika tidak.
        """
        if self._is_borrowed:
            self._is_borrowed = False
            self._due_date = None
            return True
        return False

    @abstractmethod
    def display_info(self):
        """
        Abstract method yang harus diimplementasikan oleh setiap subclass
        untuk menampilkan informasi detail dari item perpustakaan.
        """
        pass

    @abstractmethod
    def get_type(self):
        """
        Abstract method yang harus diimplementasikan oleh setiap subclass
        untuk mengembalikan tipe item perpustakaan.
        """
        pass


class Book(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan buku di perpustakaan.
    """
    def __init__(self, item_id, title, author, publisher, year_published, isbn, num_pages):
        super().__init__(item_id, title, publisher, year_published)
        self.__author = author  
        self.__isbn = isbn  
        self.__num_pages = num_pages  

    @property
    def author(self):
        """Property untuk mengakses penulis buku."""
        return self.__author

    @property
    def isbn(self):
        """Property untuk mengakses ISBN buku."""
        return self.__isbn

    @property
    def num_pages(self):
        """Property untuk mengakses jumlah halaman buku."""
        return self.__num_pages

    def display_info(self):
        """
        Implementasi dari abstract method display_info untuk menampilkan informasi buku.
        
        Returns:
            str: Informasi lengkap tentang buku.
        """
        status = "Dipinjam" if self._is_borrowed else "Tersedia"
        due_info = f" (Tenggat: {self._due_date.strftime('%d/%m/%Y')})" if self._is_borrowed else ""
        
        return (f"[BUKU] {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Penulis: {self.__author}\n"
                f"Penerbit: {self._publisher}\n"
                f"Tahun Terbit: {self._year_published}\n"
                f"ISBN: {self.__isbn}\n"
                f"Jumlah Halaman: {self.__num_pages}\n"
                f"Status: {status}{due_info}")

    def get_type(self):
        """
        Implementasi dari abstract method get_type untuk mengembalikan tipe item.
        
        Returns:
            str: Tipe item ("Buku").
        """
        return "Buku"


class Magazine(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan majalah di perpustakaan.
    """
    def __init__(self, item_id, title, publisher, year_published, issue_number, category):
        super().__init__(item_id, title, publisher, year_published)
        self.__issue_number = issue_number  
        self.__category = category  

    @property
    def issue_number(self):
        """Property untuk mengakses nomor terbitan majalah."""
        return self.__issue_number

    @property
    def category(self):
        """Property untuk mengakses kategori majalah."""
        return self.__category

    def display_info(self):
        """
        Implementasi dari abstract method display_info untuk menampilkan informasi majalah.
        
        Returns:
            str: Informasi lengkap tentang majalah.
        """
        status = "Dipinjam" if self._is_borrowed else "Tersedia"
        due_info = f" (Tenggat: {self._due_date.strftime('%d/%m/%Y')})" if self._is_borrowed else ""
        
        return (f"[MAJALAH] {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Penerbit: {self._publisher}\n"
                f"Tahun Terbit: {self._year_published}\n"
                f"Nomor Terbitan: {self.__issue_number}\n"
                f"Kategori: {self.__category}\n"
                f"Status: {status}{due_info}")

    def get_type(self):
        """
        Implementasi dari abstract method get_type untuk mengembalikan tipe item.
        
        Returns:
            str: Tipe item ("Majalah").
        """
        return "Majalah"


class DVD(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan DVD di perpustakaan.
    """
    def __init__(self, item_id, title, publisher, year_published, director, duration, genre):
        super().__init__(item_id, title, publisher, year_published)
        self.__director = director 
        self.__duration = duration 
        self.__genre = genre  

    @property
    def director(self):
        """Property untuk mengakses sutradara DVD."""
        return self.__director

    @property
    def duration(self):
        """Property untuk mengakses durasi DVD."""
        return self.__duration

    @property
    def genre(self):
        """Property untuk mengakses genre DVD."""
        return self.__genre

    def display_info(self):
        """
        Implementasi dari abstract method display_info untuk menampilkan informasi DVD.
        
        Returns:
            str: Informasi lengkap tentang DVD.
        """
        status = "Dipinjam" if self._is_borrowed else "Tersedia"
        due_info = f" (Tenggat: {self._due_date.strftime('%d/%m/%Y')})" if self._is_borrowed else ""
        
        return (f"[DVD] {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Sutradara: {self.__director}\n"
                f"Penerbit: {self._publisher}\n"
                f"Tahun Terbit: {self._year_published}\n"
                f"Durasi: {self.__duration} menit\n"
                f"Genre: {self.__genre}\n"
                f"Status: {status}{due_info}")

    def get_type(self):
        """
        Implementasi dari abstract method get_type untuk mengembalikan tipe item.
        
        Returns:
            str: Tipe item ("DVD").
        """
        return "DVD"


class Library:
    """
    Class untuk mengelola koleksi item perpustakaan.
    """
    def __init__(self, name):
        self.__name = name  
        self.__items = {}  
        self.__item_count = 0  

    @property
    def name(self):
        """Property untuk mengakses nama perpustakaan."""
        return self.__name

    @property
    def item_count(self):
        """Property untuk mengakses jumlah item di perpustakaan."""
        return self.__item_count

    def add_item(self, item):
        """
        Menambahkan item baru ke perpustakaan.
        
        Args:
            item (LibraryItem): Item perpustakaan untuk ditambahkan.
            
        Returns:
            bool: True jika berhasil ditambahkan, False jika gagal.
        """
        if not isinstance(item, LibraryItem):
            print("Error: Item harus berupa instance dari LibraryItem.")
            return False
            
        if item.item_id in self.__items:
            print(f"Error: Item dengan ID {item.item_id} sudah ada di perpustakaan.")
            return False
            
        self.__items[item.item_id] = item
        self.__item_count += 1
        return True

    def remove_item(self, item_id):
        """
        Menghapus item dari perpustakaan berdasarkan ID.
        
        Args:
            item_id: ID dari item yang akan dihapus.
            
        Returns:
            bool: True jika berhasil dihapus, False jika item tidak ditemukan.
        """
        if item_id in self.__items:
            del self.__items[item_id]
            self.__item_count -= 1
            return True
        return False

    def get_item_by_id(self, item_id):
        """
        Mencari item berdasarkan ID.
        
        Args:
            item_id: ID dari item yang dicari.
            
        Returns:
            LibraryItem: Item jika ditemukan, None jika tidak.
        """
        return self.__items.get(item_id)

    def search_items_by_title(self, title):
        """
        Mencari item berdasarkan judul (pencarian parsial).
        
        Args:
            title (str): Judul atau bagian judul yang dicari.
            
        Returns:
            list: Daftar item yang judulnya mengandung kata kunci pencarian.
        """
        found_items = []
        for item in self.__items.values():
            if title.lower() in item.title.lower():
                found_items.append(item)
        return found_items

    def display_all_items(self):
        """
        Menampilkan semua item di perpustakaan.
        """
        if not self.__items:
            print(f"Perpustakaan {self.__name} tidak memiliki item.")
            return
            
        print(f"=== Daftar Item di {self.__name} ===")
        for item in self.__items.values():
            print("-" * 40)
            print(item.display_info())
        print("-" * 40)

    def display_available_items(self):
        """
        Menampilkan item yang tersedia untuk dipinjam.
        """
        available_items = [item for item in self.__items.values() if not item.is_borrowed]
        
        if not available_items:
            print(f"Tidak ada item yang tersedia untuk dipinjam di {self.__name}.")
            return
            
        print(f"=== Item Tersedia di {self.__name} ===")
        for item in available_items:
            print("-" * 40)
            print(item.display_info())
        print("-" * 40)

    def display_borrowed_items(self):
        """
        Menampilkan item yang sedang dipinjam.
        """
        borrowed_items = [item for item in self.__items.values() if item.is_borrowed]
        
        if not borrowed_items:
            print(f"Tidak ada item yang sedang dipinjam di {self.__name}.")
            return
            
        print(f"=== Item Dipinjam di {self.__name} ===")
        for item in borrowed_items:
            print("-" * 40)
            print(item.display_info())
        print("-" * 40)

    def get_items_by_type(self, item_type):
        """
        Mengambil item berdasarkan tipenya (Buku, Majalah, DVD, dll).
        
        Args:
            item_type (str): Tipe item yang dicari.
            
        Returns:
            list: Daftar item dengan tipe yang diminta.
        """
        return [item for item in self.__items.values() if item.get_type() == item_type]


def create_sample_library():
    """
    Membuat perpustakaan dengan beberapa contoh data.
    
    Returns:
        Library: Objek perpustakaan yang sudah diisi dengan data contoh.
    """
    library = Library("Perpustakaan Kota")
    
    
    book1 = Book("B001", "Python Programming", "John Smith", "Tech Press", 2022, 
                "978-1234567890", 450)
    book2 = Book("B002", "Data Structures and Algorithms", "Jane Doe", "CS Publications", 2020, 
                "978-0987654321", 380)
    book3 = Book("B003", "Introduction to Python", "Robert Johnson", "Learning Press", 2019,
                "978-2345678901", 320)
    magazine1 = Magazine("M001", "National Geographic", "National Geographic Society", 2023, 
                        "January 2023", "Science")
    magazine2 = Magazine("M002", "Time", "Time USA, LLC", 2023, 
                        "February 2023", "News")
    dvd1 = DVD("D001", "The Matrix", "Warner Bros.", 1999, 
              "Wachowski Brothers", 136, "Sci-Fi")
    
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(magazine1)
    library.add_item(magazine2)
    library.add_item(dvd1)
    
    return library


def display_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n" + "=" * 50)
    print("SISTEM MANAJEMEN PERPUSTAKAAN".center(50))
    print("=" * 50)
    print("1. Lihat Semua Item")
    print("2. Lihat Item yang Tersedia")
    print("3. Lihat Item yang Dipinjam")
    print("4. Cari Item berdasarkan ID")
    print("5. Cari Item berdasarkan Judul")
    print("6. Pinjam Item")
    print("7. Kembalikan Item")
    print("8. Tambah Item Baru")
    print("0. Keluar")
    print("=" * 50)


def search_by_id(library):
    """
    Fungsi untuk mencari item berdasarkan ID melalui terminal.
    
    Args:
        library (Library): Objek perpustakaan yang akan dicari.
    """
    print("\n--- PENCARIAN BERDASARKAN ID ---")
    item_id = input("Masukkan ID item: ")
    
    
    item = library.get_item_by_id(item_id)
    
    if item:
        print("\nItem ditemukan!")
        print("-" * 40)
        print(item.display_info())
        print("-" * 40)
    else:
        print(f"\nItem dengan ID '{item_id}' tidak ditemukan.")


def search_by_title(library):
    """
    Fungsi untuk mencari item berdasarkan judul melalui terminal.
    
    Args:
        library (Library): Objek perpustakaan yang akan dicari.
    """
    print("\n--- PENCARIAN BERDASARKAN JUDUL ---")
    title = input("Masukkan judul atau kata kunci: ")
    
    
    found_items = library.search_items_by_title(title)
    
    if found_items:
        print(f"\nDitemukan {len(found_items)} item:")
        for i, item in enumerate(found_items, 1):
            print(f"\n- Hasil #{i} -")
            print(item.display_info())
            print("-" * 40)
    else:
        print(f"\nTidak ada item dengan judul yang mengandung '{title}'.")


def borrow_item(library):
    """
    Fungsi untuk meminjam item melalui terminal.
    
    Args:
        library (Library): Objek perpustakaan.
    """
    print("\n--- PEMINJAMAN ITEM ---")
    item_id = input("Masukkan ID item yang ingin dipinjam: ")
    
    
    item = library.get_item_by_id(item_id)
    
    if not item:
        print(f"\nItem dengan ID '{item_id}' tidak ditemukan.")
        return
        
    if item.is_borrowed:
        print(f"\nItem '{item.title}' sedang dipinjam dan tidak tersedia.")
        return
        
    
    days = input("Masukkan jumlah hari peminjaman [default: 14]: ")
    days = int(days) if days.isdigit() else 14
    
    if item.borrow(days):
        print(f"\nBerhasil meminjam '{item.title}'.")
        print(f"Tanggal pengembalian: {item.due_date.strftime('%d/%m/%Y')}")
    else:
        print("\nGagal meminjam item.")


def return_item(library):
    """
    Fungsi untuk mengembalikan item melalui terminal.
    
    Args:
        library (Library): Objek perpustakaan.
    """
    print("\n--- PENGEMBALIAN ITEM ---")
    item_id = input("Masukkan ID item yang ingin dikembalikan: ")
    
    
    item = library.get_item_by_id(item_id)
    
    if not item:
        print(f"\nItem dengan ID '{item_id}' tidak ditemukan.")
        return
        
    if not item.is_borrowed:
        print(f"\nItem '{item.title}' tidak sedang dipinjam.")
        return
        
    
    if item.return_item():
        print(f"\nBerhasil mengembalikan '{item.title}'.")
    else:
        print("\nGagal mengembalikan item.")


def add_new_item(library):
    """
    Fungsi untuk menambahkan item baru melalui terminal.
    
    Args:
        library (Library): Objek perpustakaan.
    """
    print("\n--- TAMBAH ITEM BARU ---")
    print("Pilih jenis item:")
    print("1. Buku")
    print("2. Majalah")
    print("3. DVD")
    
    choice = input("Pilihan Anda [1-3]: ")
    
    
    if choice not in ["1", "2", "3"]:
        print("Pilihan tidak valid.")
        return
        
    
    item_id = input("ID Item: ")
    title = input("Judul: ")
    publisher = input("Penerbit: ")
    year_published = input("Tahun Terbit: ")
    
    
    if not year_published.isdigit():
        print("Tahun harus berupa angka.")
        return
    year_published = int(year_published)
    
    
    if choice == "1":  
        author = input("Penulis: ")
        isbn = input("ISBN: ")
        num_pages = input("Jumlah Halaman: ")
        
        if not num_pages.isdigit():
            print("Jumlah halaman harus berupa angka.")
            return
        num_pages = int(num_pages)
        
        new_item = Book(item_id, title, author, publisher, year_published, isbn, num_pages)
        
    elif choice == "2":  
        issue_number = input("Nomor Terbitan: ")
        category = input("Kategori: ")
        
        new_item = Magazine(item_id, title, publisher, year_published, issue_number, category)
        
    else:  # DVD
        director = input("Sutradara: ")
        duration = input("Durasi (menit): ")
        genre = input("Genre: ")
        
        if not duration.isdigit():
            print("Durasi harus berupa angka.")
            return
        duration = int(duration)
        
        new_item = DVD(item_id, title, publisher, year_published, director, duration, genre)
    
    
    if library.add_item(new_item):
        print(f"\nBerhasil menambahkan {new_item.get_type()} '{title}' ke perpustakaan.")
    else:
        print("\nGagal menambahkan item ke perpustakaan.")


def main():
    """
    Fungsi utama untuk menjalankan aplikasi manajemen perpustakaan.
    """
    library = create_sample_library()
    
    while True:
        display_menu()
        choice = input("Pilih menu [0-8]: ")
        
        if choice == "0":
            print("\nTerima kasih telah menggunakan Sistem Manajemen Perpustakaan!")
            break
            
        elif choice == "1":
            library.display_all_items()
            
        elif choice == "2":
            library.display_available_items()
            
        elif choice == "3":
            library.display_borrowed_items()
            
        elif choice == "4":
            search_by_id(library)
            
        elif choice == "5":
            search_by_title(library)
            
        elif choice == "6":
            borrow_item(library)
            
        elif choice == "7":
            return_item(library)
            
        elif choice == "8":
            add_new_item(library)
            
        else:
            print("\nPilihan tidak valid. Silakan pilih menu 0-8.")
        
        
        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()