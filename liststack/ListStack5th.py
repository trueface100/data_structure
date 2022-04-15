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

input="(abc)"
parenBalence(input)

def main():
    input="(abc)(abccdd)"
    parenBalence(input)

if __name__=="__main__":
    main()

