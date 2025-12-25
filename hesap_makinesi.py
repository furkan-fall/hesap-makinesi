
#kullanılan kütüphaneler - math şart değil!
import math
import colorama

#font
fonts = colorama.Style.BRIGHT

#banner - background pic
back_ground_color = colorama.Fore.YELLOW
print(back_ground_color+fonts +f"""
  _    _                         __  __       _    _                 _ 
 | |  | |                       |  \/  |     | |  (_)               (_)
 | |__| | ___  ___  __ _ _ __   | \  / | __ _| | ___ _ __   ___  ___ _ 
 |  __  |/ _ \/ __|/ _` | '_ \  | |\/| |/ _` | |/ / | '_ \ / _ \/ __| |
 | |  | |  __/\__ \ (_| | |_) | | |  | | (_| |   <| | | | |  __/\__ \ |
 |_|  |_|\___||___/\__,_| .__/  |_|  |_|\__,_|_|\_\_|_| |_|\___||___/_|
                        | |                                            
                        |_|                                            
                                                 
                                          )   )  
 (   (   (  (     (  (                 ( /(( /(  
 )\  )\ ))\ )(  ( )\ )\ )  (   (       )\())\()) 
((_)((_)((_|()\ )((_|()/(  )\  )\ )   ((_)((_)\  
\ \ / (_))  ((_|(_|_))(_))((_)_(_/(   /  (_) (_) 
 \ V // -_)| '_(_-< | || / _ \ ' \)) | () || |   
  \_/ \___||_| /__/_|\_, \___/_||_|   \__(_)_|   
                     |__/                                        
\n""")



#genel renkler
user_inter_face = colorama.Fore.BLUE
user_inter_face2 = colorama.Fore.WHITE
islem_sonucu_color = colorama.Fore.GREEN
# -> Öncelikle kullanıcıdan input alıcaz
sayi_1 = int (input(user_inter_face+f"Lütfen 1.sayınızı giriniz ->{user_inter_face2} "))
sayi_2 = int(input(user_inter_face+f"Lütfen 2.sayınızı giriniz ->{user_inter_face2} "))

#Kullanıcı input - İnfo
ipucu = " + , - , * , / , // , % ,** -> "
islem_secimi =input(user_inter_face+f"Lütfen Yapmak istediniz işlemi seçiniz: {user_inter_face2 + ipucu}") #Matematik işlemleri için ipucular
#hesaplama işlemleri için değişkenler
#degiskenlere isim verirken snake_case kuralına dikkat edildi
hesaplama_islemi_toplama =  sayi_1 + sayi_2 #toplama
hesaplama_islemi_cikarma =  sayi_1 - sayi_2 #çıkarma
hesaplama_islemi_carpma =  sayi_1 * sayi_2  #çarpma
hesaplama_islemi_bolme =  sayi_1 / sayi_2   #bölme
hesaplama_islemi_tam_bolme =  sayi_1 // sayi_2 #tam bölme
hesaplama_islemi_modulus =  sayi_1 % sayi_2  #modülüs (mod)- kalanı bulma
hesaplama_islemi_usunu_alma =  sayi_1 ** sayi_2 #üsünü bulma



#kullanıcının yaptıklarını denetleme ve ona göre davranma
if islem_secimi == "+":
    print(f"İşlem sonucu -> {islem_sonucu_color} {hesaplama_islemi_toplama}") #-> Sonuçları renkli alıyoruz
elif islem_secimi == "-":
    print(f"İşlem sonucu ->  {islem_sonucu_color} {hesaplama_islemi_cikarma}")

elif islem_secimi == "*":
    print(f"İşlem sonucu -> {islem_sonucu_color} {hesaplama_islemi_carpma}")

elif islem_secimi == "/":
    print(f"İşlem sonucu -> {islem_sonucu_color} {hesaplama_islemi_bolme}")

elif islem_secimi == "//":
    print(f"İşlem sonucu -> {islem_sonucu_color} {hesaplama_islemi_tam_bolme}")

elif islem_secimi == "%":
    print(f"İşlem sonucu ->{islem_sonucu_color}  {hesaplama_islemi_modulus}")

elif islem_secimi == "**":
    print(f"İşlem sonucu -> {islem_sonucu_color} {hesaplama_islemi_usunu_alma}")


#uygun sonuçlar yoksa hata mesajı ve input bekleme
else:
    print("Geçersiz işlem yaptınız!")
    input("Kapatmak için herhangi bir tuşa basınız....")


print(f"""                                                                                                                                              
                                                                                                                                              
████▄  ▄▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄     ▄▄▄  ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄    ▄▄▄▄  ▄▄ ▄▄   ▄█▀▀▀▀█ ▄▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄  ▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄   ▄▄▄▄▄  ▄▄▄  ▄▄    ▄▄    
██  ██ ██▄▄  ██▄██ ██▄▄  ██    ██▀██ ██▄█▀ ██▄▄  ██▀██   ██▄██ ▀███▀   █  █▀▄  ██▄▄  ██ ██ ██▄█▄ ██▄█▀ ██▀██ ███▄██   ██▄▄  ██▀██ ██    ██    
████▀  ██▄▄▄  ▀█▀  ██▄▄▄ ██▄▄▄ ▀███▀ ██    ██▄▄▄ ████▀   ██▄█▀   █     █▄ ▀▀ █ ██    ▀███▀ ██ ██ ██ ██ ██▀██ ██ ▀██ ▄ ██    ██▀██ ██▄▄▄ ██▄▄▄ 
                                                                        ▀▀▀▀▀                                                                 """)
#Çıkış boş input!
quit_app = input( colorama.Fore.RED + f"Çıkmak için herhangi bir tuşa basın....")

