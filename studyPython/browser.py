import webbrowser

url = "https://www.google.com/search?&q="

keyList = ["Java","C++","파이썬"]

#해당 url로 webbrowser를 열어줘

for word in keyList:
    webbrowser.open(url+word)

#open_new
# : 새로운 프로그램으로 열어줘
#open_new_tab
# : 새 tab에서 열어줘

