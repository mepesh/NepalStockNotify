import sys,threading,time
import winBallon as wb
import stockServicesClass as ssc
from stockServicesClass import NepalStockServices


if(ssc.getMarketStatus()=="\nMarket Open\n"):
    wb.balloon_tip("Market Closed","Come Back when market is Opened ",5)
    sys.exit()
elif(ssc.getMarketStatus()=="\nMarket Close\n"):
    url_code="0"
    while(url_code=="0"):
        code = raw_input("Plese enter the Code eg:[scb,adbl,nlic]\n")
        url_code = ssc.getUrlCode(code)
    recentPrice = ssc.getRecentPrice(url_code)
    print "The Recent Price Of "+code.upper()+" is "+recentPrice
    yn = "a"
    while(yn.upper()!="Y" and yn.upper()!="N"):
        yn=raw_input("Do you want to create ALERT of Stocks \n [Y]es or [N]o only \n")
        yn=yn.upper()
        if(yn=="Y"):
            bs = "z"
            while(bs.upper()!="B" and bs.upper()!="S"):
                bs = raw_input("Are you looking to [B]uy or [S]ell\n")
                if(bs.upper()=="B"):
                    threshold = raw_input("Notify me when the seller is available below :")
                    wb.balloon_tip("Alert "+ code.upper(),"Alert's when Seller is available Below "+threshold,5)
                    ssc.getMarketDepthSell(code.upper(),url_code,threshold);


                elif(bs.upper()=="S"):
                    threshold = raw_input("Notify me when the buyer is available above :")
                    wb.balloon_tip("Alert "+code.upper(),"Alert's when Buyer is available Above "+threshold,5)
                    ssc.getMarketDepthBuy(code.upper(),url_code,threshold);
                    


        elif(yn=="N"):
            wb.balloon_tip("Thank You","Come Back Soon",7)
            print "Thank you for using \n"
            print "comeback if you need notification of Nepal Stock \n"
            sys.exit()





