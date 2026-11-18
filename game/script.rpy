
define r = Character('Rian')
define p = Character('Pak Seno')
define g = Character('Gadis Payung Merah')
define i = Character('Ibu')
define n = Character(None)

# Character Position
transform posisi_kiri:
    zoom 0.5
    xpos 230
    yalign 0.82

transform posisi_kanan:
    zoom 0.5
    xpos 1690
    xanchor 1.0
    yalign 0.82

# System Variables
default honesty = 0
default memory = 0
default father_bond = 0
default mother_bond = 0

# Chapter 1 Flags
default cek_papan = False
default cek_saku = False
default elak_jam = False

label start:

    scene black

    n "Terdengar suara getar ponsel di atas permukaan meja kayu yang berulang tiga kali sebelum akhirnya diangkat."

    i "Halo, Yan? Maaf Ibu telepon malam malam. Kamu sudah istirahat?"

    r "Belum, Bu. Ini Rian masih beresin berkas kerjaan. Kenapa, Bu? Ada yang penting?"

    i "Nggak ada apa-apa, Nak. Ibu cuma kepikiran saja. Sudah hampir setahun kamu nggak pulang. Kapan kamu ada libur barang dua hari?"

    n "Terdengar suara kertas diremas pelan—amplop pemberitahuan kontrak kerja yang tidak diperpanjang."

    r "Bu, kan Rian sudah bilang bulan lalu. Di sini lagi masa penyesuaian proyek besar. Kalau Rian pulang sekarang tanpa bawa hasil apa-apa, mau ditaruh di mana muka Rian? Ibu tunggu saja sampai urusan di sini beres, jangan telepon terus nanyain kapan pulang."

    n "Hening selama tiga detik di seberang telepon. Hanya terdengar tarikan napas pelan."

    i "Iya, Yan. Maaf ganggu waktumu. Jangan lupa makan malam, ya."

    n "Sambungan telepon terputus. Suara dengung hening memenuhi ruangan. Terdengar langkah kaki tergesa-gesa, ritsleting koper ditarik cepat, lalu pintu kamar ditutup rapat."

    r "Sial... kenapa aku ngomong kayak gitu barusan."
    n "Rian langsung mengambil jaket dan tas nya, lalu bergegas menancap gas mobil menuju pintu tol untuk menuju ke rumah orang tua nya"
    n "Suara jalan tol perlahan menghilang, digantikan hembusan angin malam yang dingin dan dengung lampu neon stasiun."
    with dissolve

    scene stasiun

    "Game dimulai!"

    n "Layar perlahan terbuka dari gelap. Cahaya lampu neon putih pucat menerangi lantai keramik abu-abu yang lembap."

    n "Rian duduk menyandar di bangku besi panjang dengan jaket denim lusuh. Di samping kakinya tergeletak sebuah koper hitam."

    show boti at posisi_kiri onlayer characters

    "Jam dua lewat..."
    "Sebentar. Ini peron berapa? Kok sepi banget?"

    hide boti onlayer characters

    n "Rian berdiri dan meregangkan bahunya yang kaku. Sejauh mata memandang, ujung peron di sebelah kiri dan kanan tertutup kabut putih tipis."

    n "Satu-satunya penanda yang menempel di tiang besi hanyalah papan seng tua bertuliskan angka 0."

    show boti at posisi_kiri onlayer characters

    "Stasiun Nol. Bagus. Jangan-jangan tadi aku ketiduran di bus terus diturunin di terminal antah-berantah."

    hide boti onlayer characters

    n "Rian mengamati sekelilingnya. Tidak ada petugas, tidak ada penumpang lain, bahkan suara kereta pun tidak terdengar."

    show boti at posisi_kiri onlayer characters

    r "Oke... daripada berdiri di sini terus, mending cari tahu dulu tempat ini."

    hide boti onlayer characters

    menu:

        "Periksa papan jadwal keberangkatan di dekat tiang.":

            $ memory += 1
            $ cek_papan = True

            n "Rian berjalan mendekati papan jadwal manual yang tergantung di dekat tiang besi."

            n "Huruf-huruf plastiknya tampak miring dan sebagian sudah memudar."

            n "Hanya ada satu baris tulisan yang masih bisa dibaca."

            n "JALUR PULANG — MENUNGGU JADWAL"

            show boti at posisi_kiri onlayer characters

            r "Sistem informasi macam apa ini. Nggak ada jam keberangkatan, nggak ada nama kota tujuan."

            hide boti onlayer characters

        "Periksa saku jaket dan celana untuk mencari ponsel.":

            $ memory += 1
            $ cek_saku = True

            n "Rian merogoh saku jaket dan celananya."

            n "Namun, ponselnya tidak ditemukan. Jarinya justru menyentuh sesuatu yang terasa seperti kertas tebal."

            n "Ia mengeluarkan selembar tiket karton kusam tanpa tanggal dan nama stasiun asal."

            show boti at posisi_kiri onlayer characters

            r "Kapan aku beli tiket kertas model begini? Perasaan tadi nyetir sendiri..."

            hide boti onlayer characters

        "Langsung berjalan menuju pos loket di ujung cahaya.":

            n "Rian mengangkat koper hitamnya dan mulai berjalan menuju arah cahaya di ujung peron."

            show boti at posisi_kiri onlayer characters

            r "Mudah-mudahan ada petugas yang bisa ditanyain."

            hide boti onlayer characters

    n "Belum jauh Rian berjalan, terdengar suara langkah sepatu kulit yang teratur dari arah lorong."

    n "Seorang pria paruh baya berseragam petugas stasiun berwarna abu-abu tua berjalan menghampirinya sambil membawa papan klip kayu."

    show laki at posisi_kanan onlayer characters

    p "Selamat malam, Mas. Kalau mencari kereta ekspres ke arah kota, jalurnya sudah tutup sejak tadi."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Akhirnya ada orang."

    r "Pak, permisi mau tanya, ini daerah mana ya? Saya mau arah pulang ke kampung, tapi kayaknya salah ambil jalur."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Ini Stasiun 0. Transit sementara."

    hide laki onlayer characters

    n "Pak Seno melirik pergelangan tangan Rian yang sejak tadi beberapa kali diperiksa."

    show laki at posisi_kanan onlayer characters

    p "Ngomong-ngomong, dari tadi saya perhatikan Mas sering sekali melirik jam tangan. Sedang dikejar jadwal rapat?"

    hide laki onlayer characters

    menu:

        "Kebiasaan di Jakarta, Pak. Kalau telat sedikit saja rasanya sudah ketinggalan banyak hal.":

            $ honesty += 1
            $ father_bond += 1

            n "Pak Seno mengangguk kecil. Sudut bibirnya sedikit terangkat."

            show laki at posisi_kanan onlayer characters

            p "Orang kota memang selalu berlari, bahkan saat sedang duduk menunggu."

            p "Padahal keretanya saja belum tentu datang lebih cepat."

            hide laki onlayer characters

            show boti at posisi_kiri onlayer characters

            r "Hehe... iya juga, Pak."

            hide boti onlayer characters

        "Nggak juga, Pak. Cuma memastikan baterai jam saya masih jalan.":

            $ elak_jam = True

            n "Pak Seno memperhatikan jam tangan Rian sejenak sebelum kembali menatapnya."

            show laki at posisi_kanan onlayer characters

            p "Begitu. Silakan saja dicek, kalau memang masih bisa jalan."

            hide laki onlayer characters

            n "Setelah mengatakan itu, Pak Seno kembali memperhatikan papan klip kayunya."

            show boti at posisi_kiri onlayer characters

            r "Iya, Pak."

            hide boti onlayer characters

        "Bapak petugas shift malam di sini? Sepi sekali stasiunnya.":

            $ father_bond += 1

            show laki at posisi_kanan onlayer characters

            p "Memang tidak banyak penumpang yang turun di sini pada jam segini."

            hide laki onlayer characters

            show boti at posisi_kiri onlayer characters

            r "Pantas saja sepi banget."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Sudah biasa."

            hide laki onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Silakan tunggu di ruang tunggu dekat mesin minuman kalau kedinginan."

    p "Kabut malam di peron tidak bagus untuk badan yang sedang capek."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Oh, ada mesin minuman juga ternyata."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Ikuti lorong itu. Nanti juga terlihat."

    hide laki onlayer characters

    n "Pak Seno merapikan papan klip kayunya, kemudian berjalan perlahan menuju pos loket."

    n "Rian memperhatikan punggung pria itu sejenak sebelum kembali mengangkat kopernya."

    show boti at posisi_kiri onlayer characters

    r "Petugasnya agak aneh juga..."

    hide boti onlayer characters

    n "Dengan langkah perlahan, Rian mulai mengikuti arah lorong yang ditunjukkan Pak Seno."

    scene black with fade

    n "Suara langkah kaki Rian perlahan menghilang di antara dengung lampu neon."

    n "Di ujung lorong, sebuah cahaya kecil tampak menyala."

    return
