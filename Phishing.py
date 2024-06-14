#phishing url detector
#list of known phishing urls

phishing_urls=["revil.ru","conti.ru","nso.il","doubledragon.cn","ryuk.ru","spam.com"]
#prompt the user to enter the url
url=input("Enter a url:")
#extract the domain from the url
domain=url.split("//")[-1].split("/")[0]
#check the conditions
if domain in phishing_urls:
    print("Beware!! this url is a known phishing url.")
else:
    print("this url does not appear to be a phishing url.")