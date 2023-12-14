from selenium.webdriver.firefox.webdriver import WebDriver
import time,random
import bs4

wait = 5
usr = ''  #input your email 
passw=''  #input your password

session = WebDriver()
session.get('https://monportail.uniq.edu/index.php')
email = session.find_element_by_name('user')
email.send_keys(usr)
password= session.find_element_by_name('password' )
password.send_keys(passw)
 
submit = session.find_element_by_name('submit')
submit.click()
time.sleep(wait)

email = session.find_element_by_name('user')
email.send_keys(usr)
password= session.find_element_by_name('password' )
password.send_keys(passw)

submit = session.find_element_by_name('submit')
submit.click()

time.sleep(wait)
progression= session.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/p')
progression.click()
time.sleep(wait)

ev = session.get('http://etudiant.uniq.edu/monportail/evaluation-des-professeurs/4bf110213await6e719226d84waitwaitwaita0d908cwait6784f673cbc143072a233wait107aa46b0b812waitac3ef6b8aa1ef8ed3wait20afbe6bbcwait98288619bwaitewait3e7be6a0cce4f3cd74z+TtdGzJzdoQRcP73waitqpqbUx9qoKZwaita1b@!!V62lbMYu8=') 
time.sleep(wait) 
html = bs4.BeautifulSoup(session.page_source,features='html.parser')
links = html.find_all(name='a')
notes=[]
for l in links:
    try:
        if l.get('href').startswith('http://etudiant.uniq.edu/monportail/evaluer-un-cours/'):
            notes.append(l.get('href'))
    except:
        pass


for note in notes:
    session.get(note)
    time.sleep(wait)
    try:
        questions = session.find_elements_by_class_name('radio')
        for q in questions:
            choices  = q.find_elements_by_tag_name('label')
            random.choice(choices).click()

        save = session.find_element_by_name('save')
        save.click()   
       
    except:
        pass

