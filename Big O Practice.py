#define a O(1)constant 
def func_constant(letters):
    print (letters[0])
lst = [1,2,3,4,5,6]  
func_constant(lst)

#define a O(n) Linear==List the items in a list
june = [1,2,3,4,5,6,7]
def func_lin(lst):
    for d in lst: #print every item in the list
        print (d)
func_lin(june)

jane=[1,2,3]
def func_quad(jane):
    for b in jane:
        for c in jane:
            print (b,c) 
func_quad(jane) 