# Prefer Explicit String Concatenation over Implicit, Especially in Lists

tarix: 9.09.2025


+ operatörü mevcut olduğunda, otomatik biçimlendirici satır sonunu yine de değiştirebilir, ancak bu durumda en azından kodun yazarının asıl amacının ne olduğu açıktır.
	örnek:
		my_test6 = [
	    "first line\n",
	    "second line\n" + "third line\n",
	]

Benim tavsiyem, herhangi bir karışıklığı önlemek için, bir işlev çağrısı birden fazla konumsal argüman aldığında her zaman açık dize birleştirme kullanmanızdır Yukarıdaki print örneğinde olduğu gibi tek bir konumsal argüman varsa, örtük dize birleştirme kullanmak uygundur. Anahtar kelime argümanları, açıklığı en üst düzeye çıkaran açık veya örtük birleştirme kullanılarak aktarılabilir, çünkü kardeş dize sabitleri = karakterinden sonra konumsal argümanlar olarak yanlış yorumlanamaz.

## Hatırlanması Gerekenler
1. Python kodunda iki string literal birbirinin yanında yer aldığında, C programlama dilindeki örtük string birleştirme özelliğine benzer şekilde, aralarında **+** operatörü varmış gibi birleştirilirler.
2. Liste ve tuple literal'larındaki öğelerin örtük olarak birleştirilmesinden kaçının, çünkü bu, orijinal yazarın niyetine dair belirsizlik yaratır. Bunun yerine, + operatörüyle açık birleştirme kullanmalısınız.
3. İşlev çağrılarında, bir konumsal argüman ve herhangi bir sayıda anahtar kelime argümanı ile örtük dize birleştirme kullanmak uygundur, ancak birden fazla konumsal argüman olduğunda açık birleştirme kullanmalısınız.
