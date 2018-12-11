
class I18N():
    ''' Internatiaonalization'''

    def __init__(self, language):
        if language == 'en' :self.resourceLanguageEnglish()
        elif language == 'de' : self.resourceLanguageGerman()
        else: raise NotImplementatError('Unsupported Language.')

    def resourceLanguageEnglish(self):
        self.title = "Python Graphical User Interface"

    def resourceLanguageGerman(self):
        self.title = "Python Grafische Benutzeroberflche"




if __name__=='__main__':
    language = 'en'
    inst = I18N(language)
    print(inst.title)

    language = 'de'
    inst = I18N(language)
    print(inst.title)
