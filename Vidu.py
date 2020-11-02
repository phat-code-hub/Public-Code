m=0
for i in range (100):
    r=i %22
    m=max(m,i-r)
    print(f"i={i}\tr={r}\t i-r: {i-r}\t m={m}")