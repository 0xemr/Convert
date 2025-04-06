# Belge Dönüştürücü

Bu program, DOC/DOCX dosyalarını PDF'e ve PDF dosyalarını DOC formatına dönüştürmenizi sağlar.

## Kurulum

1. Python'un bilgisayarınızda kurulu olduğundan emin olun.
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install docx2pdf
pip install pdf2docx
```

## Kullanım

1. Programı çalıştırın:
```bash
python doc_pdf_converter.py
```

2. Açılan arayüzde dönüştürme tipini seçin:
   - DOC -> PDF: Word dosyasını PDF'e dönüştürür
   - PDF -> DOC: PDF dosyasını Word dosyasına dönüştürür

3. "Dosya Seç" butonuna tıklayarak dönüştürmek istediğiniz dosyayı seçin.

4. Dönüştürme işlemi otomatik olarak başlayacak ve tamamlandığında size bilgi verilecektir.

## Notlar

- Dönüştürülen dosyalar, orijinal dosya ile aynı klasöre kaydedilir.
- Dosya adı aynı kalır, sadece uzantısı değişir.
- Program hem .doc hem de .docx formatlarını destekler. 