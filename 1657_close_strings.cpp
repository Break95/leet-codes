bool cmp(int& a, int& b){
        return a > b;
}

template <typename Map>
bool key_compare(Map const& lhs, Map const& rhs ) {
    return lhs.size() == rhs.size()
        && std::equal(lhs.begin(), lhs.end(), rhs.begin(),
                     [](auto a, auto b){ return a.first == b.first; });
}

class Solution {
public:
    bool closeStrings(string word1, string word2) {

        if(word1.length() != word2.length())
            return false;

        std::map<char, int> charFreqA, charFreqB;
        std::map<char, int> setA, setB;


        for(int i = 0; i < word1.length(); ++i){
            charFreqA[word1[i]] += 1;
            charFreqB[word2[i]] += 1;
        }

        std::vector<int> vecA, vecB;
        for(auto& it: charFreqA)
            vecA.push_back(it.second);
        for(auto& it: charFreqB)
            vecB.push_back(it.second);

        if(!key_compare(charFreqA, charFreqB))
            return false;

        std::sort(vecA.begin(), vecA.end(), cmp);
        std::sort(vecB.begin(), vecB.end(), cmp);

        for(int i = 0; i < vecA.size(); ++i){
            if(vecA[i] != vecB[i])
                return false;
        }

    return true;
    }
