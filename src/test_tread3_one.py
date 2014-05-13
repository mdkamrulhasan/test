from multiprocessing import Process, Pipe
import random
import time
def f(conn,ns,ne):
    #conn.send([42, None, 'hello'])
    #time.sleep(10)

    sum=0 #ns

    for i in range(ns,ne):
		sum+=1

    #rn=random.randint(nn,nn+5)
    conn.send(sum)#time.time())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    nn=1000000000

    '''
    sum=0

    ts=time.time()
    for i in range(nn):
	sum+=1
    print sum
    te=time.time()
    print te-ts
    '''

    ts=time.time()
    p = Process(target=f, args=(child_conn,0,nn/2))
    p.start()
    s1=parent_conn.recv()   # prints "[42, None, 'hello']"

    #time.sleep(2)
    parent_conn1, child_conn1 = Pipe()
    p1 = Process(target=f, args=(child_conn1,nn/2,nn))
    p1.start()
    s2=parent_conn1.recv()   # prints "[42, None, 'hello']"
    te=time.time()
    #print s1+s2
    #print te-ts


    ts=time.time()
    psL=[]
    pipesL=[]
 
    nPs=2#24
    sum=0
    for ii in range(nPs):
        pc_conn,ch_conn=Pipe()
	#pipesL.append((pc_conn,ch_conn))
	ps=Process(target=f, args=(ch_conn,0,nn/nPs))#random.randint(nn,nn+1)))
	pipesL.append((ps,(pc_conn,ch_conn)))
	pipesL[ii][0].start()
  	#

    #sum=0
    for ii in range(nPs):
	#pipesL[ii][0].start()
  	#pipesL[ii][0].join()
	sum+=pipesL[ii][1][0].recv()

    print sum

    te=time.time()
    print te-ts
