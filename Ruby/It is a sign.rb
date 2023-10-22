str=[]
4.times {
    str.push(gets.chomp)
}
def panlindrome(st)
    st_rev=st.reverse
    return st.eql?(st_rev)
end
ans="Trash"
str.each do |word|
    next if(!panlindrome(word))
    ans="Open"
    break
end
puts ans