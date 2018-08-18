
def countdown(num):
    import time
    while num>=0:
     time.sleep(0.3)
     if num==0:
        print('GO GO GO !!!')
        break
     print(num, 'Seconds to Go!')
     num-=1 #or use num-=1
 
