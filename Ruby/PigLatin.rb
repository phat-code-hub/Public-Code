words=gets().chomp().split()
temp=[]
words.each {
    |w|
    temp <<(w[1..-1]+w[0]+"ay") 
}
pigLatin=temp.join(" ")
puts pigLatin