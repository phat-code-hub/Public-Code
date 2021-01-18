WAITING_TIME=20;
name=gets().chomp()
agents=gets().to_i
peoples=gets().chomp().split(" ");
peoples<<name
my_order= peoples.sort!.index(name)
my_group=my_order / agents
puts (my_group+1)*WAITING_TIME