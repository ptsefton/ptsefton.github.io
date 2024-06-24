import os
from subprocess import call
import codecs
import shutil
from bs4 import BeautifulSoup
import base64




for root, dirs, files in os.walk("."):
    for file in files:
       # if len(root) == 2:
       
        meta_path = root.split("/")
        filename = os.path.join(root,file)
        if len(meta_path) == 5:
            filename = os.path.join(root,file)
            if file =="index.html":
                #Fix image & href links to attachemnts like images and PDF versions
                s = BeautifulSoup(open(filename))
                temp_html = filename + ".temp"
                def redo_attachments(el, att):
                    for i in s.find_all(el):
                        
                        src = i.get(att)
                        
                        if src != None and src.startswith('./'):
                            src = "/blog/" + "/". join(meta_path[1:]) + "/" + src[2:]
                            print "Redid attribute: %s" % src
                            i[att] = src

                #rewrite doc with new attachements
                redo_attachments("a","href")
                redo_attachments("img","src")
                open(temp_html,'w').write(str(s))
                
                temp_md =  filename.replace(".html",".mdtemp")
                #call(["pandoc", "-f","html","-o", filename + ".md", "-t", 'html', "pandoc.in"]) #--selfcontained
                call(["pandoc", "-f","html","-o", temp_md, "-t",'markdown', '--atx-headers', temp_html])
                raw = open(temp_md, 'r').read()
                html = raw.split("\n")
                print root
                #print html
                if len(html) > 8:
                    title = html[9].replace("# ", "")
                    if title == "None":
                        title = "Yet another untitled post"
                    meta = '---\nTitle: "%s"\n' % title
                    meta += "Slug: %s\n" % meta_path[4]
                    meta += "Date: %s-%s-%s\n\n" % (meta_path[1], meta_path[2], meta_path[3])
                    meta += "---"
                    open(filename.replace(".html",".md"),'w').write(meta + "\n".join(html[12:]))
                else:
                    print "something wrong with ", root, file
            
                
