import os,time

def postal_codes():
    csv = open('data/communes.txt')
    codes = set()
    for line in csv:
        _,code,_ = line.split('\t')
        codes.add(code.strip())
    return codes

def used_postal_codes():
    used = set()
    for root, dirnames, filenames in os.walk('raw'):
        for filename in filenames:
            if '.csv' in filename:
                used.add(filename.replace('.csv',''))
    return used

def postal_codes_left():
    return postal_codes() - used_postal_codes()

if __name__ == '__main__':
    while True:
        a  = len(postal_codes())
        b = len(used_postal_codes())
        print a-b,',',a,',',b,',',int(float(b)*1.0/a*10000)/100.,',',time.time()
        time.sleep(60)
