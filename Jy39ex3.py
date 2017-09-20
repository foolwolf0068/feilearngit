'''
FishC
'''


# Jy40
class C:
    def x(self):
        print("Feige --> X-man!")


def main():
    c = C()
    c.x()
    c.x = 1
    print("c.x = %d" % c.x)
    c.x() # chuangjiande shuxingming = fangfaming  shuxing hui fugai fangfa


if __name__ == "__main__":
    main()
        

