from vantivsdk import *

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

    