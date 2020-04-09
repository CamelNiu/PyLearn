import time,os,random,requests
from multiprocessing import Pool


class

def testApi(url,num):
  print('child process['+str(os.getpid())+']' )
  start = time.time()

  for i in range(num):
    memberId = 100000
    memberId = memberId + i
    param = {'member_id':memberId}
    r = requests.get(url,params = param)
    print(r.text)
  end   = time.time()

  print(end-start)

testApi('http://api.digifinex.com/invite/invite_reward_info',200)

# if __name__ == "__main__":
#   print('Parent process[' + str(os.getpid())+']')
#   p = Pool(10)

#   for i in range(10):
#     p.apply_async(testApi,args=('http://api.digifinex.com/invite/invite_reward_info',5,))




