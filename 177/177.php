<?php
    	function quickSort($data, $key) {
    		// Data is already sorted
    		if ((count($data) == 2 && $data[0] <= $data[1]) || count($data) <= 1) {
    			return $data;
    		}
    		$sList = Array();
    		$gList = Array();
            $equalList = Array();
    		foreach ($data as $num) {
    			if ($num < $data[$key]) {
    				$sList[] = $num;
    			} else if ($num == $data[$key]) {
                    $equalList[] = $num;
                } else {
    				$gList[] = $num;
    			}
    		}
    		$sortedSlist = quickSort($sList, rand(0, count($sList)-1));
    		$sortedGlist = quickSort($gList, rand(0, count($gList)-1));

    		return array_merge($sortedSlist, $equalList, $sortedGlist);
    	}

    	// Get Data
    	$handle = fopen('data.txt', 'r');
    	$sizeOfList = 0;
    	$rawData = Array();
    	while (($line = fgets($handle)) !== false) {
    		$rawData[] = trim(str_replace("\n\r", "", $line));
    		$sizeOfList++;
    	}
    	fclose($handle);
    	$startingKey = rand(0, $sizeOfList-1);

    	$sortedData = quickSort($rawData, $startingKey);
    	foreach ($sortedData as $number) {
    		echo $number."\n";
    	}
        echo "\n".count($rawData)." items in original list.";
        echo "\n".count($sortedData)." items sorted.\n\n";
?>