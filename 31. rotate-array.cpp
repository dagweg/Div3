class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        ios::sync_with_stdio(0);
        cin.tie(0);

        k %= nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());

    }
};
