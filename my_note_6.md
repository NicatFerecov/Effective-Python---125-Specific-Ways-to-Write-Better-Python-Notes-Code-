# Avoid Striding and Slicing in a Single Expression

tarix: 9.09.2025

Temel dilimleme işlemine ek olarak Python, somelist **[start:end:stride]** biçiminde bir dilimin adım uzunluğu için özel bir sözdizimi içerir. Bu, bir diziyi dilimlerken her n'inci öğeyi almanızı sağlar. Örneğin, adım uzunluğu, bir listedeki çift ve tek sıra numaralarına göre gruplandırmayı kolaylaştırır.

*example:*
	Burada, ::2 **“Başlangıçtan itibaren her ikinci öğeyi seç”** anlamına gelir. Daha karmaşık olan ::-2 ise **“Sonundan başlayarak geriye doğru her ikinci öğeyi seç”** anlamına gelir.
*2::2* ne anlama gelir?  Ve *-2::-2, -2:2:-2 ve 2:2:-2* arasındaki fark nedir?
*example:*
	x[2::2]     # ["c", "e", "g"]
	x[-2::-2]   # ["g", "e", "c", "a"]
	x[-2:2:-2]  # ["g", "e"]
	x[2:2:-2]   # []

	output:
	>>>
	['c', 'e', 'g']
	['g', 'e', 'c', 'a']
	['g', 'e']
	[]
Adım kullanmanız gerekiyorsa, pozitif bir değer tercih edin ve başlangıç ve bitiş indekslerini atlayın. Başlangıç veya bitiş indeksleriyle adım kullanmanız gerekiyorsa, adımlama için bir atama ve dilimleme için başka bir atama kullanmayı düşünün.

## Hatırlanması Gerekenler
1. Başlangıç, bitiş ve adım uzunluğunu tek bir dilimde birlikte belirtmek son derece kafa karıştırıcı olabilir.
2. Adım atmak gerekiyorsa, başlangıç veya bitiş indeksleri olmadan yalnızca pozitif adım değerlerini kullanmaya çalışın; negatif adım değerlerinden kaçının.
3. Tek bir dilimde başlangıç, bitiş ve adım uzunluğu gerekiyorsa, iki atama yapmayı (biri adım uzunluğu, diğeri dilimleme için) veya itertools yerleşik modülünden islice kullanmayı düşünün.