

def parse_meebit_data(meebit_dict):
    
    meebit_id = meebit_dict['token_id']
    
    try:#fetching data reom opensea data structure
        creator_username = meebit_dict['creator']['user']['username']
    except:
        creator_username = None
    try:
        creator_address = meebit_dict['creator']['address']
    except:
        creator_address = None
    
    try:
        owner_username = meebit_dict['owner']['user']['username']
    except:
        owner_username = None
    
    owner_address = meebit_dict['owner']['address']
    
    traits = meebit_dict['traits']
    num_sales = int(meebit_dict['num_sales'])
    #creating dic to store the data in a easier way    
    result = {'meebit_id': meebit_id,
              'creator_username': creator_username,
              'creator_address': creator_address,
              'owner_username': owner_username,
              'owner_address': owner_address,
              'traits': traits,
              'num_sales': num_sales}
    
    return result


def parse_sale_data(sale_dict):
    
    is_bundle = False

    if sale_dict['asset'] != None:
        meebit_id = sale_dict['asset']['token_id']
    elif sale_dict['asset_bundle'] != None:
        meebit_id = [asset['token_id'] for asset in sale_dict['asset_bundle']['assets']]
        is_bundle = True
    
    #information about sale and seller as well as buyer is fetched
    seller_address = sale_dict['seller']['address']
    buyer_address = sale_dict['winner_account']['address']
    
    try:
        seller_username = sale_dict['seller']['user']['username']
    except:
        seller_username = None    
    try:
        buyer_username = sale_dict['winner_account']['user']['username']
    except:
        buyer_username = None
    
    timestamp = sale_dict['transaction']['timestamp']
    total_price = float(sale_dict['total_price'])
    payment_token = sale_dict['payment_token']['symbol']
    usd_price = float(sale_dict['payment_token']['usd_price'])
    transaction_hash = sale_dict['transaction']['transaction_hash']
    

    result = {'is_bundle': is_bundle,
              'meebit_id': meebit_id,
              'seller_address': seller_address,
              'buyer_address': buyer_address,
              'buyer_username': buyer_username,
              'seller_username':seller_username,
              'timestamp': timestamp,
              'total_price': total_price, 
              'payment_token': payment_token,
              'usd_price': usd_price,
              'transaction_hash': transaction_hash}
    
    return result

