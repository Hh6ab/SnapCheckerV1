import requests
import json
print('''
███████╗███╗   ██╗ █████╗ ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗     ██╗   ██╗ ██╗
██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║███║
███████╗██╔██╗ ██║███████║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝    ██║   ██║╚██║
╚════██║██║╚██╗██║██╔══██║██╔═══╝     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝ ██║
███████║██║ ╚████║██║  ██║██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║     ╚████╔╝  ██║
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝   ╚═╝
   Free Version By : Xcode                                                                                                                                                                 
''')
print('''
                    ▒▒▒▒▒▒▒▒▒▒                    
                ▒▒▒▒░░      ░░▒▒▒▒                
              ▒▒░░              ░░▒▒              
            ▒▒░░                  ░░▒▒            
            ▒▒                      ▒▒            
  ▒▒      ▒▒░░              ████    ░░▒▒      ▒▒  
▒▒░░▒▒    ▒▒░░            ████████  ░░▒▒    ▒▒░░▒▒
▒▒░░░░▒▒  ▒▒░░  ██▓▓    ██▓▓▓▓▓▓████░░▒▒  ▒▒░░░░▒▒
▒▒░░  ░░▒▒▒▒░░  ▓▓▓▓    ██▓▓▒▒▒▒▓▓██░░▒▒░░░░  ░░▒▒
  ▒▒    ░░▒▒░░            ██▓▓▓▓▓▓  ░░▒▒░░    ▒▒  
  ▒▒░░    ▒▒░░                      ░░▒▒      ▒▒  
    ░░    ▒▒░░  ██              ██  ░░▒▒    ▒▒    
    ▒▒░░░░▒▒░░    ██▓▓▒▒▓▓▒▒▓▓██    ░░▒▒░░░░▒▒    
      ▒▒░░▒▒░░      ▒▒▒▒▒▒▒▒▒▒      ░░▒▒░░░░      
        ▒▒░░        ▒▒░░░░░░▒▒        ░░▒▒        
        ▒▒░░░░  ░░░░▒▒░░░░░░▒▒░░░░  ░░░░▒▒        
        ▒▒░░░░░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░▒▒        
        ▒▒░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒        
      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒      
      ▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒      
    ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒    
  ▓▓▒▒▒▒▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒▓▓  
    ▒▒▒▒▒▒            ▒▒▒▒▒▒            ▒▒▒▒▒▒    
------------------------------------------------------------------------
#Coded By : Xcode & Twitter: @XcodeOn1

''')
UserInput = input(" What User You want To check :  ")
url = "https://app.snapchat.com:443/loq/suggest_username_v2"
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
           "Accept": "application/json", "Accept-Locale": "en_SA", "Connection": "close",
           "X-Snapchat-UUID": "", "x-snapchat-att": "CgsYACAAFaiThEQIChK4AXyUc_6dfBtKSeUR7bYZn0xI3IaxCqocThfdZ4fCFeoM8mrMEximQTGWrkzcyg1sjaRpG4u1K0n7-Next7xsXOUxyVojGVG1gu6BZ8_cFt0q-JMVpYEUrN6IIab-cKS9_5WiHel0tW6U04TmiXOac9dHtkIgbvF0w9J6vq3XxA8_IEF6ibfu2qkBZxvaRuCrEzZh-4GFEo_0BM6m2dJmTZTxTw5xxKwlGBIXq_yqQ7Ba-v8lfOEEzdw=",
           "User-Agent": "Snapchat/10.87.0.69 (Twitter XcodeOn1; iOS 13.5.1; gzip)",
           "Accept-Language": "en-SA;q=1, ar-SA;q=0.9, en-US;q=0.8, bn-SA;q=0.7, pa-SA;q=0.6",
           "Accept-Encoding": "gzip, deflate"}
web_data = {"req_token": "9307955c05e1ab886e3a9eeff7a501f40deb4d8219ac0a87f9b4f214dfc518eb", "requested_username": UserInput, "timestamp": "1595566579397"}
response= requests.post(url, headers=headers, data=web_data)

print("Status code: ", response.status_code)
print(response.json())
