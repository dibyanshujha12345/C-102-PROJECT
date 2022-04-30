import dropbox


def upload_file():
    access_token="sl.BGijv93-wkihqYQp6-Aa169mxQd_tP3TOqIhO3L-r0cDoxO9P9mBWpajRZyn21OTYbxLsLwr9r_n-5iP146iIKrUqbPjwJg8v52dpVloQSZMY4Pc8Qu_e3vFmgHLGEcgb8s6M8Ofoo7K"
   
    file_from="C:\\Users\Sabita Jha\Pictures\Screenshots"
    file_to="https://www.dropbox.com/sh/0eov6pq44nsfeja/AACHRNm3_adNTj97HHR0rXjva?dl=0"
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!!")


upload_file()        