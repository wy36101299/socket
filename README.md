socket
======

簡單的socket example  
分為兩個檔案 server.py and client.py  
server.py 為server端，client.py為client端(multi thread處理)  

###如何使用
--------------

    $ python server.py port
    $ python client.py port
    
ip 寫在程式裡面，預設為 localhost，port 為自行輸入

###example
--------------

    $ python server.py 8880
    $ python client.py 8880
    
server 以prot 8880開啟
client 以prot 8880連線

###reference
--------------
[Python socket document](https://docs.python.org/2/library/socket.html)  
[Python socket – network programming tutorial](http://www.binarytides.com/python-socket-programming-tutorial/)  
[Python socket – network programming tutorial 中文翻譯](http://www.oschina.net/question/12_76126)  
