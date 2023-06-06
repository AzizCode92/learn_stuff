class User:
    def __init__(self, user_data):
        self.id = user_data.get("id")
        self.name = user_data.get('name')
        self.username = user_data.get('username')
        self.email = user_data.get('email')
        self.address = Address(user_data.get('address'))
        self.phone = user_data.get('phone')
        self.website = user_data.get('website')
        self.company = Company(user_data.get('company'))

class Address:
    def __init__(self, address_data):
        self.street = address_data.get('street')
        self.suite = address_data.get('suite')
        self.city = address_data.get('city')
        self.zipcode = address_data.get('zipcode')
        self.geo = Geo(address_data.get('geo'))


class Geo:
    def __init__(self, geo_data):
        self.lat = geo_data.get('lat')
        self.lng = geo_data.get('lng')


class Company:
    def __init__(self, company_data):
        self.name = company_data.get('name')
        self.catchPhrase = company_data.get('catchPhrase')
        self.bs = company_data.get('bs')
