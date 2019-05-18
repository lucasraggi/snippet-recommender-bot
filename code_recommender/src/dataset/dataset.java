public class DataSet{
    public void bubbleSort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr[j] > arr[j+1])
                {
                    // swap temp and arr[i]
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
    }

    public void bubbleSort(float arr[]) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr[j] > arr[j+1])
                {
                    // swap temp and arr[i]
                    float temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
    }

    public void bubbleSort(double arr[]) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr[j] > arr[j+1])
                {
                    // swap temp and arr[i]
                    double temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
    }


    public void selectionSort(int arr[]){
        int n = arr.length;
 
        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
 
            // Swap the found minimum element with the first
            // element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
        
    public void selectionSort(float arr[]){
        int n = arr.length;
 
        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
 
            // Swap the found minimum element with the first
            // element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    public void sort(double arr[]){
        int n = arr.length;
 
        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
 
            // Swap the found minimum element with the first
            // element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

        public int binarySearch(int arr[], int l, int r, int x) {
            if (r>=l) 
            { 
                int mid = l + (r - l)/2; 
       
                // If the element is present at the  
                // middle itself 
                if (arr[mid] == x) 
                   return mid; 
       
                // If element is smaller than mid, then  
                // it can only be present in left subarray 
                if (arr[mid] > x) 
                   return binarySearch(arr, l, mid-1, x); 
       
                // Else the element can only be present 
                // in right subarray 
                return binarySearch(arr, mid+1, r, x); 
            } 
       
            // We reach here when element is not present 
            //  in array 
            return -1; 
        } 

        public float binarySearch(float arr[], int l, int r, float x) {
        if (r>=l) 
        { 
            int mid = l + (r - l)/2; 
   
            // If the element is present at the  
            // middle itself 
            if (arr[mid] == x) 
               return mid; 
   
            // If element is smaller than mid, then  
            // it can only be present in left subarray 
            if (arr[mid] > x) 
               return binarySearch(arr, l, mid-1, x); 
   
            // Else the element can only be present 
            // in right subarray 
            return binarySearch(arr, mid+1, r, x); 
        } 
   
        // We reach here when element is not present 
        //  in array 
        return -1; 
    } 

    public double binarySearch(double arr[], int l, int r, double x) {
        if (r>=l) 
        { 
            int mid = l + (r - l)/2; 
   
            // If the element is present at the  
            // middle itself 
            if (arr[mid] == x) 
               return mid; 
   
            // If element is smaller than mid, then  
            // it can only be present in left subarray 
            if (arr[mid] > x) 
               return binarySearch(arr, l, mid-1, x); 
   
            // Else the element can only be present 
            // in right subarray 
            return binarySearch(arr, mid+1, r, x); 
        } 
   
        // We reach here when element is not present 
        //  in array 
        return -1; 
    } 

}

