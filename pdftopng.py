#src_pdf内のファイルをdst_imgへpngファイルを作成する
import subprocess
import os

for file in os.listdir("src_pdf"):
    print( file )
    if file[7]=='a':
        dirname = os.path.join("img","pdf",file[9:11],file[4:7]+'02')
    else:
        dirname = os.path.join("img","pdf",file[9:11],file[4:7]+'01')

    if os.path.isdir( dirname )==False:
        os.makedirs(dirname,exist_ok=True)

    cmd = 'pdftocairo -png src_pdf\%s %s/'%(file,dirname)

    print( dirname )

    #cmd = 'dir'
    returncode = subprocess.Popen( cmd ,shell=True)

    print( returncode )
