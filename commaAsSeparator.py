def comma(lis):
    for i in range(0,len(lis)-1):
        if lis[i]==lis[-2]:
            print(lis[i]+' and '+lis[i+1])
            break
        print(lis[i]+', ',end='')

spam=['apples','bananas','tofu','cats']
comma(spam)
