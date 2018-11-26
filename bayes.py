import math
import string

class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha=alpha     

    def fit(self,X, y):
        """
         Fit Naive Bayes classifier according to X, y. """
        self.classifier=[]
        X = [clean(x).lower() for x in X]
        for i in range(len(set(y))):
            self.classifier.append({list(set(y))[i]:{}})
        for message in X:
            for i in range(len(self.classifier)):
                for j in self.classifier[i]:
                    if y[X.index(message)] in self.classifier[i]:
                        words=message.split()
                        for word in words:
                            if word in self.classifier[i][j]:
                                self.classifier[i][j][word]+=1
                            else:
                                self.classifier[i][j][word]=1
        return self.classifier

    def predict(self,X_test):
        """ Perform classification on an array of test vectors X. """
        classvalues=[]
        self.new_XY=[]
        max_i=0
        timesword={}
        totalwords=0
        for i in range(len(self.classifier)): # 0,1
            for j in self.classifier[i]: # j = spam/ham
                classvalues.append(len(self.classifier[i][j]))
                print(classvalues)
                totalwords += len(self.classifier[i][j])
        for message in X_test:
            imessage=set(message.split())
            for i in range(len(self.classifier)):
                for j in self.classifier[i]:
                    for word in imessage:
                        timesword[word]=0
            for i in range(len(self.classifier)):
                for j in self.classifier[i]:
                    for word in imessage:
                        if word in self.classifier[i][j]:
                            timesword[word]+=self.classifier[i][j][word]
            max=-12452
            for i in range(len(self.classifier)):
                for j in self.classifier[i]:
                    result=math.log(classvalues[i]/totalwords)
                    for word in imessage:
                        if timesword[word]==0:
                            wordint=0
                        elif word in self.classifier[i][j]:
                            wordint=math.log((self.classifier[i][j][word]+self.alpha)/(classvalues[i]+totalwords))
                        else:
                            wordint=math.log((0+self.alpha)/(classvalues[i]+totalwords))
                        result+=wordint
                    if result>max:
                        max=result
                        max_i=i
            self.new_XY.extend([z for z in self.classifier[max_i]])
        return self.new_XY

    def score(self,y_test):  
        """ Returns the mean accuracy on the given test data and labels. """
        bottom=len(y_test)
        up=0
        for l in range(len(new_XY)):
            if self.new_XY[l]==y_test[l]:
                up+=1
        return up/bottom

def clean(s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)


            
