#!/usr/bin/python3
import glob
import sys
import datetime

def get_file_number(file_path):
    # Funkcja pomocnicza do uzyskania numeru z nazwy pliku
    return int(''.join(filter(str.isdigit, file_path)))

files = glob.glob("./out/out*.txt")
files = sorted(files, key=get_file_number)
tab=[]

now = datetime.datetime.now()
data = now.strftime("%H:%M:%S %d/%m/%Y")

with open("raport.html", "w") as report_file:
# Rozpocznij pisanie kodu HTML
    report_file.write("<html>\n")
    report_file.write("<head><title>Dominika Wiśniewska - projekt</title></head>\n")
    report_file.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"> \n')
    report_file.write("</head> \n")
    report_file.write("<body>\n")
    report_file.write('<div class="container">\n')
    report_file.write(f"<h1>Raport {data} :</h1>\n")
    report_file.write("<table><thead><tr><th>Dane wejściowe</th><th>Dane wyjściowe</th></tr></thead><tbody>\n")

    for file_path in files:
        tab.append(get_file_number(file_path))
    files2 = []
    for i in range(len(tab)):
        files2.append(f"./in/in{tab[i]}.txt")

    paths=[]
    for i in range(len(files)):
        paths.append(files2[i])
        paths.append(files[i])

    for path in paths:
        with open(path, "r") as current_file:
            content = current_file.read()
            if paths.index(path) %2 ==0:
                report_file.write("<tr>\n")
            report_file.write(f"<td><pre>{content}</pre>\n </td>")
            if paths.index(path) %2 ==1:
                report_file.write("</tr>\n")


    # Zakończ pisanie kodu HTML
    report_file.write(" </tbody>\n</table>\n</div>\n")
    report_file.write("</body>\n")
    report_file.write("</html>\n")

print("Raport został utworzony w pliku raport.html.")

