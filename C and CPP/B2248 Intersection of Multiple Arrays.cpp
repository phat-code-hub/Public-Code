/*
    Given a 2D array nums that contains n arrays of distinct integers, 
    return a sorted array containing all the numbers that appear in all n arrays.

    For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 
    3 and 4 are the only numbers that are in all arrays.
    
    Created by Ueda
*/
#include<iostream>
#include <vector>
#include<unordered_map>
#include<algorithm>

int main(){
    std::vector<std::vector<int>> nums ={{3,1,2,4,5},{1,2,3,4},{3,4,5,6}};
    // Declare dictionary to count elements
    std::unordered_map<int,int> count_map;
    // Iterate over nums arrays to assign to count_map 
    for (std::vector<int>& num:nums){
        for (int n:num){
            count_map[n]++;
        }
    }
    int n=int(nums.size());
    // Result array 
    std::vector<int> res;
    for(auto [key,val]:count_map){
        // Add to result array if value equal n
        if (val == n) res.push_back(key);
    };
    // Sort the result
    sort(res.begin(),res.end());
    for (int ans:res){
        std::cout<<ans<<std::endl;
    }
    return 0;
}