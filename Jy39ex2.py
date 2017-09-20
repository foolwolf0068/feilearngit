'''
FishC
'''


# Jy40
class C:
    count = 0


def main():
        
    # 2
    a = C()
    b = C()
    c = C()
    c.count += 10 
    
    print("a.count=",a.count)
    print("b.count=",b.count)
    print("c.count=",c.count)
    print("C.count=",C.count)
    C.count += 100
    print("after  C.count += 100")
    print("a.count=",a.count)
    print("b.count=",b.count)
    print("c.count=",c.count) # shili shuxing
    print("C.count=",C.count)

if __name__ == "__main__":
    main()
