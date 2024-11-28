from deep_translator import GoogleTranslator

def translate_de2en(text):
    translated = GoogleTranslator(source='de', target='en').translate(text)
    return translated

def translate_en2de(text):
    translated = GoogleTranslator(source='en', target='de').translate(text)
    return translated



if __name__ == "__main__":
    text = "Weiter so, du bist großartig. Ich bin Giannis und ich komme aus griechenland. Jetzt lebe ich in Schweden"
    translated = translate_de2en(text)

    print(translated)