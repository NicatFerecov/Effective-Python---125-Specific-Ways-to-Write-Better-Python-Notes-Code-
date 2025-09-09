# Prefer Interpolated F-Strings over C-Style Format Strings and str.format

tarix: 8.09.2025

Biçimlendirme, önceden tanımlanmış metni veri değerleriyle birleştirerek, bir dize olarak depolanan, insan tarafından okunabilir tek bir mesaj haline getirme işlemidir. Python, dil ve standart kütüphaneye yerleşik dört farklı dize biçimlendirme yöntemine sahiptir.

## C-Style Formatting
'%' islediler.


Biçim dizesi, biçimlendirme ifadesinin sağ tarafındaki değerlerle değiştirilecek yer tutucular olarak biçim belirleyicileri (%d gibi) kullanır. Biçim belirleyicilerinin sözdizimi, Python (ve diğer programlama dilleri) tarafından miras alınan C dilinin printf işlevinden gelmektedir. Python, **%s**, **%x** ve **%f** format belirleyicileri gibi printf'ten bekleyebileceğiniz tüm olağan seçenekleri ve ondalık basamakları, dolgu, doldurma ve hizalama üzerinde kontrolü destekler.

Python'da C tarzı format dizgileriyle ilgili dört sorun vardır. İlk sorun, formatlama ifadesinin sağ tarafındaki tuple içindeki veri değerlerinin türünü veya sırasını değiştirirseniz, tür dönüştürme uyumsuzluğu nedeniyle hatalar alabilirsiniz.

C tarzı biçimlendirme ifadelerinin ikinci sorunu, değerleri bir dizeye biçimlendirmeden önce küçük değişiklikler yapmanız gerektiğinde okunması zor hale gelmeleridir ve bu, son derece yaygın bir ihtiyaçtır.

Biçimlendirme ifadeleriyle ilgili baska bir sorun ise, bir biçim dizisinde aynı değeri birden çok kez kullanmak istediğinizde, bunu sağdaki tuple'da tekrarlamanız gerekmesidir:
	template = "%s loves food. See %s cook."
	name = "Max"
	formatted = template % (name, name)
	print(formatted)

Bu, biçimlendirilen değerlerde küçük değişiklikleri tekrarlamak zorunda kalırsanız özellikle can sıkıcı ve hataya açık bir durumdur. Örneğin, burada bir referansta title() yöntemini çağırıyorum, ancak diğerinde çağırmıyorum, bu da uyumsuz çıktıya neden oluyor.

Python'daki % operatörü, tuple yerine sözlükle de biçimlendirme yapabilme özelliği sayesinde bu sorunların bazılarını çözmeye yardımcı olur. Sözlükteki anahtarlar, %(anahtar)s gibi aynı ada sahip biçim belirleyicilerle eşleştirilir


Biçimlendirme ifadelerinde sözlük kullanmak da ayrıntı düzeyini artırır ve bu, Python'da C tarzı biçimlendirme ifadelerinin 4 numaralı sorunudur. Her anahtar en az iki kez belirtilmelidir: bir kez biçim belirleyicide, bir kez sözlükte anahtar olarak ve muhtemelen bir kez daha sözlük değerini içeren değişken adı için.

## The format Built-in Function and str.format
Bu işlevi, str türünün yeni format yöntemini çağırarak birden fazla değeri birlikte biçimlendirmek için kullanabilirsiniz. %d gibi C tarzı format belirteçleri kullanmak yerine, **{}** ile yer tutucular belirtebilirsiniz. Varsayılan olarak, format dizesindeki yer tutucular, format yöntemine aktarılan karşılık gelen konumsal argümanlarla, göründükleri sırayla değiştirilir.

