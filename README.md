# Http Server for file handling
Python Based File Sever

Watch the demo of the Application [here](https://www.youtube.com/watch?v=F1jedLLX1aQ&feature=youtu.be) 

The server is implemented using Python's HTTPServer class. It implements `do_GET` and `do_POST` methods to handle requests from client. The server supports following operations
  - Display list of available files
  - Update file
  - Delete file

The client gets an interface for connecting to sever using Browser. I have hosted the server on `localhost` of my machine at `PORT=8888`. But this application can be configured to run on any machine by changing the `HOST` and `PORT` in `configure.py` file.

The client sends `GET/POST` requests from browser. The working flow of read,list,update,delete opertations is given below:
- **read** : This is used to display contents of a specified file. The client sends a POST request and filename is accessed at the server end using cgi FieldStorage api with the help of form elements names.
- **list** : list is used to list the files that are available at the sever. 
- **update** : This is used to update the contents of a file at the server. The client sends the file to be updated and the new contents using POST request. At the server side the file is opened and write mode is modified with the new contents.
- **delete** : This feature lets you to delete a file.
  

### Implementation Details

The serverside is developed using python. First `HTTPServer(('', PORT), requestHandler)` creates a server that runs forever and accepts requests until it is stopped manually.

#####`def do_GET(self)`
This method uses `path.endswith()` to check for the data files to serve to the client. This check is kept so that only data files are served and source code is hidden from the user.

#####`def do_POST(self)`
This method handles POST requests. It checks whether it is `read`,`delete` or `update` requests and handles the requests accordingly. Html reaponse is created using following code snippet.
```
self.send_response(200)
self.end_headers()
```

`wfile.write()` function is used to write html file. Errors are handled and appropriate 404 reaponse is sent using `send_error(404)`.

### Version
1.0

### Code Structure

* HttpServer.py - The heart of the app, python server.
* index.html - Frontend interface for the client. 


### Installation

```sh
$ git clone https://github.com/rohanbharadwaj/File-Sever.git
$ cd server
$ python HTTPServer.py
```

### Configuration
To chnage the Host and Port of the Server edit the file `configure.py`

```sh
$ vim configure.py

PORT = 8888         #The port where the server runs
HOST = 'localhost'  # The host address where the server is hosted.
```



### Screenshots 

![ScreenShot](https://github.com/rohanbharadwaj/File-Server/blob/master/screenshots/pic1.png)
![ScreenShot](https://github.com/rohanbharadwaj/File-Server/blob/master/screenshots/pic2.png)
![ScreenShot](https://github.com/rohanbharadwaj/File-Server/blob/master/screenshots/pic3.png)
![ScreenShot](https://github.com/rohanbharadwaj/File-Server/blob/master/screenshots/pic4.png)
![ScreenShot](https://github.com/rohanbharadwaj/File-Server/blob/master/screenshots/pic5.png)

### Requirements

* Python 2.7
* Browser
