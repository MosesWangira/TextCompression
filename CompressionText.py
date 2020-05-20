#Python script for compression of text using lossy method
#Not advisable for texts but I use it as a stepping stone
TextToCompress = input("Enter your sentence : ") 

def compression(original):
    result = ""
    for i in range(len(original)):
        charactor = original[i]
        if(charactor not in ('a','e','i','o','u')):
           result += charactor
    print(result)
print("*********Compressing******")
compressed = compression(TextToCompress)

#example
#Input : Hey I love you dont leave me
#Output : Hy I lv y dnt lv m
