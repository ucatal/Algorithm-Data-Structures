using NUnit.Framework;
using System;

namespace DataStructuresAlgorithm
{
    public class Toptal_Task2_Zigzag_BinaryTree
    {
        [Test]
        public int Task2(Tree T)
        {
            return FindLongestZigZag(T, 0) - 1;
        }

        private int FindLongestZigZag(Tree t, int currentMaxValue)
        {
            if (t == null) return 0;

            int leftCount = CountTree(t, true, 0);
            int rightCount = CountTree(t, false, 0);

            currentMaxValue = Math.Max(leftCount, rightCount);
            currentMaxValue = Math.Max(currentMaxValue, FindLongestZigZag(t.l, currentMaxValue));
            currentMaxValue = Math.Max(currentMaxValue, FindLongestZigZag(t.r, currentMaxValue));

            return currentMaxValue;
        }

        private int CountTree(Tree node, bool moveLeft, int count)
        {
            if (node == null) return count;

            count = moveLeft
                ? CountTree(node.l, !moveLeft, node.l == null ? count : count + 1)
                : CountTree(node.r, !moveLeft, node.r == null ? count : count + 1);

            return count;
        }
    }

    public class Tree
    {
        public int x;
        public Tree l;
        public Tree r;
    };
}