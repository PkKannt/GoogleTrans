import googletrans
from googletrans import Translator
print(googletrans.LANGUAGES)
t = Translator()
a = t.translate("chào",src="vi",dest="af")
#print(a.text)