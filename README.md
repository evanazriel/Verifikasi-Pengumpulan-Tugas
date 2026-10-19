## LAPORAN PROYEK ALJABAR BOOLEAN
Studi Kasus 5: Validasi Pengumpulan Tugas pada LMS Kampus 

Mata kuliah Matematika Diskrit diampu oleh : Andri Rahadyan S.Pd., M.Si 

Proyek ini dibuat untuk menyelesaikan Studi Kasus 5: Validasi Pengumpulan Tugas pada LMS Kampus dalam mata kuliah Matematika Diskrit. Program ini bertujuan untuk memodelkan, menyederhanakan, dan memverifikasi kesetaraan ekspresi logika Boolean dari aturan verifikasi sistem LMS menggunakan Python.
Fungsionalitas inti meliputi :
1. Representasi Fungsi Awal ($f\_awal$): Memodelkan aturan bisnis asli sistem LMS ke dalam fungsi Boolean ($C + D \cdot [A + (B \cdot C \cdot D)]$).

2. Representasi Fungsi Sederhana ($f\_sederhana$): Menerapkan hasil penyederhanaan bentuk Sum-of-Products (SOP) minimal ($A \cdot C + A \cdot D + B \cdot C \cdot D$) menggunakan hukum Aljabar Boolean dan Peta Karnaugh (K-Map).

3. Representasi Gerbang Universal ($f\_nand$): Mensimulasikan rancangan rangkaian fisik menggunakan gerbang universal  NAND.Verifikasi Otomatis: Melakukan pengujian tabel kebenaran secara menyeluruh pada $16$ kombinasi masukan ($A, B, C, D$) untuk memastikan seluruh fungsi bernilai ekuivalen (100% cocok).

## Requirement
* Python 3 (Direkomendasikan: Python 3.8 atau yang lebih baru)

# Setup and Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/evanazriel/Verifikasi-Pengumpulan-Tugas.git 
    ```

2. **Run main.py**
    ```bash
    python main.py
    ```

## Identitas Kelompok

| No | NIM          | Nama Lengkap                  |
| -- | ------------ | ----------------------------- |
| 1  | 202543500183 | Evan Azriel Devtriyan         |
| 2  | 202543500195 | Razan Maulana Hakim           |
| 3  | 202543500194 | Zhyzho Putra William          |