Bunun nasıl çalıştığını düşünmenin yolu, format belirleyicilerin değerle birlikte format yerleşik işlevine aktarılacağıdır (yukarıdaki örnekte format(value, “.2f”)). Bu işlev çağrısının sonucu, genel biçimlendirilmiş dizedeki yer tutucuyu değiştiren şeydir. __format__ özel yöntemini kullanarak sınıf başına biçimlendirme davranışını özelleştirebilirsiniz.
str.format ile dikkat edilmesi gereken bir diğer ayrıntı da köşeli parantezlerden ({) kaçınmaktır. Bunları yanlışlıkla yer tutucular olarak yorumlanmamaları için iki katına çıkarmalısınız ({{) (C tarzı biçim dizelerinde % karakterini doğru şekilde kaçınmak için iki katına çıkarmanız gerektiği gibi.

Köşeli parantezler içinde, yer tutucuyu değiştirmek için format yöntemine aktarılan bir argümanın konumsal indeksini de belirtebilirsiniz. Bu, format ifadesinin sağ tarafını da değiştirmenize gerek kalmadan çıktı sırasını yeniden düzenlemek için format dizesinin güncellenmesini sağlar ve böylece yukarıdaki 1 numaralı sorunu çözer.

Aynı konum dizini, değeri format yöntemine birden fazla kez aktarmaya gerek kalmadan format dizisinde birden fazla kez referans alınabilir, bu da yukarıdaki 3 numaralı sorunu çözer.

Bu eksiklikler ve C tarzı biçimlendirme ifadelerinden kaynaklanan sorunlar (yukarıdaki sorunlar #2 ve #4) göz önüne alındığında, genel olarak str.format yöntemini kullanmaktan kaçınmanızı öneririm. Biçim belirleyicilerde (iki nokta üst üste işaretinden sonraki her şey) kullanılan yeni mini dil ve format yerleşik işlevinin nasıl kullanıldığı hakkında bilgi sahibi olmak önemlidir. Ancak str.format yönteminin geri kalanı, Python'un yeni f-dizilerinin nasıl çalıştığını ve neden bu kadar harika olduklarını anlamanıza yardımcı olacak tarihi bir eser olarak değerlendirilmelidir.

## Interpolated Format Strings (F-String)
Python 3.6, bu sorunları kesin olarak çözmek için enterpolasyonlu format dizileri (kısaca f-dizileri) ekledi. Bu yeni dil sözdizimi, format dizisinin başına f karakteri eklemenizi gerektirir. Bu, bayt dizisinin başına b karakteri ve ham (kaçış karakteri içermeyen) dizinin başına r karakteri eklenmesine benzer.

Yeni formatın yerleşik mini dilindeki tüm seçenekler, f-string içindeki yer tutuculardaki iki nokta üst üste işaretinden sonra kullanılabilir. Ayrıca, str.format yöntemine benzer şekilde (yani !r ve !s ile) değerleri Unicode ve repr dizelerine zorlama özelliği de mevcuttur.
	formatted = f"{key!r:<10} = {value:.2f}"
	print(formatted)
	>>>
	'my_var'   = 1.23

F-dizileri ayrıca, yer tutucu parantezlerin içine tam bir Python ifadesi koymanıza olanak tanır ve yukarıdaki sorun #2'yi, biçimlendirilen değerlerde kısa bir sözdizimi ile küçük değişiklikler yapılmasına izin vererek çözer. C tarzı biçimlendirme ve str.format yöntemi ile birden fazla satır gerektiren işlemler artık tek bir satıra sığar.

## Hatırlanması Gerekenler
1. % operatörünü kullanan C tarzı format dizeleri, çeşitli tuzaklar ve ayrıntılılık sorunları ile karşı karşıyadır.
2. str.format yöntemi, biçimlendirme belirleyicileri mini dilinde bazı yararlı kavramlar getirir, ancak bunun dışında C tarzı biçimlendirme dizelerinin hatalarını tekrarlar ve kullanılmamalıdır.
3. F-dizileri, değerleri dizelere biçimlendirmek için kullanılan yeni bir sözdizimidir ve C tarzı biçim dizelerinin en büyük sorunlarını çözer.
4. F-dizileri, format belirleyicilere doğrudan rastgele Python ifadeleri yerleştirilmesine olanak tanıdıkları için kısa ama güçlüdür.