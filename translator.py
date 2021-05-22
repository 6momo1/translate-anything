from googletrans import Translator

translator = Translator()

output = translator.translate("this is a test",dest="zh-cn")

print(output.text)


