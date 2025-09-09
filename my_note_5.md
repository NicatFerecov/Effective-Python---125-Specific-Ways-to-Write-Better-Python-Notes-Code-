# Know How to Slice Sequences

tarix: 9.09.2025

Dilimleme sözdiziminin temel biçimi somelist **[başlangıç:bitiş]** şeklindedir; burada başlangıç dahil, bitiş hariçtir:
*Not: başlangıç dahil, bitiş hariçtir.*

Bir dizinin sonuna kadar dilimleme yaparken, son indeksi gereksiz olduğu için dışarıda bırakmalısınız.

*Not:*
Bir listeyi negatif bir değişkenle indekslemek, dilimleme işleminden şaşırtıcı sonuçlar alabileceğiniz birkaç durumdan biridir. Örneğin, somelist[-n:] ifadesi, n sıfırdan büyük olduğunda (örneğin, n 3 olduğunda somelist[-3:]) düzgün çalışır. Ancak, n sıfır olduğunda, somelist[-0:] ifadesi somelist[] ile eşdeğerdir ve bu da orijinal listenin bir kopyasını oluşturur.

Bir listeyi dilimleme işleminin sonucu, tamamen yeni bir listedir. Yeni listedeki her bir öğe, orijinal listedeki karşılık gelen nesnelere başvurur. Dilimlemeyle oluşturulan listeyi değiştirmek, orijinal listenin içeriğini etkilemez.

Dilimleme yaparken başlangıç ve bitiş indekslerini dışarıda bırakırsanız, orijinal listenin tamamının bir kopyası elde edersiniz.


## Hatırlanması Gerekenler
1. Dilimleme yaparken fazla ayrıntıya girmeyin: Başlangıç dizini için 0 veya bitiş dizini için dizinin uzunluğu değerini vermeyin.
2. Dilimleme, sınırların dışında kalan başlangıç veya bitiş indekslerini kabul eder, bu da bir dizinin ön veya arka sınırlarında dilimleri ifade etmenin kolay olduğu anlamına gelir (örneğin, a[:20] veya a[-20:]).
3. Bir liste dilimine atama yapmak, uzunlukları farklı olsa bile orijinal dizideki o aralığı referans verilenle değiştirir.