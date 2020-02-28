import mechanize
br = mechanize.Browser()
br = mechanize.Request("http://icanhazip.com")
br.set_proxy("1.165.72.62:9000", "http")
print br.open(req).read()

