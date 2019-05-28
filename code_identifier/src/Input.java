int binarySearch(int arr[], int l, int r, int x) 
    { 
        if (r>=l) 
        { 
            int mid = l + (r - l)/2; 
   
            // If the element is present at the  
            // middle itself 
            if (arr[mid] == x) 
               return mid; 
   
   
            return binarySearch(arr, mid+1, r, x); 
        } 
   
        // We reach here when element is not present 
        //  in array 
        return -1; 
    } 