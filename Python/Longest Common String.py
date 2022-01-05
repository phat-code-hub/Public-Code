#List up all available search keywords 
def search_words_list(data):
    sub_str=[]
    #Find the shortest word in list
    min_wd=min(data, key=len)
    #expand keyword for search
    for i in range(len(min_wd)):
        for j in range(i+1,len(min_wd)+1):
            sub_str.append(min_wd[i:j])
    #Sort result by the length in descendent order
    len_sorted_list=sorted(sub_str,key=len,reverse=True)
    return len_sorted_list
#------------------------------------------------------
# if all words contain keyword return true, all count results are greater or equal 1
def Find(word,data):
    search_Result=[s.count(word) for s in data]
    return all(x>=1  for x in search_Result)
#------------------------------------------------------
words= input('Chuoi: ').strip().split()
search_List=search_words_list(words)
#loop searching from the longest keyword, if found stop and print
for keyword in search_List:
    if Find(keyword,words):
        print(keyword)
        break