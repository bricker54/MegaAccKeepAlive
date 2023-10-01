import requests
from mega import Mega
input("Warning! This will take an stupidly long time to finish. Press Enter to continue...")
GigabyteTotalVal = 0.00
try:
    response = requests.get('https://meganzindex.000webhostapp.com/MegaAccess/MegaAccessData.data', auth=('TheVaultUsr', 'R0Y04>2~3[Pu!ch;;@yGjY%HVa>-vO[+0Ryq|#<bLi+VH*lhKl'))
    response.raise_for_status()  # Raise an exception if the request was not successful

    # Split the content of the webpage into lines
    lines = response.text.split('\n') 

    # Iterate through the lines and print each one
    for i in range(len(i)):
        mega = Mega()
        CurrentRequest = lines[i].strip()
        m = mega.login(CurrentRequest, "MultiupSucksAss54@#")
        quota = m.get_quota()
        MBVal = float(quota)
        MBVal = MBVal / 1000
        GigabyteTotalVal = GigabyteTotalVal + MBVal
    
    print("Total Space: "+str(GigabyteTotalVal)+" GB")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
