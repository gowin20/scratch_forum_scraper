from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


#this program is gonna take like an hour to run, so just don't run it. I compiled the csv files on my computer, and it took like 20 minutes / file. If you wanna see the raw data, click on the ".csv" files to the left

#will add more as my program finishes running


#takes in a top-level forum and returns information about all the results
def results(forum,numpages):

    database = {"topic":[],"link":[],"replies":[],"views":[]}

    for i in range(1,numpages):

        page = urlopen(forum+"?page="+str(i))
        soup = BeautifulSoup(page,features="html.parser")

        #print(soup)

        nametable = soup.findAll("td",attrs={"class":"tcl"})
        replytable = soup.findAll("td",attrs={"class":"tc2"})
        viewtable = soup.findAll("td",attrs={"class":"tc3"})

        for i in range(len(nametable)):
            #make sure they all exist
            if nametable[i] and replytable[i] and viewtable[i]:
                info = nametable[i].find("a")
                title = info.getText().strip()
                link = info["href"]
                replies = int(replytable[i].getText().strip())
                views = int(viewtable[i].getText().strip())

                database["topic"].append(title)
                database["link"].append(link)
                database["replies"].append(replies)
                database["views"].append(views)
            else:
                print("ERROR")
        #        return -1


    data = pd.DataFrame(data=database)
    data = data.sort_values("views",ascending=False)

    return data



#DIFFERENT DATABASES
#by default this program will create files and generally takes forever to run. Don't run this at all please lol

scripthelp = results("https://scratch.mit.edu/discuss/7/",2200)

scripthelp.to_csv("scripts.csv")

questions = results("https://scratch.mit.edu/discuss/4/",1430)
questions.to_csv("questions.csv")

ideas = scripthelp = results("https://scratch.mit.edu/discuss/9/",360)
ideas.to_csv("ideass.csv")


#format stuff
#for post in table:


#body = table.find("tbody")
#print(table)

#links = table.findAll("tr")

#print(links)


#tcl - the title of the post + link

#tc2 - the number of REPLIES
#tc3 - the number of VIEWS