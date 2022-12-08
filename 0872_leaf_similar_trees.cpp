class Solution {
public:

    void dfs(TreeNode* root, std::vector<int>& r){
        if(!root->left && !root->right)
            r.push_back(root->val);
        if(root->left)
            dfs(root->left, r);
        if(root->right)
            dfs(root->right, r);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        std::vector<int> r1;
        std::vector<int> r2;

        dfs(root1, r1);
        dfs(root2, r2);

        return r1 == r2;
    }
};
