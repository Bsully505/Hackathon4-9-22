from spellchecker import SpellChecker
class Conversion:
    words={}
    Expressions={}
    check=None 
    def __init__(self):
        self.check = SpellChecker
        self.words['Weekend']='https://media3.giphy.com/media/l0MYxci0TrPAtdI4M/giphy.gif'#insert url 
        self.words['Goodbye']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        self.words['Hello']=''#insert url 
        
        self.Expressions["how are you doing"]='https://media0.giphy.com/media/26FLgm33ve3iUexZC/giphy.gif?cid=790b7611f3ec61ce1016d81b6689aceace595ec079fb4258&rid=giphy.gif&ct=g'
        self.Expressions["i want"]='https://media0.giphy.com/media/26FKXlsvBJoMuyE0g/200w.webp'
        self.Expressions["i like it"]='https://media4.giphy.com/media/26FLetDV4MHaixWHm/200w.webp'
        self.Expressions["i dont like this"]='https://media2.giphy.com/media/l4Jzdp8TJ2DDxeVna/200w.webp'

    def GetUrl(self,word):
        #a word should come in as a single word but just incase i will set up a split with spaces and choose the first index 
        query1 = word.split(' ')[0]
        if(len(query1)<1):
            return "Invalid word"
        if(self.check.known(query1)==query1):
            if(self.dict.get(word)):
                #now determine if the word is in our database
                return self.dict[word]
        else:
            return "Word is not in english dictionary"
        