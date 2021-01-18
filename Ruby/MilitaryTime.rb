require 'time'
tmm=gets().chomp()
tm=Time.parse(tmm)
puts tm.strftime("%H:%M")