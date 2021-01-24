words=gets().chomp().split(" ")
dau=words.collect {
    |w|
    w[0].downcase
}
cuoi=words.collect {
    |w|
    w[-1].downcase
}
dau=dau[1..-1]
cuoi=cuoi[0..-2]
p dau == cuoi