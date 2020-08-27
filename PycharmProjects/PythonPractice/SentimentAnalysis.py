from textblob import TextBlob
y=input("Type your sentence : ")
edu=TextBlob(y)
x=edu.sentiment.polarity
#Negative -> x<0 , Neutral -> x=0 ,
if x<0:
    print("Negative")
elif x==0:
    print("Neutrak")
elif x>0 and x<=1:
    print("Positive")