'''
On deciphering faststyletransfer, I came across a phrase "for a, b, c in optimize(....)"
Never seen this before, so I googled and found concepts of iterables, generatiors, and yield keyword
source: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do?page=1&tab=votes#tab-top
each 'for' is forgotten after execution. 
Handy when the function returns a huge set of values that will only be read once.
'''

def add_generator(*lists): #only one *args per input
    #for x,y in lists[0], lists[1]:  for 문에 이렇게 iterable 두개를 나열할 수 없다. 
    for x,y in zip(lists[0], lists[1]):  #work around it with zip
        yield x + y

mygenerator = add_generator([1,2,3],[4,5,6])

for i in mygenerator:
    print(i)

'''
When you call the function(line 14), the code you have written in the function body does not run.
The function only returns the generator object.
Code will continue from where it left off each time 'for' uses the generator.
함수는 for에서 연산이 이루어진다. 
'''

'''
텐서플로우에 대한 정확한 이해는 9월 프로젝트가 끝나고 시작하자. 
'''