def sum(ar):
        
    total = 0
    
    for i in ar:
        total = total + i
    
    # return(total)
    
    print(total)

if __name__ == '__main__':
    
    ar = [1,2,1,2,1,3,2,4,4,4,6]

    sum(ar)