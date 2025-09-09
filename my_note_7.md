# Prefer Catch-All Unpacking over Slicing

tarix: 9.09.2025


	oldest, second_oldest, *others = car_ages_descending
	print(oldest, second_oldest, others)
Bu kod daha kısa, okunması daha kolay ve satırlar arasında senkronize tutulması gereken sınır indekslerinin hataya açık kırılganlığı artık yok.
Yıldızlı bir ifade herhangi bir konumda (başlangıç, orta veya son) görünebilir, böylece isteğe bağlı bir dilimi ayıklamanız gerektiğinde her zaman her şeyi kapsayan açma işleminin avantajlarından yararlanabilirsiniz.
Ancak, açma atamasında yıldızlı ifade kullandığınızda, en az bir zorunlu parçaya sahip olmanız gerekir, aksi takdirde sözdizimi hatası alırsınız. Tek başına her şeyi kapsayan ifadeyi kullanamazsınız.
# Example:
	*others = car_ages_descending
	>>>
	Traceback ...
	SyntaxError: starred assignment target must be in a list or tuple
*Note*: Tek bir açma deseninde birden fazla genel ifade kullanamazsınız.
Yıldız işaretli ifadeler her durumda liste örnekleri haline gelir. Açılan diziden kalan öğe yoksa, her şeyi kapsayan kısım boş bir liste olacaktır.
Ancak, yıldızlı bir ifade her zaman bir listeye dönüştürüldüğü için, bir yineleyiciyi açmak bilgisayarınızın tüm belleğini tüketme ve programınızın çökmesine neden olma riskini de beraberinde getirir Bu nedenle, sonuç verilerinin tümünün belleğe sığacağına inanmak için iyi bir nedeniniz olduğunda yineleyicilerde her şeyi içeren açma işlemini kullanmalısınız.

## Hatırlanması Gerekenler
1. Paket açma atamaları, paket açma deseninin diğer bölümlerine atanmamış tüm değerleri bir listede depolamak için yıldızlı bir ifade içerebilir.
2. Yıldız işaretli ifadeler, açma deseninin herhangi bir konumunda görünebilir. Bunlar her zaman sıfır veya daha fazla değer içeren bir liste örneği haline gelir.
3. Bir listeyi üst üste binmeyen parçalara bölerken, her şeyi kapsayan açma işlemi, dilimleme ve indeksleme yapan ayrı ifadeler kullanmaktan çok daha az hataya meyillidir.