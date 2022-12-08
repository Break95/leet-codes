class Solution {
public:
    bool halvesAreAlike(string s) {
        int l = 0;
        int r = 0;

        int j = s.size()/2;

        std::set<char> vowels({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'});

        for(int i = 0; i < s.size()/2; ++i){
            if (vowels.find(s[i]) != vowels.end())
                l += 1;

            if (vowels.find(s[j]) != vowels.end())
                r += 1;

            ++j;
        }

        return l == r;
    }
};
