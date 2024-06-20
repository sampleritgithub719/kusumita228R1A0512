#throw(assert)
def avg(marks):
    assert len(marks)!=0,"The list is empty"
    return sum(marks)/len(marks)
marks1=[23,45,67,78,90]
#marks=[]
print("The avg of marks1:",avg(marks1))
marks2=[10,20,30,40,50]
print("The avg  of marks2:",avg(marks2))