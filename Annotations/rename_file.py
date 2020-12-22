import os
import glob

def rename(dir, pattern, titlePattern):
    os.chdir(dir)
    for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
        newfile = '{}.jpg'.format(index)
        os.rename(oldfile, newfile)
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, titlePattern % title + ext))

# rename(r'directory path', r'*.jpg', r'ResearcherLastName_%s')
