'''
FishC  Jy 40
'''

class A:
    pass

class B(A):
    pass
class C:
    pass


def main():
    # issubclass
    print(issubclass(B, A))
    print(issubclass(B, B))
    print(issubclass(A, object))
    print(issubclass(B, object))

    print(issubclass(C, A))
    print(issubclass(C, B))
    print(issubclass(C, object))
    
    # isinstance
    b1 = B()
    
    print(isinstance(b1, B))
    print(isinstance(b1, A))
    print(isinstance(b1, C))
    print(isinstance(b1, object))
    print(isinstance(b1, (A, B, C)))
    



if __name__ == "__main__":
    main()
    
