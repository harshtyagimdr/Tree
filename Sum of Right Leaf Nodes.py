int rightLeafSum(Node* root)
{
    if(!root)
    {
    return 0;
    }
    int sum=0;
    
    sum += rightLeafSum(root->left);
    sum += rightLeafSum(root->right);
    
    if(root->right && !root->right->left && !root->right->right)
    return sum+root->right->data;
    else return sum;
}