class Solution {
public:
string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0") return "0";
        if(num1.length() > num2.length()) {string temp = num1;num1 = num2;num2 = temp;}
        vector<string> strs;
        for(int i = num1.length()-1; i >= 0; i--){
            int carry = 0; 
            string s1 = ""; 
            for(int j = num2.length()-1; j >= 0; j--){
                string sp = to_string((num1[i]-'0') * (num2[j]-'0') + carry);
                int p = stoi(sp);
                carry = (sp.length() > 1) ? p/10 : 0;
                if(j == 0){
                    reverse(sp.begin(), sp.end());
                    s1.append(sp);
                    break;
                }
                if(sp.length()>1) s1.push_back(sp[1]);
                else s1.push_back(sp[0]);
            }
            reverse(s1.begin(), s1.end());
            for(int k = num1.length()-1; k > i; k--) s1.push_back('0');
                strs.push_back(s1);
                if(strs.size() > 1){
                    int ztp = strs[0].length() - strs[1].length();
                    ztp = (ztp < 0) ? -1*ztp : ztp;

                    if(strs[0].length() > strs[1].length()){ 
                        for(int l = 0; l < ztp; l++){
                            strs[1].insert(0, "0");
                        }
                    }else{
                        for(int l = 0; l < ztp; l++){
                            strs[0].insert(0,"0");
                        }
                    }
        string sum = ""; 
        int carry = 0; 
        for(int l = strs[0].length()-1; l >=0; l--){
            string sm = to_string((strs[0][l]-'0') + (strs[1][l]-'0') + carry);
            if(l == 0){ 
                if(sm.length()>1){ 
                    sum.push_back(sm[1]);
                    sum.push_back(sm[0]);
                }
                else sum.push_back(sm[0]);
                break;
            }
            if(sm.length() > 1){
                carry = sm[0]-'0';
                sum.push_back(sm[1]); 
            }else{ 
                carry = 0;
                sum.push_back(sm[0]); 
            }
        }
        reverse(sum.begin(), sum.end());
        strs.pop_back();
        strs.pop_back();
        strs.push_back(sum);
        }
    }
    return strs[0];
    }
};
