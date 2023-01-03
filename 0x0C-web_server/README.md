# 0x0C. Web server

# What is a web server?
A web server is a computer software and underlying hardware that accepts requests via HTTP or its secure variant HTTPS

**Concepts learned:**
- Primary role of a web server: The primary role of a web server is to store, process, and deliver requested web pages to end users.
- Child process: A child process is a process created by another process usually called the parent process. The benefit of a child process is that it can start or
stop at will without affecting the parent process. When a parent process dies, it however affects a child process. Apache uses child processes to handle maximum
webpage requests from end users (i.e Apache creates a new child process when the number of requests exceed the maximum number of allowed requests).

# HTTP requests
These are requests that endusers make from their browsers to the webserver. The common HTTP request includes: GET, HEAD, POST, PUT, DELETE, OPTIONS.
- GET - used to request for webpages or data from the webserver.
- HEAD - has the same effect as GET but in this case, the webserver returns only the HEAD of the HTTP response.
- POST - used to post data to the webserver.
- PUT - used to update data already available in the webserver.
- DELETE - used to delete data from the webserver.
- OPTIONS - displays the HTTP request options available to a enduser.
