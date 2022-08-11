#将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#比如输入字符串: "PAYPALISHIRING" ，numRows = 3
#按 Z 字形排列显示如下：
#P   A   H   N
#A P L S I I G
#Y   I   R
#之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len=len(s)
        row_count=numRows
        str={}
        return_str=""
        if numRows==1:
            return s
        for i in range(row_count):# 循环遍历行
            str[i]=""# 初始化每一行的字符串
        for i in range(0,s_len):# 循环遍历字符串
            i1=0
            if i%(numRows+numRows-2)>=numRows:
                i1=numRows-(i%(numRows+numRows-2))%(numRows)-2# 当前字符串的位置
            else:
                i1=(i%(numRows+numRows-2))%(numRows)# 当前字符串的位置
            if i1<numRows:# 如果当前字符串的位置在第一列,则放到对应的行
                str[i1]+=s[i]# 将当前字符串放到对应的行
            else:# 如果当前字符串的位置不在第一列,则放到对应的行
                str[numRows(i1-numRows)].append(s[i])# 将当前字符串放到对应的行
        #str的个数是numRows,每个str的长度是numRows
        for i in range(numRows):
            return_str+=str[i]
        return return_str

        

def test1():
    s=Solution()
    print(s.convert("AB",3))
    # print(s.convert("PAYPALISHIRING",4))
    
test1()


