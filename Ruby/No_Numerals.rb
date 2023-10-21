digits = {"10"=>"ten","0"=>"zero","1"=>"one","2"=>"two",
            "3"=>"three","4"=>"four","5"=>"five",
            "6"=>"six","7"=>"seven","8"=>"eight","9"=>"nine"        
        }

text = gets.chomp
idx = nil
for wd in digits.keys 
    idx = text.index(wd)
    while (idx != nil) do
        text[wd] = digits[wd]
        idx = text.index(wd,idx+1)
    end
end
puts text