## How to Use the Mailbot
1. Clone the Repo and open the Mailbot folder in your favourite Code environment.
2. In the email_addresses.txt file, add the mail addresses you want to reach and add a name if you want to address the recepient personally or add a "-" if you want to use the default greeting. It is important that the mails and the names are separated by a comma. (see the addresses in the file)
3. In the email_text.txt file, add the text you want to send by mail afterwards. Adjust it as desired.
4. Add the Newsletter you want to attach in the same folder as the three other files.
5. In the mailbot.py file, you have to change the following lines:
  - line 20 & line 84: replace the "The_SCL_Times-Volume_19.pdf" by the name of your current pdf file. (if you saved the pdf file in the folder as "The_SCL_Times-Volume_20.pdf" you also have to call it like this in the code) 
6. run the mailbot.py file
