<?php
if ($_GET['randomId'] != "Jv5nLcTQe9IhdOnPtOEgDa6zrwGqLL_oFzh4DFdxQla_CpfOIRAu2jfFPoSwsFfG") {
    echo "Access Denied";
    exit();
}

// display the HTML code:
echo stripslashes($_POST['wproPreviewHTML']);

?>  
