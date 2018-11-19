def olpalindrome(mystring):
    revstring=mystring[::-1]
    if len(mystring)==1:
        return (mystring)
    else:
        for i in range(int(len(mystring)/2)):
            if (mystring[i:len(mystring)-i] == revstring[i:len(mystring)-i]):
                if ((len(mystring)-2*i)%2!=0):
                    return(mystring[i:len(mystring)-i])
    return("No odd length palindrome found")

print(olpalindrome("aabcnonddcc"))
