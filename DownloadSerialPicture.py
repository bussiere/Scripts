
"""
By bussiere bussiere @at gmail.com
downloading a serial list of picture from the web
what 
give this program an url from a pciture and it will try to download all the list of existing picture exemple : downloader.py http://www.example.com/picture01.jpg
why : 
some times i've got a link like http://www.example.com/picture01.jpg and i guess that there are more picture of it this program will try to find them all and download them all

"""

__Author__ ="bussiere"
__Email__ = "bussiere @at gmail.com"
__Titre__ = "downloading a serial list of picture from the web"
__Description__ = "give this program an url from a pciture and it will try to download all the list of existing picture exemple : downloader.py http://www.example.com/picture01.jpg"
__Discussion__ = "some times i've got a link like http://www.example.com/picture01.jpg and i guess that there are more picture of it this program will try to find them all and download them all"
__Tags__ ="download picture pictures jpg JPG url list series serie"
import re
import time,datetime
import urllib2

def download_pictures(url,start=1,limit=999,trial=3):
    #we compile the regular exepression that will get the number and the point of the url as 01. in the http://www.example.com/picture01.jpg
    reg = re.compile("[0-9]+\.")
    # here we compile a regular expression for find html in data
    reghtml = re.compile('HTML')
    # we search the numbers with . in the url
    result = reg.search(url)
    # we get the begining position and the ending position of the numbers with .
    begin , end =  result.span()
    # we don't need the . at the end so we finish it earlier
    end =  end - 1
    #this string wil contain some zero because sometimes in the url it's 0001.jpg or 01.jpg or 1.jpg
    zero = ''
    #the i will count the zero
    i = 0
    #we put how 0 in zero that we have number in the url save one
    while  i < end -begin-1 :
        zero += '0'
        i += 1
    #here we get the extension a the end of the url .jpg here
    extension = url[end:]
    #count will determine how many times we have tried to download a file
    count = 0
    #while the download number is inferior of the limit let's goes on
    while start < limit :
        #we get the time
        t = datetime.datetime.now()
        # we make a file name with the epoch to be sure that the name will exist just one time
        name = "%s.%s"%(time.mktime(t.timetuple()),extension)
        # we make the url to download the file based on the url mixed with zero and the number of the download
        urlbis = "%s%s%s%s"%(url[:begin],zero,start,url[end:])
        #we try to download the file
        try :
            #here we open the url
            remoteFile = urllib2.urlopen(urlbis)
            #we read the file that we get
            data = remoteFile.read()
            # if the file does not exist sometimes we get a 404 error with the word HTML in it
            #so we check for it and if it is not in.
            if not reghtml.search(data) :
                #we create a file with the epoch name
                localFile = open(name, "wb")
                # we write the data in it
                localFile.write(data)
                #we close it
                localFile.close()
            else :
                #if there is the word HTML in it 
                #we end the loop
                break
        #here it is if we can't get any file at all
        except :
            # if the zero count equal zero we increase the count and put zero blank
            if i == 0 :
                zero = ''
                count += 1
            #here we just sustract zero
            else :
                # we reduce the zero counter
                i = i - 1   
                # we substract one zero
                zero = zero[:i] 
                # and we substract one to the counter of file to make it retry this file with one zero less
                start = start - 1           
        # if the failure counter is equal to the trial number we get out
        if count > trial  :
            break
        #we just increase the file counter
        start += 1
        

        
    


def main(argv=None):
    # we get the argument passed on the command line
    argv = sys.argv
    #we initialize the argument at none
    url = None
    #at which number we begin to download
    start =  None
    #how many download ?
    limit = None
    # how many time we will try to download
    trial = None
    #we get the argument in a list
    options =  sys.argv[1:]
    #we put the option one after one and initialise them
    for option in options :
        if not url :
            url = option
        else :
            if not start :
                start = option
            else :
                if not limit :
                    limit = option
                else :
                    trial = trial
    #if some options ar empty we put the default value
    if not start :
        start = 1
    if not limit :
        limit = 999 + start
    if not trial :
        trial = 3 
    #we call the download picture
    download_pictures(url,start,limit,trial)


if __name__ == "__main__":
    import sys
    #we call the main function
    sys.exit(main())


    
    


Script on the python cookbook


 
PUBLIÉ PAR BUSSIERE À L'ADRESSE 15:30 0 COMMENTAIRES   LIENS VERS CE MESSAGE
LIBELLÉS : DOWNLOAD PICTURE PICTURES JPG JPG URL LIST SERIES SERIE
VENDREDI 22 AOÛT 2008

Changing shortcut on a usb key v2
what
Changing the drive of a list of shortcut automatically must be placed in the shortcut directory on the usb key
why :
i've made some shortcut on my usb key for launchy and i had always to change them if on one pc the usb drive was i: on an other it was k: it was such a pain each time. Now it change all the shortcut automatically.
import sys,glob,re
import pythoncom
from win32com.shell import shell
import win32com
import win32com.client
import string
"""
By bussiere bussiere @at gmail.com
thanks to :
http://www.blog.pythonlibrary.org/
http://www.blog.pythonlibrary.org/?p=21
and :
http://codesnippets.joyent.com/tag/python
http://codesnippets.joyent.com/tag/python#post529
"""

__Author__ ="bussiere"
__Email__ = "bussiere @at gmail.com"
__Titre__ = "Changing shortcut on a usb key v2"
__Description__ = "Changing the drive of a list of shortcut automatically must be placed in the shortcut directory on the usb key"
__Discussion__ = "i've made some shortcut on my usb key for  http://www.launchy.net/ launchy and i had always to change them if on one pc the usb drive was i: on an other it was k: it was such a pain each time. Now it change all the shortcut automatically."
__Tags__ ="Usb shortcut windows key raccourcis"


class Win32Shortcut:
   def __init__(self, lnkname):
       self.shortcut = pythoncom.CoCreateInstance(
           shell.CLSID_ShellLink, None,
           pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
       self.shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(lnkname)

   def __getattr__(self, name):
       return getattr(self.shortcut, name)


def main():
  
   shell2 = win32com.client.Dispatch('WScript.Shell')
   # here we just get the drive where is the usb key
   drive = sys.path[0][0:2]
   #here we list all the file on the shortcut directory
   files = glob.glob(sys.path[0]+'/*')
   # here we take one file path
   path = glob.glob(sys.path[0])[0]
   #we normalize the path for python
   path = string.replace(path,'\\','\\\\')
   # we prepare a regexp for finding the shortcuts
   p = re.compile('\.lnk')
  
   for file in files :
       # we list all the files and find the shortcuts .lnk
    if p.search(file) :
           # we get the shortcut 
           s = Win32Shortcut(file)
           #we take the target directory of the shortcut
           itemPath = s.GetPath(0)[0]
           #we normalize the path of the shortcut
           file = string.replace(file,'\\','\\\\')
           # we overwrite the shortcut (same directory, same name).
           shortcut = shell2.CreateShortCut(file)
           #we replace the target path (drive = usb drive, path without the drive = itemPath[2:])
           shortcut.Targetpath =  drive + itemPath[2:]
           #we set the directory drive
           shortcut.WorkingDirectory = path
     #we save the shortcut
           shortcut.save()



if __name__ == "__main__":
   main()

