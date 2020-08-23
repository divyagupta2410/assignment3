#1.1
def myfilter(func, seq):
    result = []
    for i in seq:
        if func(i):
            result.append(i)
    return result


#1.2
def myreduce(func,seq):
    result=seq[0]
    for i in seq[1:]:
        result= func(result,i)
    return result

#2
#a
l=[i*j for i in ['x','y','z'] for j in range(1,5)]
print(l)
#b
l=[ j*i for i in range(1,5) for j in ['x','y','z']]
print(l)
#c
l=[i for i in 'ACADGILD' ]
print(l)

#d
l=[[i+j for i in [2,3,4,5]] for j in range(0,4)]
print(l)
#e
l=[(j,i) for i in [1,2,3] for j in [1,2,3]]
print(l)

