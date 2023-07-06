html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My first web page</title>
</head>
<body>

<h1 id="header">
        Python Kursu
       </h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="jpg.jpg" alt="">

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.body.name
result = soup.title.string
result = soup.h1
result = soup.h2.name
result = soup.h2.string
result = soup.findAll("h2")
result = soup.findAll("h2")[0]
result = soup.div
result = soup.findAll("div")[1]
result = soup.findAll("div")[1].ul.li
result = soup.findAll("div")[1].ul.findAll("li")
result = soup.div.findChildren()   #parent sibling children
result= soup.div
result = soup.div.findNextSibling().findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

print(result)