
// https://www.hackerrank.com/challenges/maximum-element
 static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
      int n =int.Parse(Console.ReadLine());
      Stack<int> stack=new Stack<int>(); 
      Stack<int> maxStack=new Stack<int>(); 
      for(int i = 0;i<n;i++)
      {
        string data = Console.ReadLine();
        var splitted = data.Split(' ');
        string commandType = splitted[0];
        if(commandType=="1"){
          var val =int.Parse(splitted[1]);
          stack.Push(val);   
          if(maxStack.Count == 0|| val>=maxStack.Peek())
            maxStack.Push(val);
        }else if(commandType=="2"){
          var popped = stack.Pop();
          if(popped == maxStack.Peek())
            maxStack.Pop();
        }else {
          Console.WriteLine(maxStack.Peek());
        }
      }
    }