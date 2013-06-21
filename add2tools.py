def Dunefreak():
  url = 'http://www.lomion.de/cmm/dunefrea.php'
  import urllib
  f = urllib.urlopen(url)
  rawdata = str(f.read())
  f.close()
  return rawdata

def getMonster(rawdata):
  # get source from url. http://www.lomion.de/cmm/_index.php
  monster = rawdata[rawdata.find("<title>")+6:rawdata.find("(")-1]

  setting = rawdata[rawdata.find("title=")+6:rawdata.find("\"")]
  #this currently doesn't work.

  # image =  [get /image address, save image, save address of file]

  stats = cleanStats(rawdata[rawdata.find("<table ")+7:rawdata.find("</table>")])
  stats = dict(stats)
  
  info = cleanInfo(rawdata[rawdata.find("<p class=\"f\""):rawdata.find("<br clear=")])
  info = dict(info)

  return (monster,(setting,stats, info))

def cleanStats(rawdata):
  stats = list(rawdata.split("<tr><th>"))
  stats = stats[1:len(stats)-1]
  for t in range(0,len(stats)):
    a,b = stats[t].split("</th><td>")
    a = a.strip(":").lower()
    b = b[:b.find("<")].lower()
    stats[t] = a,b
  return stats

def cleanInfo(rawdata):
    info = rawdata.split("</p>\r\n  <p class=\"f\">")
    for t in range(0,len(info)):
        info[t] = info[t].replace("class=\"f\">","<b>Info:</b> ")
        a = info[t][info[t].find("<b>")+3:info[t].find("</b>")].strip("\\r\\n").strip(":").lower()
        b = info[t][info[t].find("</b>")+5:].strip("\\r\\n").lower()
        info[t] = a,b
    return info

def nextURL(url):  #accepts the url of the current monster, returns url of next
  import urllib
  f = urllib.urlopen(url)
  rawdata = str(f.read())
  url = rawdata[rawdata.find(">Next<")-50:rawdata.find(">Next<")]
  url = url[url.find("a href=")+8:]
  url = url[:url.find("\"")]
  url = "http://www.lomion.de/cmm/"+url
  return url

"""
def toDB(monsters): #put monsters into Anydbm Database
  import anydbm
  db = anydbm.open('monsters.db','c')
  for monster in monsters:
    db[
"""
