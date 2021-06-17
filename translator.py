from googletrans import Translator


class App_Translator:

    def translate(self, text:str, src:str, to:str) -> str:
        """
        this function translates text to a given language
        """
        translator = Translator()
        output = translator.translate(text,src=src, dest=to)
        return output.text


