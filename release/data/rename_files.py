import glob, os
import sys

dir_rename = sys.argv[1]
#def rename(dir, pattern, titlePattern):

id_count = 0
for pathAndFilename in glob.iglob(os.path.join(dir_rename, "*.jpg")):
    #title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    title, ext = os.path.splitext(pathAndFilename)
    #print title
    #print ext
    path_file = os.path.dirname(pathAndFilename)
    print "------------------------"
    print "mv "+ pathAndFilename +" "+ os.path.join(path_file, "underwater_"+str(id_count)+".jpg")
    print "mv "+ title+".txt" +" "+ os.path.join(path_file, "underwater_"+str(id_count)+".txt")
    path_txt_file = title + ".txt"
    print "------------------------"
    
    os.rename(pathAndFilename, os.path.join(path_file, "underwater_"+str(id_count)+".jpg"))
    os.rename(path_txt_file, os.path.join(path_file, "underwater_"+str(id_count)+".txt"))
    id_count = id_count + 1
