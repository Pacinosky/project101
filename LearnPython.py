#counting from a list 
fruits=['apple','banana', 'apple','orange','pear','orange','waterlemon','apple']
basket={}
for fruit in fruits:
    if fruit in basket:
        basket[fruit]+=1
    else:
        basket[fruit]=1

single_fruit=[]
for fruit in basket:
    if basket[fruit]>1:
        single_fruit.append(fruit)
print(basket)
print(f'single_fruit:{single_fruit}')

