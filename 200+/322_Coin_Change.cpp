#define CANT_BE_ACHIEVE -1

class Solution
{
public:
    int coinChange(vector<int> &coins, int amount)
    {
        vector<int> dp(amount + 1, CANT_BE_ACHIEVE);
        dp[0] = 0;
        for (int curr_amount = 1; curr_amount <= amount; ++curr_amount)
        {
            int minNeededCoins = INT_MAX;
            for (int coin_i = 0; coin_i < coins.size(); ++coin_i)
            {
                if (curr_amount - coins[coin_i] >= 0 && dp[curr_amount - coins[coin_i]] != CANT_BE_ACHIEVE)
                {
                    minNeededCoins = min(minNeededCoins, dp[curr_amount - coins[coin_i]] + 1);
                }
            }
            if (minNeededCoins != INT_MAX)
            {
                dp[curr_amount] = minNeededCoins;
            }
        }
        return dp[amount];
    }
};