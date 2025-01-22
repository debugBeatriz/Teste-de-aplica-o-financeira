import pyautogui
import subprocess
import time



url_site = "https://partagerpage.netlify.app/"

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

time.sleep(1)
pyautogui.write(url_site)

time.sleep(1)
pyautogui.press('enter')



time.sleep(1)
pyautogui.press('tab')#para apertar e preencher a primeira input do formuláriopyautogui.press'tab' #para apertar e preencher a primeira input do formulário
pyautogui.press('tab')

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.press('tab')#para apertar e preencher a primeira input do formuláriopyautogui.press'tab' #para apertar e preencher a primeira input do formulário
pyautogui.press('tab')
pyautogui.press('enter')

for _ in range(8):
        pyautogui.press('tab')
        time.sleep(1)
       
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('tab')

time.sleep(1)
pyautogui.write("Beatriz") #posso colocar aspas duplas para preencher com os valores
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("beatrizgomesdesouza70@gmail.com")
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("23")
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("Sdpo987.,!")
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("Sdpo987.,!")
pyautogui.press('tab')


pyautogui.PAUSE  = 0.4   
print(pyautogui.position())
print(pyautogui.size())


time.sleep(0.5)
pyautogui.press('space')
pyautogui.moveTo(x=1273, y=54)
pyautogui.click(x=512, y=576)
pyautogui.press('enter')
pyautogui.press('tab') 

time.sleep(5.0)
pyautogui.press('space')
pyautogui.press('tab')

time.sleep(5.0)
pyautogui.press('tab')
pyautogui.press('space')

time.sleep(5.0)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')











