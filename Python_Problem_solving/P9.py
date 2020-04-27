##Multiprocessing
import multiprocessing

def spawn(num,num2):
    print('Spawned! {} {}'.format(num,num2))

if __name__ == '__main__':
    for i in range(500):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        #p.join()