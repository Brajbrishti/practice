from collections import OrderedDict

class A:
    try:
        def Dictionary_sqr(self):
            dict =  {'A':20,'D':30,'C':50,'B':80}

            my_dict=OrderedDict(sorted(dict.items()))

            print(my_dict)
            for i in dict.values():
                print(i * i)

        Dictionary_sqr()
    except:
        print("Code is done")

