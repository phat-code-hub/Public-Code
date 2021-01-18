message=gets().chomp()
spyLife=""
message.each_char {
    |c|
    if (('A'..'Z').include?(c)||('a'..'z').include?(c) || c == ' ')
        spyLife.insert(0,c)
    end
}
puts spyLife