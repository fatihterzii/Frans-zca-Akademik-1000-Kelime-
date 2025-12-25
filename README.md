🇫🇷 Fransızca Akademik Kelime Ezberleme Uygulaması
Bu proje, akademik düzeyde Fransızca kelime dağarcığını geliştirmek isteyenler için Python ve PyQt5 kullanılarak geliştirilmiş bir masaüstü uygulamasıdır. Uygulama, kullanıcılara veritabanından rastgele seçilen kelimelerle çoktan seçmeli testler sunar.

📋 Özellikler
Geniş Veritabanı: SQLite veritabanı içerisinde yüzlerce akademik Fransızca kelime ve Türkçe karşılıkları.

Rastgele Soru Üretimi: Her turda veritabanından rastgele 5 kelime çekilir; bunlardan biri soru, diğerleri seçenek olarak sunulur.

Anlık Geri Bildirim: Cevap verildiğinde "Doğru" veya "Tekrar Deneyiniz" şeklinde anında dönüt verir.

Skor Takibi: Kullanıcının doğru cevaplarına göre 100 üzerinden puanlama yapar.

Kullanıcı Dostu Arayüz: Sade ve anlaşılır PyQt5 arayüzü.

🛠️ Kullanılan Teknolojiler
Python 3.x: Programlama dili.

PyQt5: Grafiksel kullanıcı arayüzü (GUI) kütüphanesi.

SQLite3: Kelime veritabanı yönetimi.

Random: Rastgelelik ve şans faktörleri için.

⚙️ Kurulum ve Çalıştırma
Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Gereksinimleri Yükleyin

Bu proje PyQt5 kütüphanesine ihtiyaç duyar. Eğer yüklü değilse terminal veya komut satırına şu komutu yazarak yükleyebilirsiniz:

Bash
pip install PyQt5
(Not: sqlite3 ve random modülleri Python ile yerleşik gelir, ekstra kurulum gerektirmez.)

2. Dosyaları Konumlandırın

uygulama.py (kod dosyası) ve kelimeler.db (veritabanı dosyası) dosyalarının aynı klasör içinde olduğundan emin olun.

3. Uygulamayı Başlatın

Terminali açın, projenin bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın:

Bash
python uygulama.py
📂 Dosya Yapısı
uygulama.py: Uygulamanın ana kaynak kodu. Arayüz tasarımı, veritabanı bağlantısı ve oyun mantığı burada bulunur.

kelimeler.db: Fransızca kelimelerin ve Türkçe karşılıklarının tutulduğu SQLite veritabanı dosyası.

🧠 Nasıl Çalışır?
Uygulama açıldığında "Kelime Getir" butonuna basılır.

Kod, veritabanına bağlanır ve ORDER BY RANDOM() LIMIT 5 komutu ile rastgele 5 kelime çifti çeker.

Bu 5 kelimeden rastgele biri "Soru" olarak belirlenir.

Diğer kelimelerin Türkçe karşılıkları şıklar (butonlar) üzerine yerleştirilir.

Kullanıcı doğru butona bastığında skor artar ve tebrik mesajı görünür.
