using NUnit.Framework;

namespace DataStructuresAlgorithm
{
    /// <summary>
    /// it's solution of toptal task 3
    /// </summary>
    public class ToptalTask3Test
    {
        [Test]
        public void TestCaseOne()
        {
            int[] A = { 3, 2, 1 };
            int D = 1;
            int expectedResult = 3;

            var result = Result(A, D);

            Assert.AreEqual(result, expectedResult);
        }

        [Test]
        public void TestCaseTwo()
        {
            int[] A = { 1, 2, 3, 4, -1, -1, -1 };
            int D = 3;
            int expectedResult = -1;

            var result = Result(A, D);

            Assert.AreEqual(result, expectedResult);
        }

        private int Result(int[] A, int D)
        {
            int N = A.Length;
            if (D > N)
                return 0;
            int position = -1;
            int time = 0;
            int stonesWontSurface = 0;

            while (stonesWontSurface != D)
            {
                var oldPosition = position;
                stonesWontSurface = 0;

                for (int i = position + D; i > position; i--)
                {
                    if (i >= A.Length)
                        return time;
                    if (A[i] == -1)
                        stonesWontSurface++;
                    else if (A[i] <= time)
                    {
                        position = i;
                    }
                }

                if (stonesWontSurface == D)
                    return -1;

                if (position == oldPosition)
                {
                    int minimumTimeToStoneSurfacing = int.MaxValue;
                    for (int i = position + D; i > position; i--)
                    {
                        if (A[i] < minimumTimeToStoneSurfacing && A[i] > time)
                        {
                            minimumTimeToStoneSurfacing = A[i];
                        }
                    }
                    time = minimumTimeToStoneSurfacing;
                }
            }
            return time;
        }
    }
}