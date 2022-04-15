from LinkedStack import*

def reverse(str):
    st=LinkedStack()
    for i in range(len(str)):
        st.push(str[i])
    out=""
    while not st.isEmpty():
        out+=st.pop()
    return out

def main():
    w=input()
    answer=reverse(w)
    print("Input string: ",w)
    print("Reversed string: ",answer)

if __name__=="__main__":
    main()