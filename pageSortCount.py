from quickSort import*
from quicksortlambda import*


def do_sort(input_file):

    data_file=open(input_file)
    A=[]
    B=[0]
    k=0
    d=dict()
    for line in data_file.readlines():
        lpn=line.split()[0]
        A.append(lpn)

    quickSort(A,0,len(A)-1)

    for i in range(len(A)-1):
        B[k]+=1
        if A[i]!=A[i+1]:
            d[A[i]]=B[k]
            B.append(0)
            k+=1

    keys=list(d.keys())
    values=list(d.values())

    # quickSort(values,0,len(values)-1)
    # d1=sorted(d.items(),key=lambda x:x[1],reverse=True)
    # quicksortlambda(values,keys,0,len(d)-1)

    for i in range(10):
        print(keys[i])
        print(values[i])

    # for i in range(10):
    #     print(d1[i])
    # print("")

if __name__=="__main__":
    do_sort("linkbench_short.trc")
