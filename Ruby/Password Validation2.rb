SPECIALCHARS="!@#$%&*"
NUMBERS=(0..9).to_a.join()
words =gets.chomp().strip()
is_Number=words.each_char.filter {
    |x|
    NUMBERS.include? x
}
is_punctuation=words.each_char.filter {
    |s|
    SPECIALCHARS.include? s
}
puts (words.size >=7 && is_Number.size >=2 && is_punctuation.size >=2)? "Strong":"Weak"