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
        self.Expressions["thank you very much"]='https://media1.giphy.com/media/3o7TKUtetZv6DGRJxS/giphy.gif?cid=ecf05e47rrt57aebgircjl0kmgmmxpu80nm9f0lmxbc51eht&rid=giphy.gif&ct=g'
        self.Expressions["you are welcome"]='https://media0.giphy.com/media/3o7TKSRNcdPmcNmTGo/giphy.gif?cid=ecf05e47wp1jhy9wr58pb84j14nkls7i5lp51p3mtrhg5jq1&rid=giphy.gif&ct=g'
        self.Expressions["i don't understand"]='https://media4.giphy.com/media/26FL0X4d3Epuecpj2/giphy.gif?cid=ecf05e47kpj74239361piio12y30e5q5q526b9bwa38hlh1o&rid=giphy.gif&ct=g'
        self.Expressions["i dont know"]='https://media1.giphy.com/media/3oz8xwkWxsh3gQd4EE/giphy.gif?cid=ecf05e47hb5wcfetcf4cphmmu9xpa8eab5f8w0il94pu43u4&rid=giphy.gif&ct=g'
        self.Expressions["when is class finished"]='https://media3.giphy.com/media/l4JzaqiqnK8dnSryU/giphy.gif?cid=ecf05e47r8635sh2u1dunf6zmrk830emlspp71wq3nuct4qb&rid=giphy.gif&ct=g'
        self.Expressions["are you all right"]='https://i.pinimg.com/originals/20/be/d9/20bed9cc1a937486397e64ca2cde78ca.gif'
        self.Expressions["how much does it cost"]='https://www.indy100.com/media-library/image.gif?id=28084368&width=776&quality=80'
        self.Expressions["where is the restroom"]='https://i.pinimg.com/originals/c0/32/07/c03207aa7f0a7c874a8c63a838edabe2.gif'
        self.Expressions["plese help me"]='https://i.gifer.com/7HLz.gif'
        self.Expressions["Soon to come"]='https://c.tenor.com/SBaHXwhhIbMAAAAM/coming-soon.gif'



def GetUrlforWord(self,word):
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
        
        
    def GetUrlforPhrase(self,Phrase):
        #a word should come in as a single word but just incase i will set up a split with spaces and choose the first index 
        if(len(Phrase)<1):
            return ""#this is where we return word will be added soon
        
        if(self.Expressions.get(Phrase.toLowerCase())):
                #now determine if the word is in our database
            return self.Expressions[Phrase]
        else:
            return "Word is not in english dictionary"        