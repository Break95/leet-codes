
bool cmp(std::pair<string, int>& a, std::pair<string, int>& b){
        return a.second > b.second;
}

class Solution {
public:

    string frequencySort(string s) {
        std::map<char, int> mymap;
        string solve = "";

        for(auto ch: s)
            mymap[ch] += 1;

        std::vector<std::pair<string, int>> vec;

        for(auto& it: mymap)
            vec.push_back(std::pair<string,int>(std::string(1, it.first), it.second));

        std::sort(vec.begin(), vec.end(), cmp);

        for(auto& ch : vec)
            while(ch.second--)
                solve += ch.first;

        return solve;
    }
};
