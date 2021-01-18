colors=[]
3.times do 
    |n|
    colors[n]=gets.chomp().to_i
    colors[n]=colors[n].to_s(16)
end
color_Hex_Value=colors.inject("#"){ |x,y|
    x+y
}
puts color_Hex_Value