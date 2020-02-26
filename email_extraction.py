import email
import imaplib
from bs4 import BeautifulSoup
import os
import mimetypes

date = []
fro = []
to = []
sub = []
text1 = []
con_typ = []


username = 'shree*******@******'
password = '************'
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)
mail.select('Inbox/foldername')
result, data = mail.uid('search',None,'ALL')
inbox_list = data[0].split()

for item in inbox_list:
    result2,email_data = mail.uid('fetch',item,'(RFC822)')
    raw_email = email_data[0][1].decode('utf-8')
    email_message = email.message_from_string(raw_email)
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = (email_message['Subject'])
    date_ = email_message['date']
    con_ = email_message['content_type']
    counter = 1
    for part in  email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        filename = part.get_filename()
        content_type = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(content_type)
            if not ext:
                ext = '.bin'
            if 'text' in content_type:
                ext = '.text'
            elif 'html' in content_type:
                ext = '.html'
            filename = 'msg-part-%08d%s' %(counter,ext)
        counter += 1
     # save file    
        
#     save_path = os.path.join('C:/Users/shreepad.k/NLP/', 'email')
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#     with open(os.path.join(save_path,filename),'wb') as fp:
#         fp.write(part.get_payload(decode= True))
        
        
     
        #     print(email_message.get_payload())
        #     print(content_type)
    print('@@@@@@@@@@@@@@@@@@@@@')
    if 'plain' in content_type:
        print(part.get_payload)
        con_typ.append(content_type)
        date.append(date_)
        fro.append(from_)
        sub.append(subject_)
        to.append(to_)
        text1.append(part.get_payload(decode=False))
#         text1.append(text)
        
#     elif 'multipart' in content_type:
#         print(part.get_payload)
#         con_typ.append(content_type)
#         date.append(date_)
#         fro.append(from_)
#         sub.append(subject_)
#         to.append(to_)
#         text1.append(part.get_payload(decode=False))

    elif 'html' in content_type:
        print('##### bs4 ####')
        html_ = part.get_payload(decode=False)
        soup = BeautifulSoup(html_, 'html.parser')
        text = soup.get_text()
#         print(date_)
        con_typ.append(content_type)
        date.append(date_)
#         print(from_)
        fro.append(from_)
#         print(to_)
        to.append(to_)
        print(subject_,'%%%$$$$$$$$########')
        sub.append(subject_)
#         subject.append.subject_
#         print(text)
        text1.append(text)
    else:
        print(content_type,'!!!!!!!!!!!!!!!!!!!!')
        pass
#         con_typ.append(content_type)
#         date.append(date_)
#         fro.append(from_)
#         sub.append(subject_)
#         to.append(to_)
#         text1.append(part.get_payload(decode=True))

# Convert into dataframe:

new = pd.DataFrame(list(zip(con_typ,date,to,fro,sub,text1)), 
               columns =['Content_type','Date','To','From','Subject','Text'])
        