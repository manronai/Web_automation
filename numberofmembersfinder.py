import re as r
class checklinks():
    strin = 'hello'
    def __init__(self):
        print(self.strin)

    def Link(self, link):
        self.strin = link
        self.serch = r'profile\.php\?id\='
        self.rr = r.search(self.serch, self.strin)
        if self.rr:
            print(self.rr)
            print(self.rr.span())
            return str(self.strin + '&sk=about_contact_and_basic_info')
        else:
            return str(self.strin + '/about_contact_and_basic_info')
