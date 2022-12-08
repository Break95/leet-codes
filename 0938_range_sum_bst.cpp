class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int result = 0;

        if (root->val >= low && root->val <= high)
            result += root->val;

        if(root->val > low)
            if(root->left != nullptr)
                result += rangeSumBST(root->left, low, high);
        if(root->val < high)
            if(root->right != nullptr)
                result += rangeSumBST(root->right, low, high);

        return result;
    }
};
