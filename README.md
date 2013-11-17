ip2name
=======

A script to convert all IPs in a text file to resolved hostnames

Here is an example:

```
$ cat testfile.txt 
8.8.8.8 google dns server #1
8.8.4.4 google dns server #2

299.222.222.222 not a valid IP
this is what www.microsoft.com resolves to: 64.4.11.42

$ python ip2name.py < testfile.txt
[google-public-dns-a.google.com] google dns server #1
[google-public-dns-b.google.com] google dns server #2

299.222.222.222 not a valid IP
this is what www.microsoft.com resolves to: [64.4.11.42]
```

