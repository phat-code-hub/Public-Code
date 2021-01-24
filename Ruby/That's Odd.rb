n=gets().to_i;
num=[];
for i in (1..n)
    num<<gets().chomp().to_i
end
even_list=num.select{|n| n%2==0}
puts even_list.sum