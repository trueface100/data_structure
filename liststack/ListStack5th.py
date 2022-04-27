from ListStack import*

def parenBalence(str):
    st=ListStack()
    for i in range(len(str)):
        if str[i] == '(':
            st.push(str[i])
        elif str[i]==')':
            if st.isEmpty():
                return False
            else:
                st.pop()
    if st.isEmpty():
        return True
    else:
        return False

def main():
    input="(abc)(abccdd)"
    rv=parenBalence(input)
    if rv==True:
        print("True")
    else:
        print("False")

if __name__=="__main__":
    main()