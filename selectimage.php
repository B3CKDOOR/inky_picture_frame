<?php
        $path = "mailpics"; // define foldername of the images
        $fullpath = "/frame/$path/";

        $mailimg_arr = scandir($path);

        if(!empty($_GET['displayimg'])) { // when an image is clicked, display it on the picture frame
                $img_arg = $fullpath . escapeshellcmd($_GET['displayimg']);
                shell_exec("python3 /frame/image.py $img_arg > /dev/null &"); // the image already has the right size so here we don't have to use anyimage.py
                shell_exec("cp $img_arg /frame/recentimage/recent.jpg > /dev/null &"); // copy the image to the 'recentimage' folder so that we can revert back to it
                $success = "<div class='alert alert-success' role='alert'><strong>Picture is being displayed!</strong><hr>This can take a little while.</div>";
        }
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="style.css" rel="stylesheet">

    <title>Show picture</title>
  </head>
  <body>
    <div class="container-sm" style="padding:20px;">
    <h1>Show picture</h1>
    <t>Choose the picture you would like to be displayed:</t>

        <?php
        if(!empty($success)){
                echo $success;
        }
        foreach($mailimg_arr as $img) { // list the pictures and link them to the GET parameter which triggers script execution
                if (preg_match('/^[^\.][^\/]*\.(jpg|jpeg|png|gif|bmp|webp)$/i', $img)) {
                        echo "<a href='?displayimg=$img'><img src='$path/$img' class='float-start img-thumbnail img-fluid rounded' style='max-width:150px;margin:5px;'></a>\n";
                }
        }
        ?>
        </div>

  </body>
</html>
