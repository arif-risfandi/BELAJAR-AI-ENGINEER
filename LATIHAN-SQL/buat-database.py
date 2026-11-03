import sqlite3

koneksi = sqlite3.connect(
    "latihan.db"
)

koneksi.execute("""
CREATE TABLE IF NOT EXISTS pengguna (
    id INTEGER PRIMARY KEY,
    nama TEXT,
    kota TEXT
)
""")

koneksi.commit()
koneksi.close()

print("Database berhasil dibuat")