# -*- coding: utf-8 -*-
import mechanize, cookielib, re, parse, sys, postalcodes, random, os
from utils import *

while True:
    POSTALCODE = random.choice(list(postalcodes.postal_codes_left()))

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    warn(POSTALCODE)
    info("HOMEPAGE")
    br.open('https://www.transparence.sante.gouv.fr')

    warn(POSTALCODE)
    info("BIG FORM")
    r = br.follow_link(text="Recherche avancée")
    br.select_form(nr=0)
    br.form['form:codePostalBeneficiaire'] = POSTALCODE
    r = br.submit()

    warn(POSTALCODE)
    info("CAPTCHA")
    print br.geturl()
    html = r.read()
    match = re.search('Quelle est la (.*?)è[r|m]e lettre du mot « (.*?) » ?', html, re.S)
    n, word = match.group(1), match.group(2)
    print "asked:",n, word
    word = word.decode('utf-8')
    answer = word[int(n)-1]
    print "answer:",answer
    br.select_form(nr=0)
    br.form['j_idt187:captcha'] = answer.encode('utf-8')
    r = br.submit()

    warn(POSTALCODE)
    info("RESULTS")
    page = 0
    all_data = []
    while True:
        warn(POSTALCODE)
        info("page %s" % page)
        html = r.read()
        data = list(parse.results(html))
        info(str(len(data)))
        #table(data)
        all_data += data
        save_csv(all_data,"raw/tmp/%s.csv" % POSTALCODE)
        br.select_form(nr=0)
        try:
            if br.form.find_control('j_idt17:j_idt93').disabled:
                break
            r = br.submit(name='j_idt17:j_idt93')
        except mechanize._form.ControlNotFoundError: #only one page of data
            break
        page += 1

    os.remove("raw/tmp/%s.csv" % POSTALCODE)
    save_csv(all_data,"raw/%s.csv" % POSTALCODE)