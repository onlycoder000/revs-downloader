import webbrowser
import csv
import time

# with open('data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         webbrowser.open('row', new=2)
#         time.sleep(8)
#         line_count+=1
#         print(line_count)


for line in range(31,460):
    webbrowser.open('https://docs.google.com/spreadsheets/export?id=1HN817JDjCVOitnXBOIDzaeomuy21K_ZXtLgqfH5PwF4&revision='+str(line)+'&exportFormat=xlsx')
    print(line)
    time.sleep(10)
   