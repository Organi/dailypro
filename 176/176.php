    <?php
    	// Days of the Week Definition for Quick Sorting
    	$days = Array(
    		"Mon" => 0,
    		"Tue" => 1,
    		"Wed" => 2,
    		"Thu" => 3,
    		"Fri" => 4,
    		"Sat" => 5,
    		"Sun" => 6
    	);
    
    	// Get Data
    	$handle = fopen('pivot.txt', 'r');
    	$pivotData = Array();
    	while (($line = fgets($handle)) !== false) {
    		$lineData = explode(' ', $line);
    		$node = $lineData[0];
    		$dayOfWeekNum = $days[$lineData[1]];
    		$kwh = trim(str_replace("\n\r", "", $lineData[2]));
    		if (isset($pivotData[$node][$dayOfWeekNum])) {
    			$pivotData[$node][$dayOfWeekNum] += $kwh;
    		} else {
    			$pivotData[$node][$dayOfWeekNum] = $kwh;
    		}
    	}
    	fclose($handle);
    
    	// Sort Data
    	foreach ($pivotData as $node=>&$weekData) {
    		foreach ($days as $day) {
    			if (!isset($weekData[$day])) {
    				$weekData[$day] = 0;
    			}
    		}
    		ksort($weekData);
    	}
    	ksort($pivotData);
    
    	// Print Data
    	echo "\n\n|      ";
    	foreach ($days as $day=>$dayNo) {
    		echo "| ".$day." ";
    	}
    	echo "|\n";

        unset($weekData);
        unset($dayData);
        unset($node);
    	foreach ($pivotData as $node=>$weekData) {
    		echo "| ".$node." ";
            foreach ($weekData as $dayData) {
    			echo "|";
    			$spacesToFill = 5-strlen($dayData);
                echo str_repeat(" ", $spacesToFill/2);
    			if ($spacesToFill % 2 != 0) {
                    echo " ";
    			}
                echo $dayData;
                echo str_repeat(" ", $spacesToFill/2);
    		}
    		echo "|\n";
    	}
    ?>