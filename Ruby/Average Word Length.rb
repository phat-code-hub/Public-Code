phrase= gets().chomp()
words=phrase.split(" ")
sum=0
words.each do |s|
    sum += s.length
end
cnt=phrase.count(" ")
avg=sum.to_f/(cnt+1)
if (avg >=3.5)
    puts avg.ceil
else
    puts avg.floor
end