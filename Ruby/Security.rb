pattern=/\$(x)*T|T(x)*\$/
pw=gets().chomp()
if (pattern.match(pw))
    puts "ALARM"
else
    puts "quiet"
end