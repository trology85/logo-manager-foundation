import json
import os

LOGOS_DIR = 'logos'
JSON_FILE = 'logolar.json'
# Senin logonun internetteki tam yolu
BASE_URL = "https://raw.githubusercontent.com/trology85/logo-manager-foundation/main/logos/"

def run():
    # Mevcut JSON'u oku
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    # Mevcut isimleri kontrol et (Küçük harf duyarsız eşleşme için)
    existing_names = {item['name'].lower() for item in data}
    
    new_added = False
    # Klasörü tara
    if not os.path.exists(LOGOS_DIR):
        print("Logos klasörü bulunamadı!")
        return

    for filename in os.listdir(LOGOS_DIR):
        if filename.endswith('.png'):
            # Dosya adından uzantıyı at, ismi al (Örn: "atv HD")
            canal_name = filename.rsplit('.', 1)[0]
            
            # Eğer bu isim JSON listesinde yoksa ekle
            if canal_name.lower() not in existing_names:
                new_entry = {
                    "name": canal_name, # Dosyadaki ismin aynısı
                    "url": BASE_URL + filename,
                    "rev": "rev=1"
                }
                data.append(new_entry)
                new_added = True
                print(f"Eklendi: {canal_name}")

    if new_added:
        # Alfabetik sırala (isteğe bağlı ama düzenli durması için iyidir)
        data.sort(key=lambda x: x['name'].lower())
        
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("JSON güncellendi.")
    else:
        print("Yeni logo yok.")

if __name__ == "__main__":
    run()
