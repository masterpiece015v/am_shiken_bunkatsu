from lib.img_lib import pdf_mj
from lib.opencv_lib import cut_mj
import os
import shutil

def rename(dir_path,file_name):
    #一時フォルダ
    dir_path2 = dir_path + "/temp"
    os.mkdir(dir_path2)
    #ファイル名一覧取得
    files = os.listdir(dir_path)
    print(files)
    q_no = 1
    for file in files:
        if q_no < 10:
            re_file_name = file_name + "0" + "%s.png"%q_no
        else:
            re_file_name = file_name + "%s.png"%q_no

        if os.path.isfile(dir_path+"/"+file):
            os.rename(dir_path + "/" + file , dir_path2 + "/" + re_file_name)
            print( file + "→" + re_file_name)
            #os.remove(dir_path + "/" + file)
            q_no = q_no + 1

    files = os.listdir(dir_path2)
    #移動
    for file in files:
        shutil.move(dir_path2+"/"+file,dir_path+"/"+file)
    #一時フォルダの削除
    shutil.rmtree(dir_path2)

def ip_rename(dir_path,file_name):
    files = os.listdir(dir_path)
    q_no = 1
    for file in files:
        if q_no < 10:
            re_file_name = file_name + "00" + "%s.png"
        elif q_no >= 10 and q_no <= 99:
            re_file_name = file_name + "0" +"%s.png"
        else:
            re_file_name = file_name + "%s.png"

        os.rename(dir_path + "/" + file,dir_path + "/" + re_file_name%q_no)
        print( file + "→" + re_file_name%q_no)
        q_no = q_no + 1

def main():
    # pdf から pngへ変換 引数はディレクトリ
    # pdf_mj.pdf_to_png("pdf","img/pdf")
    # 問題ごとに分割する 引数は　srcディレクトリ,desディレクトリ,ファイル名,分割度数

    nendolist = []
    nendolist.append("h3002")

    #nendoki = "h253"
    shiken = "fe"
    for nendoki in nendolist:
        #ディレクトリがなければ作る
        dirimgpath = "img/mondai/%s/%s"%(shiken,nendoki)
        dirpdfpath = "img/pdf/%s/%s"%(shiken,nendoki)
        if os.path.isdir(dirimgpath)==False:
           os.mkdir(dirimgpath)
        if os.path.isdir(dirpdfpath)==False:
            os.mkdir(dirpdfpath)
        #分割
        cut_mj.cut_mondai(dirpdfpath,dirimgpath,"%s%s"%(shiken,nendoki),2)
        #リネーム
        #rename("img/mondai/%s"%nendoki,"%s%s"%(shiken,nendoki))

if __name__ == "__main__":

    main()

#python -m pip install opencv-python
