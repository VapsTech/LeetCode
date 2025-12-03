class Solution {
public:
    string addBinary(string a, string b) 
    {
        //NOTE: We assum a is always the largest sequence of bits

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

        string sum = "";

        int carry = 0;
        int i = a_nBits;
        int j = b_nBits;

        int t = 0;
        while (t < smallestSize)
        {
            i--;
            j--;
            if (a[i] == '1' && b[j] == '1')
            {
                sum.push_back(carry ? '1' : '0');
                carry = 1;
            }
            else if (a[i] == '0' && b[j] == '0')
            {
                sum.push_back(carry ? '1' : '0');
                carry = 0; // unchanged
            }
            else // a!=b, one is 1
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
