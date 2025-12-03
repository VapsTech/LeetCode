class Solution {
public:
    string addBinary(string a, string b) 
    {
        int a_nBits = a.size();
        int b_nBits = b.size();

        char largestString;
        int smallestSize = 0;
        int biggestSize = 0;
        if (a_nBits >= b_nBits)
        {
            largestString = 'a';
            smallestSize = b_nBits;
            biggestSize = a_nBits;
        }
        else
        {
            largestString = 'b';
            smallestSize = a_nBits;
            biggestSize = b_nBits;
        }

        string sum = ""; // result

        int carry = 0;
        int i = a_nBits; // a string index
        int j = b_nBits; // b string index

        int t = 0;
        while (t < smallestSize)
        {
            i--;
            j--;
            if (a[i] == '1' && b[j] == '1') // 1 + 1
            {
                sum.push_back(carry ? '1' : '0');
                carry = 1;
            }
            else if (a[i] == '0' && b[j] == '0') // 0 + 0
            {
                sum.push_back(carry ? '1' : '0');
                carry = 0; 
            }
            else // a[i] != b[j]
            {
                if (carry)
                {
                    sum.push_back('0');
                    carry = 1;
                }
                else
                {
                    sum.push_back('1');
                    carry = 0;
                }
            }
            t++;
        }

        // Handle remaining bits of the longer string
        while (t < biggestSize)
        {
            i--;
            j--;
            if (largestString == 'a')
            {
                if (a[i] == '1')
                {
                    if (carry)
                    {
                        sum.push_back('0');
                        carry = 1;
                    }
                    else
                    {
                        sum.push_back('1');
                    }
                }
                else
                {
                    if (carry)
                    {
                        sum.push_back('1');
                        carry = 0;
                    }
                    else
                    {
                        sum.push_back('0');
                    }
                }
            } 
            else 
            {
                if (b[j] == '1')
                {
                    if (carry)
                    {
                        sum.push_back('0');
                        carry = 1;
                    }
                    else
                    {
                        sum.push_back('1');
                    }
                }
                else
                {
                    if (carry)
                    {
                        sum.push_back('1');
                        carry = 0;
                    }
                    else
                    {
                        sum.push_back('0');
                    }
                }
            }
            t++;
        }

        // Final carry
        if (carry)
            sum.push_back('1');

        reverse(sum.begin(), sum.end());
        return sum;
    }
};