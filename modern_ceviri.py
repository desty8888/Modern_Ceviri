modern_ceviri = { "LOL":"haykirmak", "ROFL":"sakaya verilen cevap", "CRINGE":"Utandirici", "AGGRO":"sinirli"}

soru = input("Hangi kelimenin anlami ogrenmek istiyorsun?")

soru = soru.upper()

if soru in modern_ceviri.keys():
    print(modern_ceviri[soru])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Kelime bulunmadi!")
