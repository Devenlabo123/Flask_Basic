from vantivsdk import *

def Articles():
    articles = [
        {
            'id': 1,
            'title': 'Article One',
            'body':'A bunch of text goes here',
            'author': 'Joe Smith',
            'create_date':'04-25-2017'
            },
        {
            'id': 2,
            'title': 'Article Two',
            'body':'A bunch of text goes here',
            'author': 'John Smith',
            'create_date':'04-25-2017'
            },
        {
            'id': 3,
            'title': 'Article THREE',
            'body':'A bunch of text goes here',
            'author': 'jOSH Smith',
            'create_date':'04-25-2017'}
    
        ]
    
    return articles

def salesResponse():
    conf = utils.Configuration()

    transaction = fields.sale()
    transaction.reportGroup = "Default Report Group"
    transaction.orderId = '12344'
    transaction.amount = 106
    transaction.orderSource = 'ecommerce'
    transaction.id = 'ThisIsID'
    
    card = fields.cardType()
    card.number = '4100000000000000'
    card.expDate = '1210'
    card.type = 'VI'
    
    transaction.card = card
    
    response = online.request(transaction, conf)
    print(response)
    return response

    