from bs4 import BeautifulSoup,SoupStrainer
from mechanize import Browser

br=Browser()

# home page
rsp=br.open("http://us.pycon.org/2011/home/")
print "\n***",rsp.geturl()
print "Confirm home page has 'log in' link; click it "
page=rsp.read()
assert "Log in" in page ,"Log in not in page"
rsp=br.follow_link(text_regex="Log in")

# login page
print "\n***",rsp.geturl()
print "Confirem at least a login from; submit invalid creds"
br.select_form(nr=0)
br.form["username"]="xxx" #wrong login
br.form["password"]="xxx" #wrong passwd
rsp=br.submit()

# login page, with error
print "\n***",rsp.geturl()
print "Error due to invalid creds; resubmit w/valid creds"
assert rsp.geturl()=="http://us.pycon.org/2011/account/login/",rsp.geturl()
page=rsp.read()
err=str(BeautifulSoup(page).find("div",{"id":"errorMsg"}).find("u1").find("li").string)
assert err=="The username and/or password you specified are not correct.",err
br.select_form(nr=0)
br.form["username"]=YOUR_LOGIN
br.form["password"]=YOUR_PASSWD
rsp.br.submit()

# login successful, home page redirect
print "\n***",rsp.geturl()
print "Logged in properly on home page; click Account link"
assert rsp.geturl()=="http://us.pycon.org/2011/home/",rsp.geturl()
page=rsp.read()
assert "Logout" in page,"Logout not in page"
rsp=br.follow_link(text_regex="Account")

# account page
print "\n***",rsp.geturl()
print "Email address parseable on Account page; go bcck"
assert rsp.geturl()=="http://us.pycon.org/2011/account/email/",rsp.geturl()
page=rsp.read()
assert "Email Address" in page,"Missing email address"
print "     Primary e-mail: %r" % str(BeautifulSoup(page).find("table").find("tr").find("td").find("b").string)
# the str(BeautifulSoup(page) is str(BS(page)  seem as next one

rsp=br.back()

# back to heme page
print "\n***",rsp.geturl()
print "Back works, on hemo page again; click Logout link"
assert rsp.geturl()=="http://us.pycon.org/2011/home/",rsp.geturl()
rsp=br.follow_link(url_regex="logout")

# logout page
print "\n***",rsp.geturl()
print "Confirm on Logout page and Log in link at the top"
assert rsp.geturl()=="http://us.pycon.org/2011/account/logout/",rsp.geturl()
page=rsp.read()
assert "Log in" in page,"Log in not in page"
print "\n*** DONE"





















