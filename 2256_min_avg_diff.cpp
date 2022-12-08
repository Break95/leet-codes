class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        long lsum = 0;
        long rsum = 0;
        int minDiffVal = 2147483647;
        int minDiffIdx = 0;
        int len = nums.size();

        for(auto x: nums)
            rsum += x;

        long posDiff;
        long rhs;

        for (int i = 0; i < len; ++i){
            lsum += nums[i];
            rsum -= nums[i];

            if (len-i-1 > 0)
                rhs = std::floor(rsum/(len-i-1));
            else
                rhs = 0;

            posDiff = std::abs(std::floor(lsum/(1 + i)) - rhs);

            if (posDiff < minDiffVal){
                minDiffIdx = i;
                minDiffVal = posDiff;
            }

        }

        return minDiffIdx;
    }
};
