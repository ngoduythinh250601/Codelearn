int findString(String mainString, String findString) {
    int l = findString.length();
    int c= 0;
    for (int i = 0;i<=mainString.length()-l;i++){
        if (mainString.substring(i,i+l).equals(findString)){
            c++;
        }
    }
    return c;
}