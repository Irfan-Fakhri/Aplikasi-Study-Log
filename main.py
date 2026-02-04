catatan = []

def tambah_catatan():
    print("\n--- Tambah Catatan Belajar ---")
    mapel = input("Mata pelajaran: ")
    topik = input("Topik: ")
    durasi = input("Durasi belajar (menit): ")
    
    # Validasi durasi adalah angka
    try:
        durasi = int(durasi)
        if durasi <= 0:
            print("❌ Durasi harus lebih dari 0 menit")
            return
    except ValueError:
        print("❌ Durasi harus berupa angka")
        return
    
    # Simpan ke dalam list dengan format dictionary
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    catatan.append(catatan_baru)
    print("✅ Catatan berhasil ditambahkan!")

def lihat_catatan():
    print("\n" + "="*50)
    print("         📚 DAFTAR CATATAN BELAJAR 📚")
    print("="*50)
    
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar.")
        print("   Mulai belajar sekarang dan catat progresmu!\n")
        return
    
    for i, item in enumerate(catatan, 1):
        print(f"\n┌─ CATATAN {i} " + "─"*(40 - len(str(i))))
        print(f"│ 📖 Mapel   : {item['mapel']}")
        print(f"│ 📝 Topik   : {item['topik']}")
        print(f"│ ⏱️  Durasi  : {item['durasi']} menit")
        print("└" + "─"*49)
    
    print("\n" + "="*50)

def total_waktu():
    print("\n" + "="*50)
    print("       ⏱️  TOTAL WAKTU BELAJAR ⏱️")
    print("="*50)
    
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar.")
        print("   Mulai catat sesi belajarmu untuk melihat statistik!\n")
        return
    
    # Hitung total durasi
    total_menit = sum(item['durasi'] for item in catatan)
    jam = total_menit // 60
    menit = total_menit % 60
    
    # Tampilkan statistik
    print(f"\n📊 Total Waktu Belajar:")
    print(f"   ├─ {total_menit} menit")
    print(f"   └─ {jam} jam {menit} menit")
    print(f"\n📈 Jumlah Sesi Belajar: {len(catatan)} kali")
    print(f"📌 Rata-rata per Sesi: {total_menit // len(catatan)} menit")
    print("\n" + "="*50)

def filter_per_mapel():
    print("\n" + "="*50)
    print("       🔍 FILTER CATATAN PER MAPEL 🔍")
    print("="*50)
    
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar.\n")
        return
    
    # Ambil daftar mapel yang unik
    daftar_mapel = []
    for item in catatan:
        if item['mapel'] not in daftar_mapel:
            daftar_mapel.append(item['mapel'])
    
    # Tampilkan pilihan mapel
    print("\n📚 Daftar Mapel yang tersedia:")
    for i, mapel in enumerate(daftar_mapel, 1):
        print(f"   {i}. {mapel}")
    
    try:
        pilihan = int(input("\nPilih nomor mapel: "))
        if 1 <= pilihan <= len(daftar_mapel):
            mapel_dipilih = daftar_mapel[pilihan - 1]
            
            # Filter catatan berdasarkan mapel
            catatan_filter = [c for c in catatan if c['mapel'] == mapel_dipilih]
            
            print("\n" + "="*50)
            print(f"       📖 CATATAN MAPEL: {mapel_dipilih.upper()}")
            print("="*50)
            
            for i, item in enumerate(catatan_filter, 1):
                print(f"\n┌─ CATATAN {i} " + "─"*(40 - len(str(i))))
                print(f"│ 📝 Topik   : {item['topik']}")
                print(f"│ ⏱️  Durasi  : {item['durasi']} menit")
                print("└" + "─"*49)
            
            # Hitung total waktu per mapel
            total_menit = sum(c['durasi'] for c in catatan_filter)
            print(f"\n📊 Total waktu belajar {mapel_dipilih}: {total_menit} menit")
            print("="*50)
        else:
            print("❌ Pilihan tidak valid")
    except ValueError:
        print("❌ Input harus berupa angka")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Filter catatan per mapel")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        filter_per_mapel()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")