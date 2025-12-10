password = input("Enter password")
isAlphaPresent=False
isDigitPresent=False


for character in password:
    if( (character >='A' and character <='Z') or (character >='a' and character <='z')):
       print('its character ',character)
       isAlphaPresent = True
        
    if(character >='0' and character <='9'):
        print('its digit',character)
        isDigitPresent = True
        
        
        
if(isAlphaPresent and isDigitPresent and len(password) >=10):
    print('password is strong')
  
else :
     print('password is weak')
 