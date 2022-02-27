import requests as req
from bs4 import BeautifulSoup
import pandas as pd

cname_lst = []
cprice_lst = []
cinprice_lst = []
oprice_lst = []
clprice_lst = []
upcir_lst = []
locir_lst = []
vwap_lst = []
sector_pe_lst = []
ttm_pe_lst = []
ttm_eps_lst = []
face_value_lst = []
avgdel_20_lst = []
avgvol_20_lst = []
mkt_cap_lst = []
bookvalue_lst = []
vol_lst=[]
list = ["https://www.moneycontrol.com/india/stockpricequote/oil-drillingexploration/oilnaturalgascorporation/ONG"
        "https://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/precisioncamshafts/PC16",
        "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS",
        "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT",
        "https://www.moneycontrol.com/india/stockpricequote/computers-software/hcltechnologies/HCL02",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/idfcfirstbank/IDF01",
        "https://www.moneycontrol.com/india/stockpricequote/tyres/mrf/MRF",
        "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI",
        "https://www.moneycontrol.com/india/stockpricequote/finance-nbfc/indianrailwayfinancecorporation/IRF",
        "https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/kotakmahindrabank/KMB",
        "https://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/precisioncamshafts/PC16",
        "https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB",
        "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI",
        "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/bankbaroda/BOB",
        "https://www.moneycontrol.com/india/stockpricequote/bank-private/idbibank/IDB05",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/idfcfirstbank/IDF01",
        "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/bankindia/BOI",
        "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/ucobank/UCO",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01",
        "https://www.moneycontrol.com/india/stockpricequote/finance-nbfc/indianrailwayfinancecorporation/IRF",
        "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/adanigreenenergylimited/ADANI54145",
        "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/torrentpower/TP14"
]



for lst in list:
    r = req.get(lst)
    data = r.content

    soup = BeautifulSoup(data,'html.parser')
    #print(soup.prettify)
    companyname = soup.find(id='stockName')
    currentprice = soup.find(id="nsespotval").get('value')
    change_inprice = soup.find(id="nsechange").get_text()
    open_price = soup.find('td', class_='nseopn bseopn').get_text()
    close_price = soup.find('td', class_='nseprvclose bseprvclose').get_text()
    uppercircuit_limit = soup.find('td', class_='nseupper_circuit_limit bseupper_circuit_limit').get_text()
    lowercircuit_limit = soup.find('td', class_='nselower_circuit_limit bselower_circuit_limit').get_text()
    Volume = soup.find('td', class_='nsevol bsevol').get_text()
    VWAP = soup.find('td', class_='nsevwap bsevwap').get_text()
    mkt_cap = soup.find('td', class_='nsemktcap bsemktcap').get_text()
    avgvol_20=soup.find('td',class_='nsev20a bsev20a').get_text()
    avgdel_20 = soup.find('td', class_='nsed20ad bsed20ad').get_text()
    face_value = soup.find('td', class_='nsefv bsefv').get_text()
    ttm_eps = soup.find('td', class_='nseceps bseceps').get_text()
    ttm_pe = soup.find('td', class_='nsepe bsepe').get_text()
    sector_pe = soup.find('td', class_='nsesc_ttm bsesc_ttm').get_text()
    book_value = soup.find('td', class_='nsebv bsebv').get_text()


    elem = companyname.find('h1')
    cname_lst.append(elem.get_text())
    cprice_lst.append(currentprice)
    cinprice_lst.append(change_inprice)
    oprice_lst.append(str(open_price))
    clprice_lst.append(str(close_price))
    upcir_lst.append(str(uppercircuit_limit))
    locir_lst.append(str(lowercircuit_limit))
    vol_lst.append(str(Volume))
    vwap_lst.append(str(VWAP))
    mkt_cap_lst.append(str(mkt_cap))
    avgvol_20_lst.append(str(avgvol_20))
    avgdel_20_lst.append(str(avgdel_20))
    face_value_lst.append(str(face_value))
    ttm_eps_lst.append(str(ttm_eps))
    ttm_pe_lst.append(str(ttm_pe))
    sector_pe_lst.append(str(sector_pe))
    bookvalue_lst.append(str(book_value))

dict = {
    'Company Name' : cname_lst,
    'Current Price': cprice_lst,
    'Change in price' : cinprice_lst,
    'Open price': oprice_lst,
    'Close Price': clprice_lst,
    'Upper Circuit': upcir_lst,
    'Lower Circuit': locir_lst,
    'Volume': vol_lst,
    'VWAP': vwap_lst,
    'Market Cap':mkt_cap_lst,
    'Average Vol20':avgvol_20_lst,
    'Average Delivery':avgdel_20_lst,
    'Face Value':face_value_lst,
    'TTM EPS':ttm_eps_lst,
    'TTM PE':ttm_pe_lst,
    'Sector PE':sector_pe_lst,
    'Book Value':bookvalue_lst
}

df = pd.DataFrame(dict)

df.to_csv('moneycontrol.csv',mode="w",index=False)


# with open("4.csv", "w") as file:
#     Writer = writer(file)
#     Writer.writerow(['Company Name', 'Current Price', 'Change in Price', 'Open Price',
#                      'Close Price', 'Upper Circuit', 'Lower Circuit', 'Volume', 'VWAP',
#                      'Market Cap', 'Avg Vol20','Avg Del20', 'Face Value',
#                      'TTM EPS', 'TTM PE', 'Sector PE', 'Book Value'])
#
#     Writer.writerow(cname_lst)
#     Writer.writerow(cprice_lst)
#     Writer.writerow(cinprice_lst)
#     Writer.writerow(oprice_lst)
#     Writer.writerow(clprice_lst)
#     Writer.writerow(upcir_lst)
#     Writer.writerow(locir_lst)
#     Writer.writerow(vol_lst)
#     Writer.writerow(vwap_lst)
#     Writer.writerow(mkt_cap_lst)
#     Writer.writerow(avgvol_20_lst)
#     Writer.writerow(avgdel_20_lst)
#     Writer.writerow(face_value_lst)
#     Writer.writerow(ttm_eps_lst)
#     Writer.writerow(ttm_pe_lst)
#     Writer.writerow(sector_pe_lst)
#     Writer.writerow(bookvalue_lst)

cname_lst.clear()
cprice_lst.clear()
cinprice_lst.clear()
oprice_lst.clear()
clprice_lst.clear()
upcir_lst.clear()
locir_lst.clear()
vwap_lst.clear()
sector_pe_lst.clear()
ttm_pe_lst.clear()
ttm_eps_lst.clear()
face_value_lst.clear()
avgdel_20_lst.clear()
avgvol_20_lst.clear()
mkt_cap_lst.clear()
bookvalue_lst.clear()
vol_lst.clear()



