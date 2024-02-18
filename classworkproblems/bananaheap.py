def getkokoeatenbanannatome(k,bananaheap):
    timeTaken=0
    for i in range(0,len(bananaheap)):
        hrsTaken=bananaheap[i]//k
        if bananaheap[i]%5==0:
         timeTaken+=hrsTaken
         
        else:
           timeTaken+=hrsTaken+1
    print(timeTaken)   
getkokoeatenbanannatome(5,[21,6,12])