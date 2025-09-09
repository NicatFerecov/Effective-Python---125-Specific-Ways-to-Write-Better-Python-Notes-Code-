# Understand the Difference Between repr and str when Printing Objects

tarix: 9.09.2025

**Repr**:
	Hata ayıklama sırasında neredeyse her zaman istediğiniz şey, bir nesnenin repr sürümünü görmektir. repr yerleşik işlevi, bir nesnenin yazdırılabilir temsilini döndürür; bu, nesnenin en açık şekilde anlaşılabilir dize serileştirilmesi olmalıdır. Birçok yerleşik tür için, repr tarafından döndürülen dize geçerli bir Python ifadesidir.
	misal: *code_3.py*
Bu, **%** operatörüyle **“%r”** format dizesi veya **!r** tür dönüştürmeyle **f-dizesi** kullanmaya eşdeğerdir:


## Hatırlanması Gerekenler
1. Yerleşik Python türlerinde print işlevini çağırmak, tür bilgilerini gizleyen, insan tarafından okunabilir bir değer dizesi üretir.
2. Python'un yerleşik türleri üzerinde repr işlevini çağırmak, bir değerin yazdırılabilir temsilini içeren bir dize üretir. repr dizeleri genellikle eval yerleşik işlevine aktarılarak orijinal değer geri alınabilir.
3. %s biçim dizeleri, str gibi insan tarafından okunabilir dizeler üretir. %r, repr gibi yazdırılabilir dizeler üretir. F-dizeleri, !r dönüştürme sonekini belirtmediğiniz sürece, değiştirme metin ifadeleri için insan tarafından okunabilir dizeler üretir.
4. Sınıflarınızda __repr__ ve __str__ özel yöntemlerini tanımlayarak, örneklerin yazdırılabilir ve insan tarafından okunabilir temsilini özelleştirebilirsiniz. Bu, hata ayıklamaya yardımcı olabilir ve nesnelerin insan arayüzlerine entegrasyonunu basitleştirebilir.