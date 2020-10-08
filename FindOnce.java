/*
    Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice.

    Example 1:

    Input:
    N = 11
    arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
    Output: 4
    Explanation: 4 is the only element that
    appears exactly once.

    Your Task:
    You don't need to read input or print anything. Complete the function findOnce() which takes sorted array and its size as its input parameter and returns the element that appears only once.

    Expected Time Complexity: O(log N)
    Expected Auxiliary Space: O(1)
*/

package com.exercises;

public class FindOnce {
    public static void main( String args[]){

        int arr_length = 11;
        int arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65};
        int result = findOnce(arr,arr_length);
        System.out.println("element which appears only once is:" + result);
    }

    private static int findOnce(int[] arr, int arr_length) {
     int result = 0;
     for(int i=0;i<arr_length-1;i++){
             if (arr[i]==arr[i+1]){
                 i++;
             }
             else {
                 result = arr[i];
                 break;
             }
     }
     return result;
    }
}
