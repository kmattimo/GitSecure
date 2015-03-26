import tarfile,sys
from os import listdir
from os.path import isfile, join
 
# untars single file and drops it in destpath
def untar(fname,destpath=None):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        if destpath is not None:
	        tar.extractall(destpath)
	        print "Extracted in " + destpath
        else: 
        	tar.extractall();
	        print "Extracted in Current Directory"
        tar.close()
    else:
        print "Not a tar.gz file: '%s '" % fname

# generates list of tarballs at mypath 
def generate_tar_list(mypath):
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) 
					and f.endswith("tar.gz")]
	print onlyfiles;
	return onlyfiles;

# careful using this when internal directories are the same 
# name in the tarfile. They will overwrite eachother
def untar_dir(mypath, destpath=None ):
	tar_list = generate_tar_list(mypath)
	for t in tar_list:
		if destpath is None:
			untar(mypath + "/" + t);
		else:
			untar(mypath + "/" + t, destpath);