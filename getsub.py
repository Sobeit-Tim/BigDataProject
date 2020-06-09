
from pytube import YouTube

def get():
    url = input("url : ")

    yt = YouTube(url)
    caption = yt.captions.get_by_language_code('en')

    caption.download("Captions")

    file = open("Captions (en).srt", "r", encoding='UTF8')
    result = file.read()
    file.close()

    result = result.split('\n\n')

    time = []
    text = []

    for i in result:
        temp = i.split('\n')
        tempText = ""
        for j in range(len(temp)):
            if j == 1:
                time.append(temp[j].split(" --> "))
            elif j > 1:
                tempText += temp[j]

        text.append(tempText)


    length = 0
    sec = 0
    for i in range(len(time)):
        start = time[i][0].replace(',', ':').split(':')
        end = time[i][1].replace(',', ':').split(':')
        temp_length = len(text[i].split(' '))
        temp_time = (int(end[0]) - int(start[0])) * 3600 + (int(end[1]) - int(start[1])) * 60 + int(end[2]) - int(start[2])
        length += temp_length
        sec += temp_time
    step = length / sec

    # wholeText = sum(text, [])
    wholeText = '\n'.join(text)
    return step, wholeText