import subprocess

wifis = subprocess.getoutput('netsh wlan show profile').rsplit('\n')
wifis = [ ' '.join( f.rsplit(':')[1].rsplit()[0:]) for f in wifis if  'All User Profile' in f ]

for w in wifis:
    s = subprocess.getoutput('netsh wlan show profile {} key=clear'.format(w)).rsplit('\n')
    ss= []
    
    for i in s:
        try:
            if len(i.rsplit(':')) ==2:
                ss.append(i.rsplit(':'))
        except:
            pass

    for a in ss:
        if 'Key Content' in a[0]:
            print("{} : {}".format(w.rjust(20),a[1]))
            break

