# oh-my-bet (8 solves, 740 pts)

Arbitrary file read + SSRF + CRLF + FTP bounce attack + Python binary deserialization

### 1. Arbitrary file read
The app is vulnerable (avatar parameter) so we can read any file. Get sources. From sources it becomes clear what other services/hosts are used: 
- FTP (172.20.0.2:8877)
- MySQL
- Redis
- MongoDB

### 2. SSRF + CRLF
The app uses urllib.request.urlopen for retrieving avatar and as there no restiction on schema and path we can communicate with other services through SSRF. So in this way we can communicate with FTP server, which contains config.json and its source code (ftp-server.py). From config.json we can get address we didn't know, so we have:
- FTP (172.20.0.2:8877)
- MySQL (172.20.0.3:3306)
- Redis (172.20.0.4:6379)
- MongoDB (172.20.0.5:27017)

The server uses Python 3.6.0 and urllib.request.urlopen has CRLF issue, so now we can build a bit more complex SSRF requests.

### 3. Python binary deserialization
From task description we need to run /readflag to get flag, so we need RCE. After spending some time looking around I saw that MongoDB uses pickle serialized object to store session data. If we somehow can add our own object into the DB we'll get RCE. Unfortunetley, MongoDB uses binary protcol so existing SSRF + CRLF wouldn't be enought to create our entry.

### 4. FTP bounce attack
In ftp-server.py we see line "handler.permit_foreign_addresses = True" which enables FXP, so enables FTP bounce attack. Now we can perform complex enought SSRF to send data to MongoDB (storing package from my server to FTP and sending package from FTP to MongoDB).

Details in sources.
