Can use old crs.pem

Also if you use email auth, might be automatic

Keep the api.stechanlaytics.com.key there since that's local, can copy out rest and load new ones.

Guide

sudo openssl genrsa -out private.key 2048

From <[https://www.namecheap.com/support/knowledgebase/article.aspx/9592/2290/generating-a-csr-on-amazon-web-services-aws/](https://www.namecheap.com/support/knowledgebase/article.aspx/9592/2290/generating-a-csr-on-amazon-web-services-aws/)>

sudo openssl req -new -key private.key -out csr.pem

From <[https://www.namecheap.com/support/knowledgebase/article.aspx/9592/2290/generating-a-csr-on-amazon-web-services-aws/](https://www.namecheap.com/support/knowledgebase/article.aspx/9592/2290/generating-a-csr-on-amazon-web-services-aws/)>

Use the following details

Common Name: api.stechanalytics.com

Organization: Default Company Ltd

Locality: Default City

Country: GB

Key Size: 2048 bit

From <[https://www.sslshopper.com/csr-decoder.html](https://www.sslshopper.com/csr-decoder.html)>

CNAME

HOST _31ee43a89ec4d60e81a43c7c5fa8e3d1

Host is without stechanalytics.com at the end

Then value is value

Make sure names are

-rw-r--r--   1 ec2-user ec2-user   1679 May  2 14:32 api.stechanalytics.com.key

-rw-r--r--   1 ec2-user ec2-user  10602 May  2 14:32 api_stechanalytics.com_2024.zip

-rw-rw-r--   1 ec2-user ec2-user   5655 May  2 14:32 api_stechanalytics_com.ca-bundle

-rw-rw-r--   1 ec2-user ec2-user   2247 May  2 14:32 api_stechanalytics_com.crt

Then restart

 sudo systemctl restart graffiti_api.service