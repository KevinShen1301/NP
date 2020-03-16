<?php

if(isset($_POST["submit"])){
/* API URL */
$url = 'http://0.0.0.0:5000/addports';
  
/* Init cURL resource */
$ch = curl_init($url);
  
/* Array Parameter Data */
$data = ['studentid'=>$_POST['id']];
  
/* pass encoded JSON string to the POST fields */
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
  
/* set the content type json */
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
  
/* set return type json */
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  
/* execute request */
$result = curl_exec($ch);
echo $result;     
/* close cURL resource */
curl_close($ch);

/* API URL */
$url = 'http://0.0.0.0:5000/mailservice';
  
/* Init cURL resource */
$ch = curl_init($url);
  
/* Array Parameter Data */

  
/* pass encoded JSON string to the POST fields */
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($result));
  
/* set the content type json */
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
  
/* set return type json */
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  
/* execute request */
$result = curl_exec($ch);
echo $result;     
/* close cURL resource */
curl_close($ch);



}
?>

<HTML>
<form method="post" , action = ''>

Studentid<input type = "text" name = "id">
<input type = "submit" value = "submit" name="submit">

</form>

</HTML>