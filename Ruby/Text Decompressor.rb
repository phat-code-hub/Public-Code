$text = gets().chomp
$len  =$text.length
$tumoi=Array.new

$numset =('0'..'9')
def isNum(n)
    return $numset.include?(n)
end

def findNum(index)
    num =""
    for j in index...$len
        if isNum($text[j])
            num += $text[j]
            if (j+1 == $len) 
                return num
            end
        else
            return num
        end
    end
end

# $charset = ('a'..'z').chain('A'..'Z')
i =0
while (i<$len)
    if isNum($text[i])
        temp = findNum(i)
        lastItem = $tumoi.pop()
        $tumoi << lastItem*(temp.to_i) 
        i = i+temp.length()
    else
        $tumoi << $text[i]
        i +=1
    end
end
puts $tumoi.join("")