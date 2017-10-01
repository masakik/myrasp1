 sudo mkdir /var/tmp 

then edit the fstab file by

 sudo nano /etc/fstab

and add the line

 tmpfs /var/tmp tmpfs nodev,nosuid,size=1M 0 0 

save and close the file. Now issue

 sudo mount -a

To check if your operation succeeded issue

 df

