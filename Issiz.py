from Insan import Insan
class Issiz(Insan): # Insan sınıfından kalıtım yoluyla nesneler oluşturma
    def _init_(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        # super() metodu ile Insan sınıfının nesnelerine ulasıyoruz
        super()._init_(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        # tecrubeler nesnesini de private olarak atıyoruz
        self.__tecrubeler = tecrubeler

    # get metodu ile tecrübe bilgilerine ulaşma
    def get_tecrubeler(self):
        return self.__tecrubeler
    # set metodu ile tecrubeler private değişkenine bir değer atama
    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0.2
            beyaz_yaka_etkisi = 0.35
            yonetici_etkisi = 0.45

            max_etki = max(self._tecrubeler.values()) # self._tecrubeler sözlüğünün değerlerini döndürür
            if max_etki == 0:
                return "İşsiz"
            elif max_etki * mavi_yaka_etkisi == max_etki:
                return "Mavi Yaka"
            elif max_etki * beyaz_yaka_etkisi == max_etki:
                return "Beyaz Yaka"
            elif max_etki * yonetici_etkisi == max_etki:
                return "Yönetici"
            else:
                return "Statü bulunamadı"
        except Exception as hata: # Hata oluşması durumunda hatayı yazdırır
            print("Hata bulundu:", hata)

    # str metodu ile bilgileri yazdırma
    def _str_(self):
        return super()._str() + f"Tecrubeler: {self._tecrubeler}\n"
