// https://www.hackerrank.com/challenges/balanced-brackets
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {
    
    static Dictionary<char,char> closing =new Dictionary<char,char>()
                                                  {
                                                    {'(',')'},
                                                    {'{','}'},
                                                    {'[',']'}
                                                  };                                                    
    static string isBalanced(string s) {
      if(s.Length == 0 || s.Length % 2 != 0)
        return "NO";
      
      Stack<char> openingStack = new Stack<char>();
      
      char[] letters =s.ToCharArray();
      foreach(char c in letters)
      {
        if(closing.ContainsKey(c))
          openingStack.Push(c);
        else
        {
          if(openingStack.Count==0)
            return "NO";
          
          var currentOpen = openingStack.Pop();
          
          if(closing[currentOpen]!=c)
            return "NO";
        }
      }
      
      return openingStack.Count==0?"YES":"NO";      
    }

    static void Main(String[] args) {
        int t = Convert.ToInt32(Console.ReadLine());
        for(int a0 = 0; a0 < t; a0++){
            string s = Console.ReadLine();
            string result = isBalanced(s);
            Console.WriteLine(result);
        }
    }
}
