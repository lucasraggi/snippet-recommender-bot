int binarySearch(int arr[], int l, int r, int x) 
    { 
        if (r>=l) 
        { 
            int mid = l + (r - l)/2; 
            if (arr[mid] == x) 
               return mid;
        }
    } 