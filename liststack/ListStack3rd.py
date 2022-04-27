from ListStack import*

def parenBalence(str):
    st=ListStack()
    idx=str.find('$')

    for i in range(idx):
        st.push(str[i])
        
    for i in range(idx+1,len(str)):
        first=st.pop()
        second=str[i]
        if first!=second:
            return False
    
    return True

def main():
    input="abc$cba"
    rv=parenBalence(input)
    if rv==True:
        print("Is included")
    else:
        print("Not included")

if __name__=="__main__":
    main()