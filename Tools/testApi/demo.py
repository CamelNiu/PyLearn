import time,os,random,requests
from multiprocessing import Pool


def testApi(url,num):

  start = time.time()
  for i in range(num):
    memberId = 100000
    memberId = memberId + i
    param = {'reward_type':1}
    r = requests.get(url,params = param)
    print(r.status_code)
  end   = time.time()

  print(end-start)

testApi('http://api.digifinex.com/invite/invite_reward_record',200)

if __name__ == "__main__":
  print('Parent process[' + str(os.getpid())+']')
  p = Pool(10)

  for i in range(10):
    p.apply_async(testApi,args=('http://api.digifinex.com/invite/invite_reward_info',5,))



