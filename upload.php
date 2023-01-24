<?php
    if (isset($_POST['submit'])) {
	    #$currentDirectory = getcwd();
        #$uploadDirectory = "/uploads/";
        $uploadDirectory = "/var/www/html/uploads/users/";

        $fileName = $_FILES['f']['name'];
        $fileTempName  = $_FILES['f']['tmp_name'];

    	$uploadPath = $currentDirectory . $uploadDirectory . basename($fileName); 
        move_uploaded_file($fileTempName, $uploadPath);

        echo "The file " . basename($fileName) . " has been uploaded";
    }

    
?>

<html>
<body>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        Upload a File:
        <input type="file" name="f">
        <input type="submit" name="submit" value="Upload">
    </form>
</body>
</html>
