<html>

<h1>Hey Oh, this is radical</h1>

<?php
// SERVER

if(getenv('REQUEST_METHOD') == 'POST') {
	$client_data = file_get_contents("php://input");
	$all_json = json_decode($client_data);
	$pattern = "/(\/giphy)\s(.*)/";
	$check = $all_json->text;

	if (preg_match($pattern, $check, $matches_out))
	{
		print_r($matches_out[2]);
		$search_term = $matches_out[2];
		//$search_term = var_dump($matches_out[2]);
		shell_exec("python giphyBot.py " . $search_term);
		echo "
			<SERVER>
				Hallo, I am server
				This is what I've got from you
				$client_data
				This is the search term
				$searchterm
			</SERVER>
		";
	}
	else
	{
		echo "Does not match";	
	}
	exit();
}
?>
</html>
