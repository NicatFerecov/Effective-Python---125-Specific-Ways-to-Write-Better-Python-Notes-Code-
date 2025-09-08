# know the Differences Between bytes and str

Python'da, karakter verilerinin dizilerini temsil eden iki tür vardır: bytes ve str. Bytes örnekleri, ham, işaretsiz 8 bitlik değerler içerir **(genellikle ASCII kodlamasında görüntülenir)**


		a = b"h\x65llo"
		print(type(a))
		output:
			<class 'bytes'>

str örnekleri, insan dillerindeki metin karakterlerini temsil eden Unicode kod noktalarını içerir:
	Önemli olarak, bir str örneği ilişkili bir ikili kodlamaya sahip değildir ve bir bytes örneği ilişkili bir metin kodlamasına sahip değildir. Unicode verilerini ikili verilere dönüştürmek için str'nin encode yöntemini çağırmanız gerekir. İkili verileri Unicode verilerine dönüştürmek için bytes'ın decode yöntemini çağırmanız gerekir. Bu yöntemler için kullanmak istediğiniz kodlamayı açıkça belirtebilir veya genellikle UTF-8 olan sistem varsayılanını kabul edebilirsiniz.

Python programları yazarken, Unicode verilerinin kodlamasını ve kod çözmesini arayüzlerinizin en uzak sınırında yapmak önemlidir; bu yaklaşım genellikle Unicode sandviçi olarak adlandırılır. Programınızın çekirdeği, Unicode verilerini içeren str türünü kullanmalı ve karakter kodlamaları hakkında herhangi bir varsayımda bulunmamalıdır. Bu yapılandırma, çıktı metin kodlaması konusunda katı davranırken (ideal olarak UTF-8), alternatif metin kodlamalarını (Latin-1, Shift JIS ve Big5 gibi) kolayca kabul etmenizi sağlar.

Karater veri türleri arasındakı ayrımı Pythonda iki yaygın duruma yol açıyor:
	1. UTF-8 kodlu dizeler (veya başka bir kodlama) içeren ham 8 bit diziler üzerinde işlem yapmak istiyorsunuz.
	2. Belirli bir kodlaması olmayan Unicode dizeleri üzerinde işlem yapmak istiyorsunuz.


Python'da ham 8 bit değerler ve Unicode dizeleriyle çalışırken iki önemli husus vardır.

İlk sorun, *bytes* ve *str*'nin aynı şekilde çalışıyor gibi görünmesi, ancak bunların örneklerinin birbirleriyle uyumlu olmamasıdır. Bu nedenle, aktardığınız karakter dizilerinin türleri konusunda dikkatli olmalısınız.


byte ile byte ve str ile str birleştire bilirsiniz:
	print(b"one" + b"two")
	print("one" + "two")
hata vermez.

ama byte ile stringi birleştirmeye çalışırsanız:
	b"one" + "two"
	output:
		Traceback ...
		TypeError: can't concat str to bytes
Byte ve str örneklerinin eşitliğini karşılaştırmak, tam olarak aynı karakterleri içerdiklerinde bile (bu durumda ASCII kodlu “foo”) her zaman False sonucunu verir:

## Hatırlanması gerekenler
1 - *bytes*, 8 bitlik değer dizilerini içerir ve *str*, Unicode kod noktası dizilerini içerir.
2 - Yardımcı işlevleri kullanarak, üzerinde işlem yaptığınız girdilerin beklediğiniz karakter dizisi türü olduğundan emin olun (8 bit değerler, UTF-8 kodlu dizeler, Unicode kod noktaları vb.).
3 - *bytes* ve *str* örnekleri operatörlerle (>, ==, + ve % gibi) birlikte kullanılamaz.
4 - Bir dosyadan ikili verileri okumak veya dosyaya ikili verileri yazmak istiyorsanız, dosyayı her zaman ikili modda (örneğin “rb” veya “wb”) açın.
5 - Bir dosyaya Unicode verilerini okumak veya yazmak istiyorsanız, sisteminizin varsayılan metin kodlamasına dikkat edin. Sürprizlerle karşılaşmamak için kodlama parametresini açıkça open işlevine aktarın.