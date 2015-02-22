#!/usr/bin/python
"""HTTPServer.py: Python Server to handle file requests

File Server implemented in python that accepts GET, POST requests from 
clients. Supports read, update, delete of files.

How to run?

$python HTTPServer.py

then point your browser at http://localhost:8080

"""
__author__      = "Rohan Bharadwaj"
__copyright__   = "Copyright 2015, Rohan Bharadwaj"
__license__ = "GPL v2.0"
__version__ = "1.0"
__email__ = "rbharadwaj@cs.stonybrook.edu"

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from os import curdir, sep
import os


PORT = 8099


class requestHandler(BaseHTTPRequestHandler):
    """
    Implements do_GET and do_POST to handle requests from clients.
    """
    
    def do_GET(self):
        """
        Handles GET requests.
        
        Checks the file format to serve only data files and hide source files.
        """
        if self.path=="/":
            self.path="/index.html"
        flag = 0    
        try:
            #print self.path 
            sendReply = False
            if self.path.endswith(".json"):
                mimetype='application/json'
                sendReply = True
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path=="/read":
                mimetype='text/html'
                sendReply = True   
            if self.path=="/list.html":
                flag = 1
                sendReply = True  
        
            if sendReply == True:
                if flag:
                    files = [f for f in os.listdir('.') if os.path.isfile(f)]
                    self.send_response(200)
                    self.end_headers()  
                    self.injectHeader()
                    self.wfile.write('<div class="jumbotron"><div class="container">')
                    self.wfile.write('<div class="panel panel-default"><div class="panel-body"><h3>Files on server</h3></div></div>')
                    self.wfile.write('<ul class="list-group">')
                    for f in files:
                        if ".json" in f or ".txt" in f:
                            self.wfile.write('<li class="list-group-item">'+f+'</li>')
                    self.wfile.write('</ul></div></div>')        
                    self.injectFooter()        
                    self.injectHome()        
                else:            
                    f = open(curdir + sep + self.path) 
                    self.send_response(200)
                    self.send_header('Content-type',mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
            return
        
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


    def do_POST(self):
        """
        Handles POST requests
        
        Handles update,read,delete based.
        """
        if self.path=="/update":
            try:
                form = self.getData()
                file = form["file_name"].value
                lines = form["content"].value
                with open(file, "w") as f:
                    f.write(lines)
                self.send_response(200)
                self.end_headers()
                self.injectHeader()
                self.wfile.write('<div class="alert alert-success" role="alert">'+file+' updated successfully</div>')   
                self.injectFooter()
                self.injectHome()         
            except (IOError,KeyError) as e:
                self.send_error(404,'File Not Found: %s' % self.path)

        if self.path=="/read":
            try:
                form = self.getData()
                file = form["file_name"].value
                f = open(file)
                lines = f.readlines()
                self.send_response(200)
                self.end_headers()
                self.injectHeader()
                self.wfile.write('<div class="jumbotron"><div class="container">')
                self.wfile.write('<div class="panel panel-default"><div class="panel-heading">'+file+'</div><div class="panel-body">')
                for line in lines:
                    self.wfile.write(line)
                self.wfile.write('</div></div></div></div>')    
                self.injectFooter()
                self.injectHome()         
            except (IOError,KeyError) as e:
                self.send_error(404,'File Not Found: %s' % self.path)                
                
        if self.path=="/delete":
            try:
                form = self.getData()
                file = form["file_name"].value
                os.remove(file)
                self.send_response(200)
                self.end_headers()
                self.injectHeader()
                self.wfile.write('<div class="alert alert-danger" role="alert">'+file+' deleted successfully</div>')   
                self.injectFooter()
                self.injectHome()  
            except (OSError,KeyError) as e:
                self.send_error(404,'File Not Found: %s' % self.path)                                 
            return
     
    def getData(self):
        return cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],})   
        
    def injectHeader(self):
        self.wfile.write('<html>' \
                    '<head>' \
                    '<title>File Client</title>' \
                    '<link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">' \
                    '</head><body>')
         
    def injectFooter(self):
        self.wfile.write('</body></html>')
    
    def injectHome(self):
        self.wfile.write('<a class="btn btn-primary" HREF="index.html"><span class="glyphicon glyphicon-home"> Home</span></a>')    
                          
            
try:
    server = HTTPServer(('', PORT), requestHandler)
    print 'Started httpserver on port ' , PORT
    server.serve_forever()

except KeyboardInterrupt:
    print 'shutting down the web server'
    server.socket.close()