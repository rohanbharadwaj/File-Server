# Http Server for file handling
Python Based File Sever

The server is implemented using Python's HTTPServer class. It implements `do_GET` and `do_POST` methods to handle requests from client. The server supports following operations
  - Display list of available files
  - Update file
  - Delete file

Watch the demo of the Application [here](https://www.youtube.com/watch?v=F1jedLLX1aQ&feature=youtu.be) 
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
* index.html - Frontend client developed in HTML


### Installation

```sh
$ git clone https://github.com/rohanbharadwaj/------
$ cd server
$ python HTTPServer.py
```

### Requirements

* Python 2.7
* Browser

### Todo's

 - Write externel CSS

License
----

GNU GPL v2
