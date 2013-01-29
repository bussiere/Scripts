import markdown
input_file = markdown.codecs.open("test.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text,extensions=['qrcode', 'nl2br'])
f = open('testmd.html', 'w')
f.write(html)
f.close()