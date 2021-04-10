def almostIncreasingSequence(sequence):

    count = 0 
    i =0
    size = len(sequence)
    if(sequence[0]>sequence[1]):
        sequence.pop(0)
        count+=1
        size-=1
    while(i<size-1):
        if sequence[i]>=sequence[i+1]:
            count+=1
            if(sequence[i+1]<=sequence[i-1]):
                sequence.pop(i+1)
            else:
                sequence.pop(i)
            size = len(sequence)
            if i>0:
                i-=1
    
        else:
            i+=1
    if count>1:
        return False
    else:
        return True
