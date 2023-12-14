
import time,re

from selenium.webdriver.chrome.webdriver import WebDriver

phonenumber = ''
passw = ''
def acceptall_and_bet():
    try:
        acceptall= session.find_element_by_xpath('/html/body/hg-root/hg-layout/div/hg-layout/hg-sport-sidebar/hg-popup/div[2]/hg-bet-slip/div/div[3]/div[2]/hg-toggle/label/div/div')
        acceptall.click()
        
    except:
        pass

session=WebDriver()
session.get("https://www.paryajlakay.com/sports")

time.sleep(10)
num =session.find_element_by_xpath("/html/body/hg-root/hg-layout/hg-header/div[1]/div/div[2]/hg-login/hg-popup/div[2]/div/div/div[2]/div/form/hg-login-input/input")
num.send_keys(phonenumber) #enter your phone number

passw=session.find_element_by_xpath("/html/body/hg-root/hg-layout/hg-header/div[1]/div/div[2]/hg-login/hg-popup/div[2]/div/div/div[2]/div/form/span/input")
passw.send_keys(passw)    #enter your password


login = session.find_element_by_xpath("/html/body/hg-root/hg-layout/hg-header/div[1]/div/div[2]/hg-login/hg-popup/div[2]/div/div/div[2]/div/form/button[1]")
login.click()
time.sleep(7)
categories = ["https://www.paryajlakay.com/sports/101","https://www.paryajlakay.com/sports/102" ,"https://www.paryajlakay.com/sports/103"
,"https://www.paryajlakay.com/sports/104","https://www.paryajlakay.com/sports/105"]
for c in categories:

    session.get(c)
    time.sleep(2)


     #chose the mathes that'll play 7 hours later
    _7hours= session.find_element_by_xpath("/html/body/hg-root/hg-layout/div/hg-layout/hg-events-by-event-category/div[1]/div[1]/hg-time-filter/button[2]")
    _7hours.click()
    time.sleep(3)

    for i in range(3):
        try:
            #get more results
            moreresults=session.find_element_by_xpath('/html/body/hg-root/hg-layout/div/hg-layout/hg-events-by-event-category/div[2]/footer/span')
            moreresults.click()
            time.sleep(3)
        except:
            pass

    time.sleep(5)

    base = str('odds')
    base2= session.find_elements_by_class_name(base)
    solution1,odds = list(),list()
    cote = 5    #if you want a specific odd to bet
    done = 0    #the number of matches selected

    #for each matchs choose the highest odd between draw ,win for team 1 and win for team 2
    for n in range(0,len(base2 )-3,3):
        v1, nul, v2 = re.sub(',','.',base2[n].text), re.sub(',','.',base2[n+1].text), re.sub(',','.',base2[n+2].text)
        try:
            temp = list( [ float(v1),float(nul),float(v2) ]   )
            #odds.append(temp)
            if float(v1) > cote:
                if  float(nul) >cote:
                    solution1.append(float(v1))
                    vv1= base2[n]
                    vv1.click()
                    nnl= base2[n+1]
                    nnl.click()
                    solution1.append(float(nul))
                    done+=1
                    acceptall_and_bet()
                else:
                    solution1.append(float(v1))
                    vv1= base2[n]
                    vv1.click()
                    done+=1
                    acceptall_and_bet()
            
            elif float(v2) >cote:
                if  float(nul) >cote:
                    solution1.append(float(v2))
                    vv2= base2[n+2]
                    vv2.click()
                    nnl= base2[n+1]
                    nnl.click()
                    solution1.append(float(nul))
                    done+=1
                    acceptall_and_bet()
                else:
                    solution1.append(float(v1))
                    vv2= base2[n+2]
                    vv2.click()
                    done+=1
                    acceptall_and_bet()

            elif float(nul) >cote:
                nnl= base2[n+1]
                nnl.click()
                solution1.append(float(nul))
                done+=1
                acceptall_and_bet()
                #odds.append(base2[n+1])

            if done == 5:
                break
                #abort the program if you bet in the number of matches you wanted
        except:
            pass
    time.sleep(5)





    

















