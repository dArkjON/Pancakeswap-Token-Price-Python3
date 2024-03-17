import json
from web3 import Web3





###################################################################
#######                       SETTINGS                      #######
###################################################################
BEP20_QUOTETOKEN_ADDRESS = '0xe9e7cea3dedca5984780bafc599bd69add087d56' #<= BUSD 
BEP20_QUOTETOKEN_DECIMALS = 18 #BUSD => 18

BEP20_TOKEN_SYMBOL = "sBTX"
BEP20_TOKEN = '0x000000089fb24237dA101020Ff8e2AfD14624687' #<= sBTX Contract
BEP20_TOKEN_DECIMALS = 8

TRADINGTIGERSROUTER = '0xdEdf20172b6dC39817026c125f52d4fad8E0f29b' #This contract do all the work for you, find the best Pool and convert too your QuoteToken. <= (PancakeSwap)

FINAL_PRICE_ROUND_TO_DECIMALS = 3
###################################################################

ABI = [{
        "inputs": [
            {
                "internalType": "address",
                "name": "TokenA",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "TokenB",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "getOutputfromTokentoToken",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }]


def get_TokenPrice():
    w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    swapper = w3.eth.contract(address=Web3.toChecksumAddress(TRADINGTIGERSROUTER), abi=ABI)
    OneQuoteToken = 1 * (10**BEP20_TOKEN_DECIMALS)
    
    TOKEN_Price = swapper.functions.getOutputfromTokentoToken(
        Web3.toChecksumAddress(BEP20_TOKEN), #<= Input Token from whom we want to know the price!
        Web3.toChecksumAddress(BEP20_QUOTETOKEN_ADDRESS), #<= Output Token we use BUSD, so we know USD price!
        OneQuoteToken
        ).call()[0]
        
    TokenTokenPrice = round(TOKEN_Price / (10**BEP20_QUOTETOKEN_DECIMALS), FINAL_PRICE_ROUND_TO_DECIMALS)
    return TokenTokenPrice
	
print (get_TokenPrice())
