 # syntax
class ContactInfo:
    # 생성자
    count = 0
    def __init__(self,name='홍길동', email='name@domain.net'):
        self.name = name
        self.email = email
        ContactInfo.count += 1
    
    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

    @staticmethod
    def class_info():
        print(type(ContactInfo()))

    @classmethod
    def instance_count(self):
        print(self.count)

    

if __name__ == '__main__':
    seongmin = ContactInfo('유성민','dbtjdals1771@ajou.ac.kr')
    seongmin.print_info()
    seongmin.instance_count()

    defaultInfo = ContactInfo()    
    defaultInfo.print_info()
    defaultInfo.instance_count()
    
    
