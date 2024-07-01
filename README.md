# Netflix_Clone_Django

Bu proje, Python, Django ve JavaScript kullanarak geliştirilmiş bir Netflix klonudur. Proje, kullanıcıların filmleri keşfetmesini, izleme listeleri oluşturmasını ve film detaylarını görüntülemesini sağlar.

## Özellikler

- Kullanıcı kaydı ve girişi
- Film keşfi ve arama
- İzleme listesi oluşturma
- Film detayları görüntüleme
- Kullanıcı profili yönetimi

## Kullanılan Teknolojiler

- **Backend:** Python, Django
- **Frontend:** JavaScript, HTML, CSS
- **Veritabanı:** SQLite (veya tercihe bağlı başka bir veritabanı)

## Kurulum

### Gereksinimler

- Python 3.x
- Django 3.x

### Adımlar

1. Bu repository'i klonlayın:

    ```bash
    git clone https://github.com/kullaniciadi/netflix-clone.git
    cd netflix-clone
    ```

2. Sanal bir ortam oluşturun ve etkinleştirin:

    ```bash
    python -m venv env
    source env/bin/activate # MacOS/Linux
    env\Scripts\activate # Windows
    ```

3. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Django veritabanı migrasyonlarını yapın:

    ```bash
    python manage.py migrate
    ```

5. Gerekli JavaScript bağımlılıklarını yükleyin:

    ```bash
    npm install
    ```

6. Django geliştirme sunucusunu başlatın:

    ```bash
    python manage.py runserver
    ```

7. Tarayıcınızda projeyi görüntüleyin:

    ```
    http://localhost:8000
    ```

## Kullanım

- **Kayıt ve Giriş:** Kullanıcılar, hesap oluşturabilir ve giriş yapabilir.
![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/5ce77968-015c-4d6d-8984-c9847757f517)
![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/bd7ad1c6-4859-47c6-9ab9-52279d883b43)

- **Film Keşfi:** Ana sayfada mevcut filmleri görüntüleyebilir ve arama yapabilirsiniz.
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/729786f0-4b09-432f-8317-8abaf37df76f)
  
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/326283ef-65bd-475b-b2ed-51c322c8d201)

  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/0db57a94-e388-41bc-99ee-1aac3569fa2b)

  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/1488ada3-3549-4abe-b2e2-e9d28c7dda07)
  
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/030645ac-26c2-458f-8973-fb0fbf2f74f0)


- **İzleme Listesi:** Beğendiğiniz filmleri izleme listenize ekleyebilirsiniz.
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/079a38a7-6e49-4d51-8273-347fadd1c9c1)
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/778e2155-6a56-4bf5-802f-f9286bf48976)
 
- **Film Detayları:** Her film için detaylı bilgi ve özet görüntüleyebilirsiniz.
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/079a38a7-6e49-4d51-8273-347fadd1c9c1)
  ![image](https://github.com/GorkemKurtkaya/Netflix_Clone_Django/assets/115563271/33e89f47-1c08-4129-888b-aa337beeca2b)



## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Bu repository'i fork edin.
2. Yeni bir dal (branch) oluşturun: `git checkout -b feature/ozellik-adi`
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Yeni özellik eklendi'`
4. Dalınıza (branch) push edin: `git push origin feature/ozellik-adi`
5. Bir pull request açın.


## İletişim

Bu proje hakkında sorularınız varsa, lütfen [gorkem.kurtkaya@yahoo.com] adresinden bana ulaşın.
